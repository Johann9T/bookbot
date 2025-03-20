def get_book_text():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file, "r" , encoding="utf-8") as f:
    # do something with f (the file) here
        file_contents = f.read()
        return file_contents
def main():
    from stats import count_words   
    get_book_text() 
    count_words()    
if __name__ == "__main__":   
    main()