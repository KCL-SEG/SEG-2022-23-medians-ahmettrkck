"""Median calculator."""

def calculate_mean(num1, num2):
    return (num1 + num2) / 2


def calculate_median(numbers):
    numbers.sort()
    length = len(numbers)

    if length % 2 != 0:
        return numbers[length//2]
    else:
        return calculate_mean(numbers[length//2], numbers[length//2 - 1])

def main():
    while True:
        try:
            print("Enter a list of numbers separated by commas: ")
            numbers = [float(value) for value in input().split(",")]
        except ValueError:
            print("Some input could not be converted to a number!")
        else:
            break

    print(calculate_median(numbers))


if __name__ == "__main__":
    main()




