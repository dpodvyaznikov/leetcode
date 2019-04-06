class Solution:
    def uniqueMorseRepresentations(self, words: 'List[str]') -> 'int':
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",
                 ".--","-..-","-.--","--.."]

        reprs = {''.join([MORSE[ord(letter)-ord('a')] for letter in word]) for word in words}

        return len(reprs)
