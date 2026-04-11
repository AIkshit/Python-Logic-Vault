def analyze_text(text):
    print(f"\n--- 🔍 Analyzing: '{text}' ---")
    
    # 1. Word Count
    words = text.split()
    word_count = len(words)
    
    # 2. Vowel Count
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    
    # 3. String Reversal
    reversed_text = text[::-1]
    
    # Display Results
    print(f"🔹 Total Words: {word_count}")
    print(f"🔹 Total Vowels: {vowel_count}")
    print(f"🔹 Reversed: {reversed_text}")

if __name__ == "__main__":
    user_input = input("Enter a sentence to analyze: ")
    if user_input.strip():
        analyze_text(user_input)
    else:
        print("Please enter some text next time!")
