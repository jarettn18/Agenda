"""
Author: Jarett Nishijo
Mini-Project Week 4
"""

from typing import List

Waldo = 'W'
Other = '.'

def all_row_exists_waldo(grid: List[List[str]]) -> bool:
    """There is a Waldo in every row"""
    for row in grid:
        if Waldo in row:
            pass
        else:
            return False
    return True

def all_col_exists_waldo(grid: List[List[str]]) -> bool:
    """There is a Waldo in every column"""
    if len(grid) == 0:
        return True
    for col_i in range(len(grid[0])):
        found_waldo = False
        for row_i in range(len(grid)):
            if grid[row_i][col_i] == Waldo:
                found_waldo = True
        if not found_waldo:
            return False
    return True

def all_row_all_waldo(grid: List[List[str]]) -> bool:
    """There are all waldos in every row"""
    for row in grid:
        for col in row:
            if col != Waldo:
                return False
    return True

def all_col_all_waldo(grid: List[List[str]]) -> bool:
    """There are all waldos in every column"""
    if len(grid) == 0:
        return True
    for col_i in range(len(grid[0])):
        for row_i in range(len(grid)):
            if grid[row_i][col_i] != Waldo:
                return False
    return True

def exists_row_all_waldo(grid: List[List[str]]) -> bool:
    """There exists  a row that contains all Waldos"""
    for row in grid:
        all_waldos = True
        for col in row:
            if col != Waldo:
                all_waldos = False
                break
        if all_waldos:
            return True
    return False

def exists_col_all_waldo(grid: List[List[str]]) -> bool:
    """There exists a col that contains all Waldos"""
    if len(grid) == 0:
        return False
    for col_i in range(len(grid[0])):
        for row_i in range(len(grid)):
            all_waldos = True
            if grid[row_i][col_i] != Waldo:
                all_waldos = False
                break
        if all_waldos:
            return True
    return False

def exists_row_exists_waldo(grid: List[List[str]]) -> bool:
    """There exists a row that contains a Waldo"""
    for row in grid:
        for col in row:
            if col == Waldo:
                return True
    return False

def exists_col_exists_waldo(grid: List[List[str]]) -> bool:
    """There exists a col that contains a Waldo"""
    if len(grid) == 0:
        return False
    for col_i in range(len(grid[0])):
        for row_i in range(len(grid)):
            if grid[row_i][col_i] == Waldo:
                return True
    return False

