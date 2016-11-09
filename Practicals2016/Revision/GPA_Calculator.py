"""
<50 = N, 50-64 = P, 65-74 = C, 75-84 = D, >= 85 = HD.
(Floats should be handled, e.g. 74.95 is a C.)
"""

__author__ = "Cameron Clark"

with open("GPA_Calculator.txt", "r") as in_file:
    for line in in_file:
