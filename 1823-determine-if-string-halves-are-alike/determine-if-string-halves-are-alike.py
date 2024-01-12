class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        counter1, counter2 = 0,0
        
        sl = s.lower()
        split_word = list(sl)
        lst_char = ' '.join(split_word)
 
        low = 0
        high = len(lst_char) - 1
        while (low < high):
            if lst_char[low] == "a" or lst_char[low] == "e" or lst_char[low] == "i" or lst_char[low] == "o" or lst_char[low] == "u":
                counter1 += 1

            if lst_char[high] == "a" or lst_char[high] == "e" or lst_char[high] == "i" or lst_char[high] == "o" or lst_char[high] == "u":
                counter2 += 1
            low += 1
            high -= 1

        if counter1 == counter2:
            return True
        return False

