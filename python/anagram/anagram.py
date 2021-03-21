def find_anagrams(word, candidates):
    output_list = list()
    word_list = list(word.lower())
    for w in candidates:
        candidate_list = list(w.lower())
        if word.lower() != w.lower() and sorted(word_list) == sorted(candidate_list):
            output_list.append(w)
    return output_list
