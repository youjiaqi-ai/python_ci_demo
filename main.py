def add(a, b):
    """两数相加"""
    return a + b

def multiply(a, b):
    """两数相乘"""
    return a * b

def subtract(a, b):
    """两数相减"""
    return a - b

def divide(a, b):
    """两数相除（除数不能为0）"""
    if b == 0:
        raise ValueError("除数不能为0")
    return a / b