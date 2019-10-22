# The Turing machine
The program is able to simulate a single headed and single tape Turing ma- chine from a json machine description given as a parameter to the program. The json machine description is sligthly simplier than a formal description of the same machine.

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
