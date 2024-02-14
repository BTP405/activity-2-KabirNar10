def wordCount(t):
    """
    Reads a text file and returns a dictionary where the keys are unique words
    and the values are lists of line numbers where those words appear.

    Args:
        t (str): The path to the text file.

    Returns:
        dict: A dictionary containing word counts by line number.
    """

    word_counts = {}
    line_number = 1

    with open(t, 'r') as file:
        for line in file:
            # Convert line to lowercase and split into words
            words = line.lower().split()

            # Update word counts for each word in the line
            for word in words:
                if word not in word_counts:
                    word_counts[word] = []
                word_counts[word].append(line_number)

            line_number += 1

    return word_counts

# Example usage
word_counts = wordCount("my_text.txt")
print(word_counts)
