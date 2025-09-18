#miniproject
#chabumru and tthongch
from checkmate import checkmate

def main():
    # Example 1
    board1 = """\
R...
.K..
..P.
....\
"""
    checkmate(board1)   #Success

    # Example 2
    board2 = """\
..
.K\
"""
    checkmate(board2)   #Fail

    #For TEST
    board3 = """\
........
.......A
.K......
....P...
"""
    checkmate(board3)   #For TEST
    
    #For TEST Err1
    board4 = 1

    checkmate(board4) #For TEST

    #For TEST Err2
    board5 = """\
"""
    checkmate(board5)   #For TEST

    #For TEST Err3
    board6 = """\
........
.......A
...K....
....P...
"""
    checkmate(board6)   #For TEST


if __name__ == "__main__":
    main()