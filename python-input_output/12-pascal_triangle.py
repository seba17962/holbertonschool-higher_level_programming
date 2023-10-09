#!/usr/bin/python3
"""_summary_
"""
def pascal_triangle(n):
    """_summary_

    Args:
        n (int):

    Returns:
        list: triangle pascal
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(0, n):
        row = []
        for j in range(0, i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                prev_row = triangle[i - 1]
                value = prev_row[j - 1] + prev_row[j]
                row.append(value)
        triangle.append(row)
    return triangle
