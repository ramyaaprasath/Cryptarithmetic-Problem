# Code by Ramyaa Prasath - rp3975 and Meghna Manoj Nair - mm13032
# This is AI Project 2
import string
import os

# Function to read the equation from a file
def readFromFile(fileName):
    # Check if the file exists
    if not os.path.isfile(fileName):
        print("The input file does not exist.")
        return None
    try:
        with open(fileName, 'r') as file:
            # Read the first three lines
            lineOne = file.readline().strip()
            lineTwo = file.readline().strip()
            lineThree = file.readline().strip()
            # Check if any of the lines are empty
            if not lineOne or not lineTwo or not lineThree:
                print("The input file is empty or does not contain enough lines.")
                return None
            # Check if the lines contain non-alphabetic characters
            if not lineOne.isalpha() or not lineTwo.isalpha() or not lineThree.isalpha():
                print("The input file contains non-alphabetic characters.")
                return None
        # Return the equation in the format "lineOne + lineTwo = lineThree"
        return f"{lineOne} + {lineTwo} = {lineThree}"
    except Exception as error:
        print(f"Failed to read the file. Error: {error}")
        return None

# Function to break the equation into its components
def splitEquation(equation):
    # Split the equation into its components and return them as a tuple
    return tuple(equation.upper().split())

# Function to get the unique letters in the equation
def fetchDistinctLetters(equation):
    # Create a set of all the characters in the equation
    # Filter out the non-alphabetic characters and return the result as a list
    return [i for i in set(''.join(splitEquation(equation))) if i.isalpha()]

# Function to get the starting letters of the words in the equation
def startingLetters(equation, letters):
    parts = splitEquation(equation)
    return [letters[i] for i in range(len(letters)) if letters[i] in [part[0] for part in parts if part.isalpha()]]

# Function to check if the values assigned to the letters are correct
def validateValues(assignment, equation):
    operand1, operator, operand2, equals, result = splitEquation(equation)
    # Check if all characters have been assigned values
    if all(character in assignment or not character.isalpha() for character in operand1 + operand2 + result):
        # Convert the operands and the result to numbers
        num1 = int("".join(str(assignment.get(character, character)) for character in operand1))
        num2 = int("".join(str(assignment.get(character, character)) for character in operand2))
        sumRes = int("".join(str(assignment.get(character, character)) for character in result))
        # Check if the sum of the operands equals the result
        return num1 + num2 == sumRes
    # If not all characters have been assigned, return False
    return False

# Function to select the next unassigned variable
def chooseUnassignedVar(assignment, letters, domains):
    unassigned = [v for v in letters if v not in assignment]
    if not unassigned:
        return None
    # Sort the unassigned variables by the length of their domain
    # This is the Minimum Remaining Values (MRV) heuristic, which selects the variable with the fewest legal values left in its domain
    unassigned.sort(key=lambda var: len(domains[var]))
    # Find the maximum degree of the unassigned variables
    # This is the Degree Heuristic (DH), which selects the variable that is involved with the largest number of constraints on other unassigned neighbors
    maxDegree = max(len([v for v in unassigned if v != var]) for var in unassigned if len(domains[var]) == len(domains[unassigned[0]]))
    # Return the first unassigned variable with the maximum degree
    return next(var for var in unassigned if len([v for v in unassigned if v != var]) == maxDegree)

# Function to perform a backtrack search
def backtrack(assignment, letters, domains, equation):
    if len(assignment) == len(letters):
        # Check if the assignment is correct if all variables are assigned
        if validateValues(assignment, equation):
            return assignment
        else:
            return None

    # Select the next unassigned variable
    var = chooseUnassignedVar(assignment, letters, domains)
    for value in domains[var]:
        if value not in assignment.values():
            # If the variable is a starting letter and the value is '0', skip this value
            if var in startingLetters(equation, letters) and value == '0':
                continue
            assignment[var] = value
            # Perform a backtrack search with the new assignment
            result = backtrack(assignment, letters, domains, equation)
            if result:
                return result
            del assignment[var]
    # If no assignment could be found, return None
    return None
def solveEquation(equation, outputFile):
    if equation is None:
        return
    letters = fetchDistinctLetters(equation)
    # Check if there are more than 10 unique letters in the equation
    if len(letters) > 10:
        with open(outputFile, 'w') as file:
            file.write("INVALID EQUATION : Too many letters to have valid answer\n")
        return
    operand1, operator, operand2, equals, result = splitEquation(equation)
    # Check if the equation meets the format 4 letters + 4 letters = 5 letters
    if not (len(operand1) == 4 and len(operand2) == 4 and len(result) == 5):
        print("Your input file doesn't meet the format 4 letters + 4 letters = 5 letters. But I will compute it anyway.")
    assignment = {}
    # Initialize the domains of the variables with all digits
    domains = {var: list('0123456789') for var in letters}
    # Perform a backtrack search to find a valid assignment
    assignment = backtrack(assignment, letters, domains, equation)
    # If a valid assignment is found, print it and write it to the output file
    if assignment:
        print("Computing...")
        print(f"Original equation: {operand1} + {operand2} = {result}")
        print(f"Solution found with assignment order: {assignment}")
        print(f"Assigned digits: {''.join(str(assignment.get(c, c)) for c in operand1)} + {''.join(str(assignment.get(c, c)) for c in operand2)} = {''.join(str(assignment.get(c, c)) for c in result)}")
        with open(outputFile, 'w') as file:
            file.write("".join(str(assignment.get(c, c)) for c in operand1) + "\n")
            file.write("".join(str(assignment.get(c, c)) for c in operand2) + "\n")
            file.write("".join(str(assignment.get(c, c)) for c in result) + "\n")
    # If no valid assignment is found, write a message to the output file
    else:
        with open(outputFile, 'w') as file:
            file.write("No valid solution found for the given equation.\n")
    print(f"Output stored in {outputFile}")
# Get the equation from the input file
inputFile = input("Enter the name of the input file: ")
equation = readFromFile(inputFile)
if equation:
    outputFile = f"Output_{inputFile.split('.')[0]}.txt"
    # Solve the equation and write the solution to the output file
    solveEquation(equation, outputFile)
