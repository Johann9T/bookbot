def count_words():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file, "r" , encoding="utf-8") as f:
        file_contents = f.read()
    num_words = file_contents.split()
    anzahl_wörter = len(num_words)
    print(anzahl_wörter, "words found in the document")

def counting_characters():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file, "r" , encoding="utf-8") as f:
        file_contents = f.read()
        lower_text = file_contents.lower()
        char_dict = {}
        while char in lower_text:
            if char in lower_text:

    
    anzahl_wörter = len(num_words)
