import re

class Calculator:
    def add(self, numbers: str) -> int:
        """
        Adds numbers from a given string.

        Args:
            numbers (str): A string containing numbers separated by delimiters.

        Returns:
            int: The sum of the numbers. Returns 0 if the string is empty.
        """

        if not numbers:
            return 0

        if numbers.startswith("//") and "\n" in numbers:
            delimiter, numbers = numbers[2:].split("\n")
            nums = numbers.split(delimiter)
        else:
            delimiters = r",|\n"
            nums = re.split(delimiters, numbers)

        return sum(int(num) for num in nums if num)


