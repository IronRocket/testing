from fractions import Fraction


two_dim = (
    ("w","y","e","j","s","y"),
    ("l","o","a","a","u","o"),
    ("j","v","j","v","c","r"),
    ("a","n","m","a","i","p"),
    ("p","y","t","h","o","n"),
)
counter = 0
length_of_x = len(two_dim[0])
total_number = length_of_x*len(two_dim)
words = ("java","wow")

class Word:
    def __init__(self):
        self.starting_pos = (0,0)
        self.x = 0
        self.y = 0
        self.found = False
word_finder = Word()

while counter <total_number:
    for word in words:
        if two_dim[word_finder.y][word_finder.x] == word[0]:
            word_finder.starting_pos = (word_finder.x,word_finder.y)
            second_letter = word[1]
            def iterate(word,axes,postive=True,iterate=2):
                if postive:
                        iterator = 1
                else:
                    iterator = -1
                if axes == "x":
                    for _ in range(iterate):
                        word.x += iterator
                        if word.x < 0:
                            return False
                        if two_dim[word_finder.y][word_finder.x] == second_letter:
                            return True
                else:
                    for _ in range(iterate):
                        word.y += iterator
                        if word.x < 0:
                            return False
                        if two_dim[word_finder.y][word_finder.x] == second_letter:
                            return True
                return False
            word_finder.x += 1
            word_finder.y += 1
            
            if two_dim[word_finder.y][word_finder.x] == second_letter:
                word_finder.found = True
            
            if not word_finder.found:
                word_finder.found = iterate(word_finder,"x",postive=False)
            if not word_finder.found:
                word_finder.found = iterate(word_finder,"y",postive=False)
            if not word_finder.found:
                word_finder.found = iterate(word_finder,"x")
            if not word_finder.found:
                word_finder.found = iterate(word_finder,"y")

            if word_finder.found:
                print(word_finder.starting_pos)
                print(word_finder.x,word_finder.y)
                rise_run = (word_finder.x-word_finder.starting_pos[0],word_finder.starting_pos[1]-word_finder.y)
                print(rise_run)

            input("done")

    word_finder.x += 1
    if word_finder.x == length_of_x:
        word_finder.x = 0
        word_finder.y += 1
    counter += 1