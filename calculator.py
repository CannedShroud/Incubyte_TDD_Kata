class Calculator:
    def add(self, numbers: str) -> int:
        """
        Adds numbers from a given string.

        Args:
            numbers (str): A string containing numbers separated by delimiters.

        Returns:
            int: The sum of the numbers. Returns 0 if the string is empty.
        """
        ret = 0

        if not numbers:
            return ret

        nums = numbers.split(",")
        for num in nums:
            ret += int(num)

        return ret
