def word_count(book_text):

    words_list = book_text.split()
    count = len(words_list)
    print(f"Found {count} total words")

def complete_count(book_text):

    ch_count = {}

    for ch in book_text:
        ch = ch.lower()
        ch_count[ch] = ch_count.get(ch, 0) + 1
        
    
    return ch_count



def sort_help(dict_item):
    return dict_item["num"]



def sort_ch_counts(ch_count):
    ch_list = []

    for ch, count in ch_count.items():
        if ch.isalpha():
            ch_list.append({
                "char": ch,
                "num": count
            })
    ch_list.sort(reverse=True, key=sort_help)
    return ch_list