#How it Works:

### Pseudocode:
    # recursive backtracker
    function solve(board) {
        #find the first position with no number
        empty_spot = find_next_empty_spot(board)
   
        # if there is no empty spot we fond the solution 
        if not empty_spot:
            return True
    
        x, y = empty_spot

        # try numbers from 1 - 9
        for i in range(1,10):
            
            board[x][y] = i
            if checkBoard(board, x, y):
               
                # if board with new number i is valid 
                # then move to the next empty spot 
                if solve(board):
                    return True
                
                board[x][y] = 0

        # if the numbers 1 - 9 don't work for that spot
        # return False -> go to the previous spot and keep trying ...
        list[x][y]
        return False
    }


##Short explanation:

The algorithm searches for the first empty spot on the board,
tries the numbers from 1 to 9 until one doesn't devalidate the board
and then moves on to the next empty spot.
If at any point the number from 1 to 9 can't go into the current spot,
the algorithm backtracks(goes to the previous empty spot) and continues
trying out numbers for that spot. If it finds one it moves forward again
and if there are no more empty spots to try out we found the solution.


##Why can't we just try every solution?

The answer to this question is pretty simple...
The number of possible states of a sudoku lies around 6 * 10 ^ 21, that's a 6 with 21 zeros.
No computer could run such a calculation in a reasonable time.

The backtracking algorithm used for this solver technically has to make 6 * 10^21 checks in the worst case, but it never really gets close to that number.
From my person experience it takes from 30 thousand to 500 thousand checks.
The second number comes from a sudoku, that was named "The world's hardest Sudoku".

