def get_longer_word(word1: str, word2: str) -> str:
    word1_len = len(word1)
    word2_len = len(word2)
    
    if word1_len >= word2_len:
        return word1
    else:
        return word2

# do not modify below this line
print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))