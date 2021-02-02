from ..iterators import idx_for_diag_se_from_tr


def longest_common_substring(str1, str2):
    """Uses the dynamic programming approach
    Runtime is O(M*N), where M is the length of str1 and N is the length of str2
    str1 is associated with cols
    str2 is associated with rows
    Depends on idx_for_diag_se_from_tr
    
    Eg. For "abcdaf" and "zbcdf", the results matrix can be generated using:
    cols, rows = list(str1), list(str2)
    matrix = [[1 if item==row else 0 for item in cols] for row in rows]    
    
      a b c d a f 
    z 0 0 0 0 0 0
    b 0 1 0 0 0 0
    c 0 0 1 0 0 0
    d 0 0 0 1 0 0
    f 0 0 0 0 0 1
    
    Traverse the overlap_matrix diagonally southeast from the top right and collect the results
    
    Eg. 1:
    longest_common_substring("abcdaf", "zbcdf")
    [{'start': (4, 5), 'len': 1, 'match': 'f'},
     {'start': (1, 1), 'len': 3, 'match': 'bcd'}]
     
    Eg. 2:
    longest_common_substring("aaaccc", "aaaacc")
    [{'start': (0, 2), 'len': 1, 'match': 'a'},
     {'start': (0, 1), 'len': 2, 'match': 'aa'},
     {'start': (4, 5), 'len': 1, 'match': 'c'},
     {'start': (0, 0), 'len': 3, 'match': 'aaa'},
     {'start': (4, 4), 'len': 2, 'match': 'cc'},
     {'start': (1, 0), 'len': 5, 'match': 'aaacc'},
     {'start': (2, 0), 'len': 2, 'match': 'aa'},
     {'start': (5, 3), 'len': 1, 'match': 'c'},
     {'start': (3, 0), 'len': 1, 'match': 'a'}]
    """
    num_cols = len(str1)
    num_rows = len(str2)
    
    results = []
    prev_match, prev_diag = 0, None
    for row, col in idx_for_diag_se_from_tr(num_rows, num_cols):
        
        curr_match = 1 if str1[col] == str2[row] else 0
        curr_diag = col-row

        if curr_match == 1:
            if curr_diag != prev_diag or prev_match == 0:
                results.append({'start': (row, col),
                                'len': 1,
                                'match': str1[col]
                               })

            elif prev_match == 1:
                results[-1]['len'] += 1
                results[-1]['match'] += str1[col]

        else:
            pass

        prev_match, prev_diag = curr_match, curr_diag
    
    return results
