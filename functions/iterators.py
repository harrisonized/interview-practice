import itertools
import string


# Functions included in this file:
# # create_matrix_of_idx

# # idx_for_diag_se_from_tr
# # idx_for_diag_se_from_bl
# # idx_for_diag_nw_from_tr
# # idx_for_diag_nw_from_bl
# # idx_for_diag_ne_from_tl
# # idx_for_diag_ne_from_br
# # idx_for_diag_sw_from_tl
# # idx_for_diag_sw_from_br

# # idx_for_diag_se_from_tr_v1
# # idx_for_diag_se_from_bl_v1
# # idx_for_diag_se_from_tr_v0
# # idx_for_diag_se_from_bl_v0


def create_matrix_of_idx(num_rows=2, num_cols=3,
                         is_alphabet=False):
    """Default returns indices:
    [[(0, 0), (0, 1), (0, 2)],
     [(1, 0), (1, 1), (1, 2)],
     
    is_alphabet returns:
    [['A', 'B', 'C'],
     ['D', 'E', 'F'],
    """
    rows, cols = range(num_rows), range(num_cols)
    if is_alphabet is True:
        iterator = itertools.cycle(string.ascii_uppercase)  # alphabet_iterator
    else:
        iterator = iter([(i, j) for i in range(len(rows)) for j in range(len(cols))])  # number_iterator
    
    matrix = [[next(iterator) for col in cols] for row in rows]
    return matrix


def idx_for_diag_se_from_tr(num_rows=2, num_cols=3):
    """Traverse southeast diagonals from top right
    This is the most important variant

    Eg.
    
     0   -1   -2
      \\   \\   \\ 
    1 ['A', 'B', 'C']
      \\   \\   \\ 
      ['D', 'E', 'F']
      
    Returns row and col indices for: C, B, F, A, E, D

    Align two strings where col -> str1, row -> str2
    col: abc    abc     abc
           | => ||  =>  |
    row:   ab   ab     ab
    
    Fastest but reduces readability
    """

    if num_rows <= num_cols:
        
        # upper right triangle
        for col in range(num_cols, num_cols-num_rows, -1):
            row = 0
            while col < num_cols:
                yield row, col
                row += 1
                col += 1

        # middle diagonals
        for col in range(num_cols-num_rows, -1, -1):
            row = 0
            while row < num_rows:
                yield row, col
                row += 1
                col += 1

        # lower left triangle
        for row in range(1, num_rows):
            col = 0
            while row < num_rows:
                yield row, col
                row += 1
                col += 1
                
    else:
                        
        # upper right triangle
        for col in range(num_cols-1, 0, -1):
            row = 0
            while col < num_cols:
                yield row, col
                row += 1
                col += 1
                
        # middle diagonals
        for row in range(num_rows-num_cols+1):
            col = 0
            while col < num_cols:
                yield row, col
                row += 1
                col += 1
                
        # lower left triangle
        for row in range(num_rows-num_cols+1, num_rows):
            col = 0
            while row < num_rows:
                yield row, col
                row += 1
                col += 1


def idx_for_diag_se_from_bl(num_rows=2, num_cols=3):
    """Traverse southeast diagonals from bottom left
    This is the second most important variant

    Eg.
    
      0    1    2
       \\   \\   \\ 
    -1 ['A', 'B', 'C']
       \\   \\   \\ 
       ['D', 'E', 'F']
      
    Returns row and col indices for: D, A, E, B, F, C

    Align two strings where col -> str1, row -> str2
    col:  abc    abc    abc
          |   => ||  =>   |
    row: ab      ab       ab

    Fastest but reduces readability
    """

    if num_rows <= num_cols:
        
        # lower left triangle
        for row in range(num_rows-1, 0, -1):
            col = 0
            while row < num_rows:
                yield row, col
                row += 1
                col += 1
                
        # middle diagonals
        for col in range(0, num_cols-num_rows+1):
            row = 0
            while row < num_rows:
                yield row, col
                row += 1
                col += 1
                
        # upper right triangle
        for col in range(num_cols-num_rows+1, num_cols):
            row = 0
            while col < num_cols:
                yield row, col
                row += 1
                col += 1

    else:
    
        # lower left triangle
        for row in range(num_rows-1, num_rows-num_cols, -1):
            col = 0
            while row < num_rows:
                yield row, col
                row += 1
                col += 1
                
        # middle diagonals
        for row in range(num_rows-num_cols, -1, -1):
            col = 0
            while col < num_cols:
                yield row, col
                row += 1
                col += 1
                
        # upper right triangle
        for col in range(1, num_cols):
            row = 0
            while col < num_cols:
                yield row, col
                row += 1
                col += 1


def idx_for_diag_nw_from_tr(num_rows=2, num_cols=3):
    """Traverse northwest diagonals from top right
    Eg.
    
     0   -1   -2
      \\   \\   \\ 
    1 ['A', 'B', 'C']
      \\   \\   \\ 
      ['D', 'E', 'F']
      
    Returns row and col indices for: C, F, B, E, A, D
    """
    # upper right triangle
    for row in range(num_rows-1):
        col = num_cols-1
        while row >= 0 and col >= 0:
            yield row, col
            row -= 1
            col -= 1
            
    # lower left triangle
    for col in range(num_cols-1, -1, -1):
        row = num_rows-1
        while row >= 0 and col >= 0:
            yield row, col
            row -= 1
            col -= 1


def idx_for_diag_nw_from_bl(num_rows=2, num_cols=3):
    """Traverse northwest diagonals from bottom left
    Eg.
    
      0    1    2
       \\   \\   \\ 
    -1 ['A', 'B', 'C']
       \\   \\   \\ 
       ['D', 'E', 'F']
      
    Returns row and col indices for: D, E, A, F, B, C
    """
    
    # lower left triangle
    for col in range(num_cols-1):
        row = num_rows-1
        while row >= 0 and col >= 0:
            yield row, col
            row -= 1
            col -= 1
            
    # upper right triangle
    for row in range(num_rows-1, -1, -1):
        col = num_cols-1
        while row >= 0 and col >= 0:
            yield row, col
            row -= 1
            col -= 1


def idx_for_diag_ne_from_tl(num_rows=2, num_cols=3):
    """Traverse northeast diagonals from top right
    Eg.
          0    1    2
        //   //   //
    ['A', 'B', 'C'] 3
        //   //   //
    ['D', 'E', 'F']
      
    Returns row and col indices for: A, D, B, E, C, F
    """
    # upper left triangle
    for row in range(num_rows):
        col = 0
        while row >= 0 and col < num_cols:
            yield row, col
            row -= 1
            col += 1

    # lower right triangle
    for col in range(1, num_cols):
        row = num_rows-1
        while row >= 0 and col < num_cols:
            yield row, col
            row -= 1
            col += 1


def idx_for_diag_ne_from_br(num_rows=2, num_cols=3):
    """Traverse northeast diagonals from top right
    Eg.
          0   -1   -2
        //   //   //
    ['A', 'B', 'C'] -3
        //   //   //
    ['D', 'E', 'F']
      
    Returns row and col indices for: F, E, C, D, B, A
    """
    # lower right triangle
    for col in range(num_cols, 0, -1):
        row = num_rows-1
        while row >= 0 and col < num_cols:
            yield row, col
            row -= 1
            col += 1
            
    # upper left triangle
    for row in range(num_rows-1, -1, -1):
        col = 0
        while row >= 0 and col < num_cols:
            yield row, col
            row -= 1
            col += 1


def idx_for_diag_sw_from_tl(num_rows=2, num_cols=3):
    """Traverse southwest diagonals from top left
    Eg.
          0    1    2
        //   //   //
    ['A', 'B', 'C']  3
        //   //   //
    ['D', 'E', 'F']
      
    Returns row and col indices for: A, B, D, C, E, F
    """
    
    # upper left triangle
    for col in range(num_cols):
        row = 0
        while row < num_rows and col >= 0:
            yield row, col
            row += 1
            col -= 1

    # lower right triangle
    for row in range(1, num_rows):
        col = num_cols-1
        while row < num_rows and col >= 0:
            yield row, col
            row += 1
            col -= 1


def idx_for_diag_sw_from_br(num_rows=2, num_cols=3):
    """Traverse southwest diagonals from top left
    Eg.
          0   -1   -2
        //   //   //
    ['A', 'B', 'C'] -3
        //   //   //
    ['D', 'E', 'F']
      
    Returns row and col indices for: F, C, E, B, D, A
    """

    # lower right triangle
    for row in range(num_rows-1, 0, -1):
        col = num_cols-1
        while row < num_rows and col >= 0:
            yield row, col
            row += 1
            col -= 1
    
    # upper left triangle
    for col in range(num_cols-1, -1, -1):
        row = 0
        while row < num_rows and col >= 0:
            yield row, col
            row += 1
            col -= 1


def idx_for_diag_se_from_tr_v1(num_rows=2, num_cols=3):
    """Traverse southeast diagonals from top right
    This is the most important variant

    Eg.
    
     0   -1   -2
      \\   \\   \\ 
    1 ['A', 'B', 'C']
      \\   \\   \\ 
      ['D', 'E', 'F']
      
    Returns row and col indices for: C, B, F, A, E, D

    Align two strings where col -> str1, row -> str2
    col: abc    abc     abc
           | => ||  =>  |
    row:   ab   ab     ab
    """

    # upper right triangle
    for col in range(num_cols-1, -1, -1):
        row = 0
        while row < num_rows and col < num_cols:
            yield row, col
            row += 1
            col += 1
        
    # lower left triangle
    for row in range(1, num_rows):
        col = 0
        while row < num_rows and col < num_cols:
            yield row, col
            row += 1
            col += 1


def idx_for_diag_se_from_bl_v1(num_rows=2, num_cols=3):
    """Traverse southeast diagonals from bottom left
    Eg.
    
      0    1    2
       \\   \\   \\ 
    -1 ['A', 'B', 'C']
       \\   \\   \\ 
       ['D', 'E', 'F']
      
    Returns row and col indices for: D, E, A, F, B, C
    """

    # lower left triangle
    for row in range(num_rows, 0, -1):
        col = 0
        while row < num_rows and col < num_cols:
            yield row, col
            row += 1
            col += 1
            
    # upper right triangle
    for col in range(0, num_cols):
        row = 0
        while row < num_rows and col < num_cols:
            yield row, col
            row += 1
            col += 1


def idx_for_diag_se_from_tr_v0(num_rows=2, num_cols=3):
    """Traverse southeast diagonals from top right
    Eg.
    
     0   -1   -2
      \\   \\   \\ 
    1 ['A', 'B', 'C']
      \\   \\   \\ 
      ['D', 'E', 'F']
      
    Returns row and col indices for: C, B, F, A, E, D

    Align two strings where col -> str1, row -> str2
    col: abc     abc     abc
           |  => ||  =>  |
    row:   ab    ab     ab

    Extra loops, extra checks
    """
    for row_minus_col in range(-num_cols+1, num_rows):
        for row in range(num_cols+row_minus_col):
            col = row-row_minus_col
            if row < num_rows and col >= 0:
                yield row, col


def idx_for_diag_se_from_bl_v0(num_rows=2, num_cols=3):
    """Traverse southeast diagonals from bottom left
    Eg.
    
      0    1    2
       \\   \\   \\ 
    -1 ['A', 'B', 'C']
       \\   \\   \\ 
       ['D', 'E', 'F']
      
    Returns row and col indices for: D, E, A, F, B, C

    Extra loops, extra checks
    Very fast for low num_rows
    """
    for col_minus_row in range(-num_cols, num_rows+1):
        for col in range(num_rows+col_minus_row):
            row = col-col_minus_row
            if row >= 0 and col < num_cols :
                yield row, col
