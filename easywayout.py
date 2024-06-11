import random
from collections import Counter

def sample_words_from_file(file_path, x, output_file_path):
    # Read the paragraph from the file
    with open(file_path, 'r') as file:
        paragraph = file.read()
    
    # Split the paragraph into words
    words = paragraph.split()
    
    # Calculate the frequency of each word
    word_counts = Counter(words)
    
    # Create a list of words weighted by their frequency
    weighted_words = []
    for word, count in word_counts.items():
        weighted_words.extend([word] * count)
    
    # Sample x words with the same probability they appear in the paragraph
    sampled_words = random.choices(weighted_words, k=x)
    
    # Join the sampled words into a sentence
    new_sentence = ' '.join(sampled_words)
    
    # Write the new sentence to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(new_sentence)
    
    return new_sentence

# Example usage
file_path = 'margret.txt'  # Replace with your input text file path
output_file_path = 'sampled_margret.txt'  # Replace with your output text file path
x = 40
new_sentence = sample_words_from_file(file_path, x, output_file_path)
print(new_sentence)
