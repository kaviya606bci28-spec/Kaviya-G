def main():
    try:
        nums = list(map(int, input("Enter 10 integers separated by space: ").split()))
        if len(nums) != 10:
            print("Error: Please enter exactly 10 integers.")
            return
        MyList1 = [n for n in nums if n % 2 == 0 and n % 3 != 0]
        MyList2 = [n for n in nums if n % 9 == 0]
        print("MyList1:", MyList1)
        print("MyList2:", MyList2)
    
    except ValueError:
        print("Invalid input. Please enter integers only.")


if __name__ == "__main__":
    main()
