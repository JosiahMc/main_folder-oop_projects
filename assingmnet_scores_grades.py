# Assignment: Scores and Grades
# Write a function that generates ten scores between 
# 60 and 100. Each time a score is generated, your 
# function should display what the grade is for a 
# particular score. Here is the grade table:

# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A
# The result should be like this:

# Scores and Grades
# Score: 87; Your grade is B
# Score: 67; Your grade is D
# Score: 95; Your grade is A
# Score: 100; Your grade is A
# Score: 75; Your grade is C
# Score: 90; Your grade is A
# Score: 89; Your grade is B
# Score: 72; Your grade is C
# Score: 60; Your grade is D
# Score: 98; Your grade is A
# End of the program. Bye!


import random

def scoregrade():
    print "Scores and Grades"
    for i in range(0, 30):
        score = random.randint(50, 100)
        if score >= 50 and score <= 59:
            print "Holy smokes: {0}; how hard is this stuff?!?!??!".format(score)
        elif score >= 60 and score < 70:
            print "Score: {0}; Your grade is D".format(score)
        elif score >= 70 and score < 80:
            print "Score: {0}; your grade is C".format(score)
        elif score >= 80 and score < 90:
            print "Score: {0}; your grade is B".format(score)
        elif score >= 90 and score <= 100:
            print "Score: {0}; your grade is A".format(score)
    print "End of the program. Bye!"

scoregrade()