##first solution

def is_anagram(s, t):

    if len(s) != len(t):
        return False

    for char in set(s):
        if s.count(char) != t.count(char):
            return False

    return True

## second solution
from collections import Counter

def is_anagram_second(s, t):
    return Counter(s) == Counter(t)