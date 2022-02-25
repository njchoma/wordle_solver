
def load_word_list(word_list_file_path):
    english_words = [word.strip() for word in open(word_list_file_path).readlines()]
    return english_words

