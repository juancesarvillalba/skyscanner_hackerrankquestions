# skyscanner_hackerrankquestions
skyscanner_hackerrank quesitons
Question 1 : Find the Most Popular Destination:

Your task is to find the most popular holiday destination from a list of destinations searched for by users. You are given as standard input the integer size of the list, followed by the names of the destinations themselves. The input has the following format:

on the first line, the count of items in the list
on the subsequent lines, the name of each destination searched for, one per line (each destination is a single word with no spaces, destinations can be searched for and appear more than once) The input is correct. There is at least one destination in the input. Write a program that reads the input from stdin and then outputs out the name of the most searched for destination i.e. the destination that appears most in the list. One destination is guaranteed to be the outright winner in the input.
Examples:

Input:
    6
    Barcelona
    Edinburgh
    Barcelona
    Miami
    Miami
    Barcelona
Output:
    Barcelona
Input:
    5
    Singapore
    Bangkok
    Singapore
    Bangkok
    Singapore
Output:
    Singapore Find the Most Popular Destination:

Your task is to find the most popular holiday destination from a list of destinations searched for by users. You are given as standard input the integer size of the list, followed by the names of the destinations themselves. The input has the following format:

on the first line, the count of items in the list
on the subsequent lines, the name of each destination searched for, one per line (each destination is a single word with no spaces, destinations can be searched for and appear more than once) The input is correct. There is at least one destination in the input. Write a program that reads the input from stdin and then outputs out the name of the most searched for destination i.e. the destination that appears most in the list. One destination is guaranteed to be the outright winner in the input.
Examples:

Input:
    6
    Barcelona
    Edinburgh
    Barcelona
    Miami
    Miami
    Barcelona
Output:
    Barcelona
Input:
    5
    Singapore
    Bangkok
    Singapore
    Bangkok
    Singapore
Output:
    Singapore
    
    
 Question 2: Find the Common Manager

You are given as standard input the number of employees in a company, the first names of two selected employees in a company, and the direct line management relations between every employee. Each person in the company can directly line manage a maximum of 2 other employees. The input has the following format: * on the first line, the number of unique employees in the company * on the second line, the name of the first selected employee (a first name only without spaces) * on the third line, the name of the second selected employee (a first name only without spaces, guaranteed to be different from the first selected employee) * on the subsequent lines, the line management relations in the format "EmployeeX EmployeeY" - meaning EmployeeX manages EmployeeY (first names without spaces and spaces are used to separate the two names)

The input is correct (there are only direct line management relations, no cycles, all employees appear in the input). For simplicity, the first line after the selected employees (line 4) always contains the manager at the top of the hierarchy. Write a program that reads the input from stdin and then outputs out the name of the single employee at the lowest point in the hierarchy to which the two selected employees report, either directly or indirectly. If one employee reports to the other, either directly or indirectly, print out the name of the highest of the two selected employees.

Examples:

Input:
    6
    Hilary
    James
    Sarah Fred
    Sarah Paul
    Fred Hilary
    Fred Jenny
    Jenny James
Output:
    Fred
Input:
    4
    Simon
    Claudiu
    Sarah Claudiu
    Sarah Paul
    Claudiu Simon
Output:
    Claudiu 
Input:
    5
    Gareth
    Alex
    June Alex
    June Qing
    Qing Paul
    Qing Gareth
Output:
    June
 
 
