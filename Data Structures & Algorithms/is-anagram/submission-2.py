class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letter_track = dict()

        for char1 in s:
            letter_track[char1] = letter_track.get(char1, 0) + 1

        for char2 in t:
            if letter_track.get(char2, 0) <= 0:
                return False
            letter_track[char2] = letter_track.get(char2, 0 ) -1 
        return True