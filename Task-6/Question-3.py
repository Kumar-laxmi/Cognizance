file = open(r"Task-6\about.txt", "r")

# Words should be separated by spaces, commas or full stops.
words = file.read().replace(',','').replace('.','').split(" ")

word_len_6 = []
freq = {}

for word in words:
    # To filter words with length atleast 6
    if len(word) >= 6:
        word_len_6.append(word)
    
    # To count the frequency of each word
    if (word in freq):
        freq[word] += 1
    else:
        freq[word] = 1

print("The words with atleast 6 letters: ")
print(word_len_6)

print("\nThe most frequent word is: {}".format(max(freq, key=freq.get)))

