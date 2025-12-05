import sys
from stats import get_book_text, get_num_words, get_char_counts, get_sorted_char_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    content = get_book_text(book_path)
    num_of_words = get_num_words(content)
    char_counts_dict = get_char_counts(content)
    sorted_char_counts_dict = get_sorted_char_dict(char_counts_dict)
    
    print(
        f"============ BOOKBOT ============\n",
        f"Analyzing book found at {book_path}...\n",
        f"----------- Word Count ----------\n",
        f"Found {num_of_words} total words\n",
        f"--------- Character Count -------\n",
        sep="", end=""
    )
    for item in sorted_char_counts_dict:
        char, num = item["char"], item["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")
main()