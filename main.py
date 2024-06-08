def read_text(file_path):
	with open(file_path) as f:
		return f.read()

def word_counter(file_contents):
	word_count = file_contents.split()
	return len(word_count)

def count_letters(file_contents):
	freq = {}
	lowered = file_contents.lower()
	for x in set(lowered):
		freq[x] = lowered.count(x)
	return freq

def main():
	file_path = "books/frankenstein.txt"
	file_contents = read_text(file_path)
	word_count = word_counter(file_contents)
	letter_freq = count_letters(file_contents)
	print(f'---Begin report of {file_path}---'+'\n'+'\n'+f'The number of words in this file is: {word_count}'+'\n')
	for key, value in letter_freq.items():
		if key.isalpha():
			print(f'The {key} character was found {value} times')

if __name__ == "__main__":
    main()
