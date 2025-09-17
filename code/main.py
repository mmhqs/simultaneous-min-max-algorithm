# Finds the minimum and the maximum value in a list
def max_min_select(numberList, startIndex=0, endIndex=None):
    if endIndex is None:
        endIndex = len(numberList) - 1

    # Base case 1: list with only one number
    if startIndex == endIndex:
        return numberList[startIndex], numberList[startIndex]

    # Caso base 2: list with two numbers
    if startIndex + 1 == endIndex:
        if numberList[startIndex] > numberList[endIndex]:
            return numberList[startIndex], numberList[endIndex]
        else:
            return numberList[endIndex], numberList[startIndex]

    # Divide: find the midpoint to divide the list
    midpoint = (startIndex + endIndex) // 2

    # Conquer: call the function recursively for both halves
    max1, min1 = max_min_select(numberList, startIndex, midpoint)
    max2, min2 = max_min_select(numberList, midpoint + 1, endIndex)

    # Combine the results
    max_final = max(max1, max2)
    min_final = min(min1, min2)

    return max_final, min_final


def main():
    print("----- Min. and max. value calculator -----\n")
    try:
        numbers_list_string = input("Enter a list of numbers like 1,2,3,4: ")
        numbers_list_int = numbers_list_string.split(',')

        try:
            numbers_list_int = [
                int(numero.strip()) for numero in numbers_list_int]
        except ValueError:
            print("Erro: A entrada contém valores que não são números válidos.")

        max, min = max_min_select(numbers_list_int)

        print(f"\nList: {numbers_list_int}")
        print(f"Minimum value: {min}")
        print(f"Maximum value: {max}")

    except ValueError:
        print("\nError: Please enter a valid list of numbers.")


if __name__ == "__main__":
    main()
