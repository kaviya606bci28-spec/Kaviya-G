def print_exactly_twice(nums):
    from collections import Counter
    counts = Counter(nums)
    printed = set()
    for num in nums:
        if counts[num] == 2 and num not in printed:
            print(num, end=" ")
            printed.add(num)

if __name__ == "__main__":
    try:
        nums = list(map(int, input("enter the number:").split()))
        print_exactly_twice(nums)
    except ValueError:
        print("Invalid input. Please enter integers only.")

