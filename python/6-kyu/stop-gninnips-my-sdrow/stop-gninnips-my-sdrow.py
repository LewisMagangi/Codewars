def spin_words(sentence):
    # Your code goes here
    words = sentence.split()
    reversed_words = (word[::-1] if len(word) > 4 else word for word in words)
    return ' '.join(reversed_words)