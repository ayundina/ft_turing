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

def	check_input(file, input):
	for char in input:
		if char not in file['alphabet'] or char in file['blank']:
			print("error: input is incorrect")
			sys.exit()

#	print(state)
#	print(transitions[state])

def	check_transition(state, transitions):
	for option in transitions[state]:
		if "read" not in option \
			or "to_state" not in option \
			or "write" not in option \
			or "action" not in option:
			print("error: transition state [", state ,"] has no " \
				"\"read\" or \"to_state\" or \"write\" or \"action\"")

#	print("list.keys:		", list(file.keys()))
#	print("n_keys:			", len(file))
#	print("n_transitions:		", len(file['transitions']))
#	print("n_states:		", len(file['states']))

def	check_jsonfile(file):
	keys = list(file.keys())
	must_keys = ['name', 'alphabet', 'blank', 'states', \
		'initial', 'finals', 'transitions']
	if len(file) != 7 or keys != must_keys:
		print("error: file is incorrect. Check keys:", must_keys)
	if len(file['states']) - 1 != len(file['transitions']):
		print("error: file is incorrect. Check \"states\" and \"transitions\"")
	if file['initial'] not in file['states']:
		print("error: \"initial\" is not in a list of \"states\"")
	for state in file['finals']:
		if state not in file['states']:
			print("error: \"finals\" is not a sublist of \"states\"")
	for state in file['states']:
		if state not in file['finals']:
			check_transition(state, file['transitions'])


def	check(jsonfile, input):
	with open(jsonfile, 'r') as fd:
		try:
			jsonfile = json.load(fd)
			check_jsonfile(jsonfile)
		except:
			print("error: jsonfile is not valid")
	check_input(jsonfile, input)