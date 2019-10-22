# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    ft_turing.py                                       :+:    :+:             #
#                                                      +:+                     #
#    By: ayundina <marvin@codam.nl>                   +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/21 16:46:52 by ayundina      #+#    #+#                  #
#    Updated: 2019/10/21 16:46:54 by ayundina      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import argparse
import sys
from file_n_input_check import check

def	main():
	parser = argparse.ArgumentParser()
	parser.add_argument('jsonfile', help='json description of the machine')
	parser.add_argument('input', help='input of the machine')
	args = parser.parse_args()
	check(args.jsonfile, args.input)

main()
