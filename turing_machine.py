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

'''
self.action = True is == "Right"
self.action = False is == "Left"
'''

class Turing_Machine:
	def __init__(self, tape, init_state):
		self.tape = tape
		self.index = 0
		self.head = tape[self.index]
		self.to_state = init_state
		self.action = True

def	exec_transition(state, machine):
	pass

def	turing_machine(file, input):
	tape = input + file['blank'] * len(input)
	machine = Turing_Machine(tape, file["initial"])
	while machine.to_state not in file['finals']:
		for state in file['transitions']:
			if machine.to_state == state:
				exec_transition(state, machine)