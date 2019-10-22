# The Turing machine
The program is able to simulate a single headed and single tape Turing ma- chine from a json machine description given as a parameter to the program. The json machine description is sligthly simplier than a formal description of the same machine.

A machine is able to compute an unary addition.

This is a valid exemple of a json machine description for this project:

```
{
    "name"    : "unary_sub",
    "alphabet": [ "1", ".", "-", "=" ],
    "blank"   : ".",
    "states"  : [ "scanright", "eraseone", "subone", "skip", "HALT" ],
    "initial" : "scanright",
    "finals"  : [ "HALT" ],

    "transitions" : {

        "scanright": [
            { "read" : ".", "to_state": "scanright", "write": ".", "action": "RIGHT"},
            { "read" : "1", "to_state": "scanright", "write": "1", "action": "RIGHT"},
            { "read" : "-", "to_state": "scanright", "write": "-", "action": "RIGHT"},
            { "read" : "=", "to_state": "eraseone" , "write": ".", "action": "LEFT" }
        ],

        "eraseone": [
            { "read" : "1", "to_state": "subone", "write": "=", "action": "LEFT"},
            { "read" : "-", "to_state": "HALT"  , "write": ".", "action": "LEFT"}
        ],

        "subone": [
            { "read" : "1", "to_state": "subone", "write": "1", "action": "LEFT"},
            { "read" : "-", "to_state": "skip"  , "write": "-", "action": "LEFT"}
        ],

        "skip": [
            { "read" : ".", "to_state": "skip"     , "write": ".", "action": "LEFT"},
            { "read" : "1", "to_state": "scanright", "write": ".", "action": "RIGHT"}
        ] 
    }
}
```
The json fields are defined as follows:
##### name:
The name of the described machine
##### alphabet:
Both input and work alphabet of the machine merged into a single alphabet for simplicity’s sake, including the blank character. Each character of the alphabet must be a string of length strictly equal to 1.
##### blank:
The blank character, must be part of the alphabet, must NOT be part of the input.
states: The exhaustive list of the machine’s states names.
initial: The initial state of the machine, must be part of the states list.
##### finals:
The exhaustive list of the machine’s final states. This list must be a sub-list of the states list.
##### transitions:
A dictionnary of the machine’s transitions indexed by state name. Each transition is a list of dictionnaries, and each dictionnary describes the transition for a given character under the head of the machine. A transition is defined as follows:
###### read:
The character of the machine’s alphabet on the tape under the machine’s head.
###### to_state:
The new state of the machine after the transition is done.
###### write:
The character of the machine’s alphabet to write on the tape before moving
the head.
###### action:
Movement of the head for this transition, either LEFT, or RIGHT.

# Building
`python3 ft_turing.py unary_sub.json 111-11=`
