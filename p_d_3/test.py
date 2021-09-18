# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 19:24:43 2021

@author: Itachi
"""

current_col = 1
column_width = 4
blank_char = ' '
blank_column = format(blank_char, str(column_width))
        
        
current_num = 1
        
        
while current_num <= 100:
            
    if current_num < 10:
         print(format(blank_char, '3') + str(current_num), end = '')
                
    else:
        print(format(blank_char, '2') + str(current_num), end = '')
        
            
    if current_col < 10:
        current_col += 1
            
    else:
        current_col = 1
        print()
                
    current_num += 1
            
print('\n')