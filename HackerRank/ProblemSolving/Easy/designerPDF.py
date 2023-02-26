def designerPdfViewer(h: list[int], word: str) -> int:
    """
    Each letter gets 1mm for wide, h for height.
    :param h: heights of each letter
    :param word: word that will be printed
    :return: size in mm2 
    """
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    max_height = 0
    for letter in word:
        if h[abc.index(letter)] > max_height:
            max_height = h[abc.index(letter)]
        if max_height == max(h):
            break
    return max_height * len(word)

print(designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
"abc"))