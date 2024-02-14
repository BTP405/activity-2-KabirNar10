

def graphSnowfall(t, range_sizes):
    """
    Reads snowfall data from a text file and displays it as a bar chart.

    Args:
        t (str): The path to the text file containing snowfall data.
        range_sizes (list): A list of range sizes (e.g., [10, 20, 30]) in centimeters.

    Returns:
        None

    Raises:
        ValueError: If the file is empty or contains non-numerical data.
    """

    with open(t, 'r') as file:
        snowfall_data = [float(line.strip()) for line in file]  # Read and convert data

    if not snowfall_data:
        raise ValueError("File does not contain any valid snowfall data")

    ranges = ["{}cm - {}cm".format(r1, r2) for r1, r2 in zip(range_sizes[:-1], range_sizes[1:])]  # Create range labels
    range_counts = [0] * len(ranges)  # Initialize range counts

    for value in snowfall_data:
        range_index = int(value // range_sizes[0])  # Determine range index based on first size
        if range_index < len(range_counts):  # Ensure index is within valid range
            range_counts[range_index] += 1

    plt.figure(figsize=(8, 6))  # Set figure size for readability
    plt.bar(ranges, range_counts, color='skyblue', edgecolor='black')  # Create bar chart
    plt.xlabel("Snowfall Range (cm)")
    plt.ylabel("Number of Days")
    plt.title("Snowfall Distribution")
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()
    plt.show()

# Example usage
range_sizes = [10, 20, 30, 40, 50]  # Example range sizes (adjust as needed)
graphSnowfall("snowfall.txt", range_sizes)  # Replace "snowfall.txt" with your file path
