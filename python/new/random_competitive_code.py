from collections import defaultdict, deque

def first_non_repeating_character(stream):
    char_count = defaultdict(int)  # Dictionary to store character frequencies
    queue = deque()  # Queue to maintain the order of characters

    for char in stream:
        # Increase the count of the current character
        char_count[char] += 1

        # Add the character to the queue if it's the first occurrence
        if char_count[char] == 1:
            queue.append(char)

        # Remove characters from the queue if they are repeated
        while queue and char_count[queue[0]] > 1:
            queue.popleft()

    # If the queue is empty, there are no non-repeating characters
    if not queue:
        return None
    else:
        # Return the first non-repeating character
        return queue[0]

# Example usage:
stream = "abaabacda"
print("First non-repeating character:", first_non_repeating_character(stream))  # Output: 'b'