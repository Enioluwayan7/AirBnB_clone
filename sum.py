#!/usr/bin/python3
def cal_sum(a,b):
    """
    calculate the sum of two numbers.

    args:
    a(int) = The first number.
    b(int) = The second number.

    Returns:
    the sum of a and b.
    """
    result = a + b
    return result

def main():
    num1 = 10
    num2 = 20
    sum_result = cal_sum(num1, num2)
    print(f"The sum of {num1} and {num2} is {sum_result}")


if __name__ == "__main__":
    main()
