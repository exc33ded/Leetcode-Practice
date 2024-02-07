class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        counter1, counter2 = 0,0
        
        sl = s.lower()
        split_word = list(sl)
        lst_char = ' '.join(split_word)
 
        low = 0
        high = len(lst_char) - 1
        while (low < high):
            if lst_char[low] in "aeiou":
                counter1 += 1

            if lst_char[high] in "aeiou":
                counter2 += 1
            low += 1
            high -= 1

        if counter1 == counter2:
            return True
        return False

