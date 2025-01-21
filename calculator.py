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

        ret = int(numbers)

        return ret
