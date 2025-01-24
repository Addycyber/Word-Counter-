def count_words(text):
    """
    Count the number of words in the given text.
    
    Args:
        text (str): The input text to count words from.
    
    Returns:
        int: The word count.
    """
    words = text.split()  # Split text into words using spaces
    return len(words)

def main():
    print("Welcome to the Word Counter Program!")
    print("-----------------------------------")
    
    while True:
        # Prompt user for input
        user_input = input("Enter a sentence or paragraph (or type 'exit' to quit): ").strip()
        
        if user_input.lower() == "exit":
            print("Thank you for using the Word Counter. Goodbye!")
            break
        
        if not user_input:
            # Handle empty input
            print("Error: No text entered. Please try again.")
            continue
        
        # Count the words and display the result
        word_count = count_words(user_input)
        print(f"Word Count: {word_count}\n")

if __name__ == "__main__":
    main()
