def read_text(file_path):
	with open(file_path) as f:
		return f.read()

def word_counter(file_contents):
	word_count = file_contents.split()
	return len(word_count)

def main():
	file_path = "books/frankenstein.txt"
	file_contents = read_text(file_path)
	word_count = word_counter(file_contents)
	print (f'The number of words in this file is: {word_count}')

if __name__ == "__main__":
    main()
