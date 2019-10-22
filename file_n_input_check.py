# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    file_n_input_check.py                              :+:    :+:             #
#                                                      +:+                     #
#    By: ayundina <marvin@codam.nl>                   +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/21 18:34:23 by ayundina      #+#    #+#                  #
#    Updated: 2019/10/21 18:34:25 by ayundina      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import json
import sys

'''
check_input() checks if the given input for the machine contains only the
symbols from the "alphabet" (in jsonfile).

Param 1: file - is a jsonfile given as a machine description.

Param 2: input - is a str to be processed by the machine.

Returns: None.
'''

def	check_input(file, input):
	for char in input:
		if char not in file['alphabet'] or char in file['blank']:
			print("error: input is incorrect")
			sys.exit()

#	print(state)
#	print(transitions[state])

'''
check_transition() checks if each "state" in "transition" has:
read, to state, write and action.

Param 1: state - is a state to check in "transitions".

Param 2: transitions - is a dictionary to be checked.

Returns: None.
'''

def	check_transition(state, transitions):
	for option in transitions[state]:
		if "read" not in option \
			or "to_state" not in option \
			or "write" not in option \
			or "action" not in option:
			print("error: transition state [", state ,"] has no " \
				"\"read\" or \"to_state\" or \"write\" or \"action\"")

'''
To access values:

print("list.keys:		", list(file.keys()))
print("n_keys:			", len(file))
print("n_transitions:		", len(file['transitions']))
print("n_states:		", len(file['states']))
'''

'''
check_jsonfile() checks the given jsonfile.
1. Checks the presence of all 7 keys and their titles of the keys
2. Checks the number of states in "transitions"
3. Checks if "initial" state is a part of th "states"
4. Checks if "finals" is a sublist of "states"
5. Iterates "states" of "transitions" to check necessary command keys:
read, to state, write and action. Check is done in check_transition() function.

Param 1: file - is a jsonfile given as a machine description

Returns: None
'''

def	check_jsonfile(file):
	keys = list(file.keys())
	must_keys = ['name', 'alphabet', 'blank', 'states', \
		'initial', 'finals', 'transitions']
	if len(file) != 7 or keys != must_keys:
		print("error: file is incorrect. Check keys:", must_keys)
	if len(file['states']) - len(file['finals']) != len(file['transitions']):
		print("error: file is incorrect. Check \"states\" and \"transitions\"")
	if file['initial'] not in file['states']:
		print("error: \"initial\" is not in a list of \"states\"")
	for state in file['finals']:
		if state not in file['states']:
			print("error: \"finals\" is not a sublist of \"states\"")
	for state in file['states']:
		if state not in file['finals']:
			check_transition(state, file['transitions'])

'''
check() - reads and parses arguments from stdin.
Checks the given "jsonfile" and "input" 

Param 1: jsonfile - is a file given as a machine description

Param 2: input - is a str to be processed by the machine

Returns: a dictionary from opened jsonfile
'''

def	check(jsonfile, input):
	with open(jsonfile, 'r') as fd:
		try:
			jsonfile = json.load(fd)
			check_jsonfile(jsonfile)
		except:
			print("error: jsonfile is not valid")
	check_input(jsonfile, input)
	return jsonfile