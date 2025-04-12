import stats
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        #print(file_contents)
    return file_contents

def main():
    
    if (len(sys.argv)) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    text = get_book_text(book_path)
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    word_count = stats.get_num_words(text)
    print(f"Found {word_count} total words")
    new_var = stats.counter(text)
    sorted_report = stats.report(new_var)
    print("--------- Character Count -------")
    for item in sorted_report:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

main()