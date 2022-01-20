from create_confusion_set_kd import *
import pickle


if __name__ == "__main__":
    cwd = os.getcwd()
    fvp = os.path.join(cwd, "confusion-set/all-vietnamese-syllables.txt")
    fvp2 = os.path.join(cwd, "confusion-set/common-vietnamese-syllables.txt")
    full_vocab = load_vocab(fvp)
    common_vocab = load_vocab(fvp2)    
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


    with open('full_confusion_set_2.pickle', 'wb') as handle:
        pickle.dump(full_confusion_set_2, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('full_confusion_set_1.pickle', 'wb') as handle:
        pickle.dump(full_confusion_set_1, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('full_confusion_set_with_common_word_1.pickle', 'wb') as handle:
        pickle.dump(full_confusion_set_with_common_word_1, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('full_confusion_set_with_common_word_2.pickle', 'wb') as handle:
        pickle.dump(full_confusion_set_with_common_word_2, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # Confusion set with regional dialects