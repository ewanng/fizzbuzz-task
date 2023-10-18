from fizzbuzz import fizzbuzz


def get_user_input():
    # Enter Try block and continue if two valid integers are entered
    try:
        start = int(input("Enter the starting number (1-100): "))
        end = int(input("Enter the ending number (1-100): "))
        return start, end

    # if start or end is not an integer, print error and enter function again
    except ValueError:
        print("Invalid input, please enter an integer.")
        return get_user_input()


def main():
    # call get_user_input() function to get start and end values
    start, end = get_user_input()

    # Call the fizzbuzz function with given start and end numbers
    fizzbuzz_result = fizzbuzz(start, end)
    print("FizzBuzz Result:", fizzbuzz_result)


if __name__ == "__main__":
    main()
