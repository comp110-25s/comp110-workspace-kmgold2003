def count_to_n(n:int) -> None:
    count : int = 0
    while count < n:
        print(f"Count is: {count}")
        count = count + 1
    print(f"Count is: {count}")

count_to_n(4)