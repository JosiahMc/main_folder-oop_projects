
# Assignment: Checkerboard
# Write a program that prints a 'checkerboard'
# pattern to the console.
#
# Your program should require no input and produce
# console output that looks like so:
#
# * * * *
#  * * * *
# * * * *
#  * * * *
# * * * *
#  * * * *
# * * * *
#  * * * *
# Each star or space represents a square. On a traditional checkerboard
# you'll see alternating squares of red or black. In our case we will
# alternate stars and spaces. The goal is to repeat a
# process several times. This should make you think of looping.



def checkers(start,end)
for row in range(start, end):
    strrow = ""
    for i in range(start, end):
        if row % 2 == 0:
            if i % 2 == 0:
                strrow += "*"
            else:
                strrow += " "
        else:
            if i % 2 != 0:
                strrow += "*"
            else:
                strrow += " "
    print strrow
checkers(0,8)
