class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        hm = {  
            'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".",
            'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---",
            'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---",
            'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-",
            'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--..",
        }

        st = set()

        for word in words:
            res = ""
            for char in word:
                res += hm[char]
            st.add(res)

        return len(st)