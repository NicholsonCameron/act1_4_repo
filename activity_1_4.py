# -*- coding: utf-8 -*-
"""Activity-1.4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NdsuvXHKcBf3KIfTxzag55ZW7PrHuQb5
"""

triangle_area = lambda b, h: 1/2*(b*h)

triangle_area(3,4)

def test_triangle_area():
  assert triangle_area(3,4) == 6
  assert triangle_area(5, 10) == 25
  assert triangle_area(10, 0) == 0
  assert triangle_area(20, 50) == 500
test_triangle_area()

def triangle_area(b, h):
    """Computes the area of a triangle

       Args:
           b (base): a number that is the base of the triangle
           h (height): a number that is the height of the triangle

       Returns:
           A number representing the area of a triangle
    """
    output = 1/2*(b*h)
    return output

def test_triangle_area():
    assert triangle_area(3, 4) == 6
    assert triangle_area(10, 0) == 0
test_triangle_area()

help(triangle_area)
