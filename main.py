from create_confusion_set_kd import *



if __name__ == "__main__":
    full_vocab = load_vocab("./all-vietnamese-syllables.txt")
    common_vocab = load_vocab("./common-vietnamese-syllables.txt")
    full_vocab_telex_dict = {x: decompose_to_telex(x) for x in full_vocab}

    # Confusion set with keystroke of 2
    full_confusion_set_2 = create_confusion_set_kd(full_vocab_telex_dict, m_keystroke_distance_2)
    full_confusion_set_with_common_word_2 = full_confusion_set_2.copy()
    for word in full_confusion_set_with_common_word_2:
        confusion_set = full_confusion_set_with_common_word_2[word]
        new_confusion_set = [c for c in confusion_set if c in common_vocab]
        full_confusion_set_with_common_word_2[word] = new_confusion_set
        
    # Confusion set with keystroke of 1
    full_confusion_set_1 = create_confusion_set_kd(full_vocab_telex_dict, m_keystroke_distance_1)
    full_confusion_set_with_common_word_1 = full_confusion_set_1.copy()
    for word in full_confusion_set_with_common_word_1:
        confusion_set = full_confusion_set_with_common_word_1[word]
        new_confusion_set = [c for c in confusion_set if c in common_vocab]
        full_confusion_set_with_common_word_1[word] = new_confusion_set

    # Confusion set with regional dialects