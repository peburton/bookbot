def read_text(file_path):
	with open(file_path) as f:
		return f.read()

def word_counter(file_contents):
	word_count = file_contents.split()
	return len(word_count)

def lower_case(file_contents):
	lowered_string = file_contents.lower()
	return lowered_string

def count_letters(lowered_string):
	freq = {}
	for x in set(lowered_string):
		freq[x] = lowered_string.count(x)
	return freq

def main():
	file_path = "books/frankenstein.txt"
	file_contents = read_text(file_path)
	word_count = word_counter(file_contents)
	lowered_string = lower_case(file_contents)
	letter_freq = count_letters(lowered_string)
	print(file_contents)
	print (f'The number of words in this file is: {word_count}')
	print (f'The number of times each character appears in the text is:{letter_freq}')

if __name__ == "__main__":
    main()
