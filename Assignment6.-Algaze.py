"""
Simple triangle utilities.
"""


def is_triangle(a: float, b: float, c: float) -> bool:
    """
    Return True if a,b,c can form a triangle.
    Conditions:
      - Each side > 0
      - Triangle inequality: sum of any two sides > the third
    """
    for x in (a, b, c):
        if x <= 0:
            return False
    return (a + b > c) and (a + c > b) and (b + c > a)


def classify_triangle(a: float, b: float, c: float) -> str:
    """
    Return one of: 'equilateral', 'isosceles', 'scalene', 'right'.
    Raises ValueError if the sides cannot form a triangle.

    'right' takes precedence over 'isosceles'/'scalene' if applicable.
    """
    if not is_triangle(a, b, c):
        raise ValueError("Invalid triangle sides")

    sides = sorted([a, b, c])
    a2, b2, c2 = sides[0] ** 2, sides[1] ** 2, sides[2] ** 2
    is_right = abs((a2 + b2) - c2) < 1e-9

    if sides[0] == sides[2]:
        return "equilateral"
    if is_right:
        return "right"
    if sides[0] == sides[1] or sides[1] == sides[2]:
        return "isosceles"
    return "scalene"


def perimeter(a: float, b: float, c: float) -> float:
    """
    Compute the perimeter of a triangle. Raises ValueError if invalid.
    """
    if not is_triangle(a, b, c):
        raise ValueError("Invalid triangle sides")
    return a + b + c
