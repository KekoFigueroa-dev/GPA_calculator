# Grade Point Average Calculator

A Python application that helps students calculate their current GPA, determine required grades for desired averages, and simulate grade modifications. Features robust input validation and a fun ASCII art reward!

## Features

- Calculate current GPA from multiple grades with float precision
- Sort and display grades from highest to lowest
- Calculate required grade for achieving desired average
- Simulate "what-if" grade scenarios
- Robust input validation for error prevention
- Fun ASCII art reward upon completion
- User-friendly interface with personalized outputs

## How to Use

1. Enter your name when prompted
2. Input the number of grades (positive integer required)
3. Enter each grade (floating point numbers accepted)
4. View your current grade summary including:
   - Total number of grades
   - Highest and lowest grades
   - Current average
5. Enter your desired average
6. See what grade you need to achieve your goal
7. Try different grade scenarios with the grade modifier
8. Enjoy your ASCII tank reward!

## Technical Details

- Written in Python 3
- Uses list manipulation for efficient grade storage and sorting
- Implements comprehensive input validation with try-except blocks
- Maintains data integrity with deep copy for grade simulations
- Rounds all calculations to 2 decimal places
- Uses f-strings for clean string formatting

## Example Output

```
Welcome to my Grade Point Average (GPA) Calculator App !
What is your name: John
How many grades would you like to enter: 3
Enter grade: 85
Enter grade: 92
Enter grade: 78

Grades highest to lowest:
92
85
78

John's Grade Summary:
    Total number of grades: 3
    Highest grade: 92
    Lowest grade: 78
    Average: 85.0
[...]
```

## Author
Sergio Figueroa (May 2025)