Steven Sparks   
May 25, 2021  
IT FDN 110 A Sp 21: Foundations Of Programming: Python  
Assignment 07 Binary Files and Exceptions  
https://github.com/ssparky77/IntroToProg-Python-Mod07.git (external site)  
  
# Error Handling and Working with Binary Files
  
## Introduction
This paper discusses the steps I completed to create a script demonstrating how error handling and pickling work in Python. I started with a math script I have been working with since the beginning of class. I added functions to that script to clean up my demo, and then I added an error handling and pickling demo.
Working with Functions
This project did not come with a starter file, so the first step required me to write a script to employ error handling and pickling. I am not very creative, so I decided to work with the math code I already wrote. I created functions to capture user input, perform math operations, and display the results.  See Figure 1 below for a snippet of my math function code.
 
### (Figure 1: Math processing code from Assignment07.)
  
## Error Handling
The next step was setting up a Try/Except block for my main script to report when a user entered ‘0’ for the second value. The user entering ‘0’ for the second value created an error because my math script divides the first value by the second, and division by zero is undefined.  See Figure 2 below for a screenshot of my Try/Except Block
 
### (Figure 2: Screenshot of a Try/Except block in Assignment07.py.)
As directed, I used PyCharm for the project.  See Figure 3 below for a screenshot of some of the program’s error handling code running in the preview window of PyCharm.
 
### (Figure 3: Assignment07.py running in PyCharm.)
  
## Pickling
Pickling is writing binary data to and reading binary data from “.dat” files in Python.  To demonstrate pickling, I wrote code to save the user input data from the math program to a binary file and then report the contents of that file back.  Again, I used functions from previous assignments to simplify the presentation of the demo code.  See Figure 4 below for a screenshot of the pickling part of my script for this assignment. 
 
### (Figure 4: Screenshot of my pickling code for Assignment07.py.)
  
## Summary
I feel like I learned more about error handling and pickling through creating this project. Looking back, I think editing and revising code from one of the “list-making” projects we did would have been better to demonstrate my knowledge from this section. Still, I did not come to that realization until after I completed the assignment.  Perhaps next time!
