# Meat Processing Factory

This Python code simulates a meat processing factory where multiple employees work concurrently to process servings of beef, pork, and chicken. The code utilizes threading to simulate the concurrent execution of tasks by different employees.

## Functionality

The code implements the following functionalities:

- The `MeatProcessingFactory` class represents the meat processing factory and keeps track of the available servings of beef, pork, and chicken.
- The factory has multiple employees, denoted by letters A, B, C, D, and E.
- Each employee can perform three types of tasks: processing beef, processing pork, and processing chicken.
- Each task involves picking a serving of meat and processing it. Each task has a specific time duration: 1 second for beef, 2 seconds for pork, and 3 seconds for chicken.
- The number of available servings for each meat type is initially set (10 beef servings, 7 pork servings, and 5 chicken servings).
- The code ensures mutual exclusion when accessing and modifying the serving counts by using locks (`beef_lock`, `pork_lock`, and `chicken_lock`).

## Running the Code

To run the code:

1. Make sure you have Python installed on your machine.
2. Save the code in a Python file (e.g., `meat_processing.py`).
3. Open a terminal or command prompt and navigate to the directory where the Python file is saved.
4. Run the code by executing the following command:
``` 
python meat_process.py
```

## Output

All of the output will be write in the console and a `output.txt` file. 

The example of output also can be seen in `output.txt` file in this repo.