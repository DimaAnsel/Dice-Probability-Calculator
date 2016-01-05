# Dice Probability Calculator User Guide

This dice probability calculator is designed for calculating probability of rolling non-numerical or else non-standard dice. It supports arbitrary numbers of arbitrary-sided dice. Dice do not have to have the same number of faces.


## Input File

Input files should be saved as plain text (.txt) files. When entering the name of the input file, omit the .txt suffix (Ex: To instruct the program to process "testdice.txt", enter "testdice").

1. Each line represents a new die.
2. To indicate multiple instances of a die, put "*<number of occurences" at the beginning of the line, before any spaces or tabs, followed by either a space or a tab. See example below.
2. Faces of a die are separated by spaces or tabs. Faces cannot contain spaces, tabs, pound signs, or asterisks.
3. To indicate multiple instances of a face on a die, use "<face name>*<number of occurences>". See example below.
5. Anything past a pound sign (#) on a line is ignored.
6. Empty lines are ignored.

Example input file:

    attack defense movement*3 no_action # This die has 1 attack face, 1 defense face, 3 movement faces, and 1 no_action face.

    # The '*2' in the following line indicates that two die should be rolled.
    *2 green green blue*6               # This die has 2 green faces and 6 blue faces.


## Output File

The program outputs a comma-separated value (.csv) file containing a list of the dice rolls, as well as how many times they can occur and the percentage chance of each combination occuring. This file can be viewed in most spreadsheet programs.