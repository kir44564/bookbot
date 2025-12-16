import sys
from stats import word_count, complete_count, sort_ch_counts

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    book_text = get_book_text(book_path)

    print("----------- Word Count ----------")
    word_count(book_text)

    print("--------- Character Count -------")
    ch_stats = complete_count(book_text)
    sorted_stats = sort_ch_counts(ch_stats)
    
    for item in sorted_stats:
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

main()
    
