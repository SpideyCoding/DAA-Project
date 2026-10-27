## Overview

This Python program calculates the **minimum number of visits required to check every lecture exactly once**, given a set of available visit times and the start and end times of the lectures. If it is impossible to check every lecture exactly once under the given constraints, the program reports that no valid solution exists.

## Requirements

- Python
- No external libraries are required. The program uses only Python's standard library.

## How to Run

1. Download the Python code file named `daa_project.py`.
2. Open a terminal or command prompt in the directory containing `daa_project.py`.
3. Run the following command:

   ```bash
   python main.py
   ```

4. Follow the prompts to enter the available visit times and lecture intervals.

## Input Format

The program expects the following inputs:

1. **Number of available visit times (`n`):** An integer indicating how many possible visit times are available.
2. **Available visit times:** Enter `n` times, one per line, in `HH:MM` format using a 24-hour clock.
3. **Number of lectures (`k`):** An integer indicating the number of lectures.
4. **Lecture intervals:** Enter the start and end times of each lecture on a single line, separated by a space. Use `HH:MM HH:MM` format.

### Example Input

```text
Enter number of available visit times: 4
Enter visit times in HH:MM format:
09:00
12:00
15:00
18:00
Enter number of lectures: 2
Enter lecture start and end times (HH:MM HH:MM):
10:00 13:00
14:00 17:00
```

## Output

The program prints the minimum number of visits required to check every lecture exactly once.

For the example above, the output is:

```text
Minimum visits required: 2
```

If no valid solution exists, the program prints:

```text
Not possible to check every lecture exactly once.
```

## Notes and Assumptions

- All times must be provided in `HH:MM` format using the 24-hour clock.
- Lecture start and end times are interpreted as inclusive endpoints.
- An interval with the same start and end time is treated as a single time point by the interval-checking function.
- The program assumes that the input times and lecture intervals are valid.

