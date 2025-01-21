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

        delimiters = r",|\n"

        if numbers.startswith("//") and "\n" in numbers:
            delimiter, numbers = numbers[2:].split("\n")
            delimiters += f"|{delimiter}"
        
        nums = re.split(delimiters, numbers)

        negatives = [n for n in nums if int(n) < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed {', '.join(negatives)}")

        return sum(int(num) for num in nums if num)


