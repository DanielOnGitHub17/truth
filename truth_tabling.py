import re
import unittest, timeit, time
# if number of variables (n > 10) use normal get combinations else use get combinations better (has better time complexity)
def get_combinations_columns(n):
    # if n > ... input("continue at your own risk? max == n") if yess...
    max_comb = group_of = 2 ** n
    columns = []
    while group_of != 1:
        row = ''
        group_of //= 2
        for i in range(max_comb//group_of):
            # repeat instead of switch
            row +=  group_of * ('F' if (i % 2) else 'T')
        columns.append(row)
    return columns

def get_combinations_columns_better(n):
    max_comb = group_of = 2 ** n
    columns = []
    while group_of != 1:
        group_of //= 2
        columns.append((group_of*'T'+group_of*'F') * (max_comb // group_of // 2))
    return columns
    

def get_combinations_rows_from_columns(n):
    rows = []
    columns = get_combinations_columns_better(n)
    outer = len(columns)
    inner = len(columns[0])
    for i in range(inner):
        rows.append('')
        for col in columns:
            rows[-1] += col[i]
    return rows

if __name__ == "__main__":
    print(*get_combinations_rows_from_columns(int(input())), sep='\n')