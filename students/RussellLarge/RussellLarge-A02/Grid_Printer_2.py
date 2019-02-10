multi_dash = dash * n
line = plus + multi_dash
full_line = line * 2 + plus
column_lines = col + space * n
full_col_line = column_lines * 2 + '|'
print(full_line)
print((full_col_line + '\n') * n, end=full_line)
print('\n' + (full_col_line + '\n') * n, end=full_line)
print()