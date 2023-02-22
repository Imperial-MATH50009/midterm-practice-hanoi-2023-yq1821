# Principles of Programming mid-term test practice

The instructions are similar those that will be on the test. This exercise
won't be manually marked, but there are tests and the autograder, and you can
ask questions on Ed about this problem.

## Instructions

1. Ensure your Principles of Programming venv is active.
2. Clone this repository.
3. Complete the programming tasks. Tests are provided for parts 2-4 inclusive.
   Parts 1 and 5.1 are tested by the autograder when you push.
4. Commit and push as you go. **Do not** rely on one big commit and push at the
   end of the test. Only commits timestamped before the end of the test
   will count.

The tests and autograder are a guide, the test will be manually marked in order
to ensure that your code doesn`t produce the right output for the wrong reasons,
and in order to allocate the part 5.2 style marks.

## The task

The towers of Hanoi is a classic children's game in which a stack of discs of
decreasing size is arranged on one of three posts. The objective is to move the
whole stack to another post according to the following rules.

1. Only one disc can be moved at once.
2. No disc may be placed on top of a smaller disc.

[![Photo of the towers of Hanoi game](Tower_of_Hanoi.jpg)](https://commons.wikimedia.org/wiki/File:Tower_of_Hanoi.jpeg)

Your challenge is to write a package implementing this game.

### Part 1 (2 marks)

Create a package `hanoi` containing a module `hanoi.py`. Make the
package installable.

### Part 2 (3 marks)

In the `hanoi.hanoi` module, create a class `Game`. The constructor of this
class should take a single integer parameter which is the number of discs. The
class should internally set up three stacks, numbered 0, 1, and 2. Stack number
0 should contain the numbers from 1 to the number of discs, with 1 at the top of
the stack and the numbers increasing with stack depth. We will interpret a
larger number as indicating a larger disc. (2 marks)

Implement a method `stack()` which takes a single integer parameter whose value
is a stack number (0, 1, or 2). `stack()` should return a list containing the
contents of the specified stack, in order from bottom to top. (1 mark)

### Part 3 (3 marks)

Implement the `__str__` special method. The output should be a string containing
three lines, one for each stack. Each line should consist of the symbol `>`
followed by a space, followed by a comma-separated list of the disc numbers
currently on that stack. For example, in a game with 5 discs in which one disc
has been moved to stack 2, the output would be:

    > 5, 4, 3, 2
    > 
    > 1

As a reminder, lines within a string are separated by the newline character, `"\n"`.

### Part 4 (8 marks)

Implement a method `move()` which takes two integer parameters, `from_stack` and
`to_stack`. Assuming that this is a legal move, invoking this method should move
the top disc on `from_stack` to the top position on `to_stack`. (3 marks)

The following erroneous inputs should be handled: 
1. If `from_stack` is empty, then the method should raise `ValueError` with the
   an error message of the following form. For example, if `from_stack==0` then
   the error would be `Stack 0 is empty.` (2 marks)
2. If the disc being moved has a higher number than the top disc on `to_stack`,
   then the method should raise `ValueError` with an error message of the
   following form. For example if the user attempted to place disc 2 on disc 1,
   then the error message would be `Cannot place disc 2 on disc 1.` (2 marks)

If one of these exceptions occurs, the `Game` should be left in the state it was
in before `move()` was called. (1 mark)

### Part 5 (4 marks)

1. Ensure that your code passes Flake8 (2 marks); and 
2. otherwise conforms to good programming style as we have learned in this
   course (2 marks).

There is no need to write any docstrings for this test.
