def divide(dividend, divisor):
    if divisor == 0:
        return "Division by zero is not allowed."
    left = 0
    right = abs(dividend)
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if mid * abs(divisor) <= abs(dividend):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    if (dividend < 0) != (divisor < 0):
        answer = -answer
    return answer
print("Quotient:", divide(25, 4))
