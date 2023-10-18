
def fizzbuzz(start, end):
    # Input Validation - Return appropriate response if flagged

    # Check if the type of start or end numbers is not an integer
    if type(start) != int or type(end) != int:
        return "Invalid input: please enter integers only"

    # Check if start or end is outside the range of 1-100
    if start < 1 or end > 100:
        return "Invalid input: start and end numbers need to be between 1 and 100"

    # Check if the start number is greater than the end number
    if start > end:
        return "Invalid input: start number greater than end number"

    # Check if the start and end numbers are equal
    if start == end:
        return "Invalid input: start and end numbers cannot be equal"

    # Declare result variable to return from function
    result = []

    '''Loop over each number in the range of given start 
    number and end number (inclusive)'''
    for num in range(start, end + 1):
        # Write each number to end result
        result.append(num)

        # Check if number is divisible by 3 and write fizz to result variable
        if (num % 3) == 0:
            result.append("fizz")

        # Check if number is divisible by 5 and write buzz to result variable
        if (num % 5) == 0:
            result.append("buzz")

    return result


if __name__ == '__main__':
    fizzbuzz()
