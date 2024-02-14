def printStats(t):
    """
    Reads numerical data from a text file and prints statistics.

    Args:
        t (str): The path to the text file containing numerical data.

    Raises:
        ValueError: If the file is empty or contains non-numerical data.
    """

    data = []
    total = 0.0
    count = 0

    try:
        with open(t, 'r') as file:
            for line in file:
                try:
                    # Convert line to a numerical value (float)
                    value = float(line.strip())
                    data.append(value)
                    total += value
                    count += 1
                except ValueError:
                    # Ignore non-numerical lines
                    pass

        if not data:
            raise ValueError("File contains no numerical data")

        # Calculate statistics
        average = total / count
        maximum = max(data)

        # Print formatted statistics
        print("Number of values:", count)
        print("Sum:", total)
        print("Average:", average)
        print("Maximum:", maximum)

    except FileNotFoundError:
        print("Error: File not found")

# Call the function with your file name
printStats("t.txt")
