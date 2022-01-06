class Cal(object):
    def add_num_and_double(self,x,y):
        """Add and double

        >>> c = Cal()
        >>> c.add_num_and_double(1,1)
        4

        >>> c.add_num_and_double('1','1')
        Traceback (most recent call last):
        ...
        ValueError
        """
        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x + y
        result *= 2
        return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()

"""Error: expect 5 result
**********************************************************************
File "/Users/jeonsuhyeon/projects/Study-Python/udemy/161.docktest.py", line 6, in __main__.Cal.add_num_and_double
Failed example:
    c.add_num_and_double(1,1)
Expected:
    5
Got:
    4
**********************************************************************
1 items had failures:
1 of   2 in __main__.Cal.add_num_and_double
***Test Failed*** 1 failures.
"""