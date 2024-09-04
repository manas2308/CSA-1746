from itertools import permutations

# Function to solve the cryptarithmetic problem
def solve_cryptarithmetic(crypt_words, result_word):
    unique_chars = set("".join(crypt_words) + result_word)
    
    if len(unique_chars) > 10:
        return "Invalid problem: more than 10 unique characters."
    
    for perm in permutations('0123456789', len(unique_chars)):
        mapping = dict(zip(unique_chars, perm))
        
        # Skip permutations where a word starts with '0'
        if any(mapping[word[0]] == '0' for word in crypt_words + [result_word]):
            continue
        
        # Convert words to numbers
        crypt_numbers = [int("".join(mapping[char] for char in word)) for word in crypt_words]
        result_number = int("".join(mapping[char] for char in result_word))
        
        if sum(crypt_numbers) == result_number:
            return {char: int(mapping[char]) for char in mapping}
    
    return "No solution found."

# Example usage:
crypt_words = ['SEND', 'MORE']
result_word = 'MONEY'

# Solve the problem
solution = solve_cryptarithmetic(crypt_words, result_word)
print(solution)
