import sys

#명령어 -> python 67.lesson.py option1 option2
print(sys.argv)
"""
['67.lesson.py', 'option1', 'option2']
"""

#명령어 -> python 67.lesson.py option1 option2
for i in sys.argv:
    print(i)
"""
67.lesson.py
option1
option2
"""