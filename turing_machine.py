# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    turing_machine.py                                  :+:    :+:             #
#                                                      +:+                     #
#    By: ayundina <marvin@codam.nl>                   +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/22 16:08:32 by ayundina      #+#    #+#                  #
#    Updated: 2019/10/22 16:08:34 by ayundina      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import sys

class Color:
	HEAD = '\033[42m\033[30m'
	ENDH = '\033[0m'

class Turing_Machine:
	def __init__(self, tape, init_state):
		self.tape = list(tape)
		self.head = 0
		self.to_state = init_state
		self.action = "RIGHT"

'''
next_state() loops through the instructions of current state,
finds the suitable to current condition instruction,
changes the state and variables according to the instruction.
Shows error if the input can't be solved by the given jsonfile/dictionary.

Param 1: state - is a state from "transitions".

Param 2: machine - is a Turing_Machine class

Returns: None.
'''

def	next_state(state, machine):
	i = 0
	states = len(state)
	while i < states:
		if machine.tape[machine.head] == state[i]['read']:
			machine.to_state = state[i]['to_state']
			machine.tape[machine.head] = state[i]['write']
			machine.action = state[i]['action']
			if state[i]['action'] == 'RIGHT':
				machine.head += 1
			elif state[i]['action'] == 'LEFT':
				machine.head -= 1
			if machine.head < 0 or machine.head >= len(machine.tape):
				print("\nerror: no solution")
				sys.exit()
			break
		i += 1

'''
exec_transition() prints the output of the steps and moves to the next state.

Param 1: state - is a state from "transitions".

Param 2: machine - is a Turing_Machine class

Returns: None.
'''

def	exec_transition(state, machine):
	print("\t[", end = '')
	print(*machine.tape[0:machine.head], sep = '', end = '')
	print(Color.HEAD + machine.tape[machine.head] + Color.ENDH, end = '')
	print(*machine.tape[machine.head + 1:], sep = '', end = '')
	print("] (" + machine.to_state + ",", end = ' ')
	print(machine.tape[machine.head] + ") ->", end = ' ')
	next_state(state, machine)
	print("(" + machine.to_state + ",", machine.tape[machine.head] + ",", \
		machine.action + ")")
	
'''
turing_machine() creates a finite tape,
Creates a Turing_Machine class named "machine"
Launches the machine.

Param 1: file - is the opened jsonfile.

Param 2: input - is a user input for machine to solve

Returns: None.
'''

def	turing_machine(file, input):
	tape = input + file['blank'] * (len(input) * 2)
	machine = Turing_Machine(tape, file["initial"])
	print("\n" + "*" * 80, sep = '')
	while machine.to_state not in file['finals']:
		exec_transition(file['transitions'][machine.to_state], machine)
	print("")
