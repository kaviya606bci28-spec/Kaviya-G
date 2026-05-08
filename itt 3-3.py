def print_pattern(n1, n2):
    if not (isinstance(n1, int) and isinstance(n2, int)):
        print("Error: Inputs must be integers.")
        return
    if n1 > n2:
        print("Error: N1 must be less than or equal to N2.")
        return
    for end in range(n2, n1 - 1, -1):
        for num in range(n1, end + 1):
            print(num, end=" ")
            print() 
try:
    n1, n2 = map(int, input().split())
    print_pattern(n1, n2)
except ValueError:
    print("Invalid input. Please enter two integers separated by space.")
