# Tame of Thrones (Geektrust)
This is my submission for the geektrust tame-of-thrones problem.

Problem Statement
Shan, the gorilla king of the Space kingdom wants to rule all Six Kingdoms in the universe of Southeros.

There is no ruler today and pandemonium reigns. Shan is sending secret messages to all kingdoms to ask for their allegiance. Your coding challenge is to help King Shan send the right message to the right kingdom to win them over. Each kingdom has their own emblem and the secret message should contain the letters of the emblem in it. Once Shan has the support of 3 other kingdoms, he is the ruler!

Input needs to be read from a text file, and output should be printed to console. Your program should execute and take the location to the test file as parameter.

## Design patterns used:
- MVC 
- Factory Pattern

## Solution Details
Requirements
Python3
Usage
To run the program :
py -m geektrust <AbsoluteInputFilePath>
Note: Sample Input File included: SampleInput.py
To build the program (run with tests) run command: py -m build <AbsoluteInputFilePath>
Additional Details
The input file is required to be in the following format:
KINGDOM_1 SECRET_MSG_TO_KINGDOM_1 KINGDOM_2 SECRET_MSG_TO_KINGDOM_2 … KINGDOM_N SECRET_MSG_TO_KINGDOM_N

The program is built on taking a few assumptions:

If multiple messages are sent to a kingdom, even a Single Accepted Message would make them ally for our kingdom and all the Unaccaptable Messages recieved thereafter would be disregarded.
The project is designed for extensible use. This is doen by making a Configuration file (globals\configs.py) where all the configuration parameters are added that can be modified according to the requirements of the end-user.
In future more ways apart from sending messages can be used to make allies. Abstract services for that have been made.
Also different ciphers can be used in future so abstract services about that have been made.
