from collections import defaultdict
import operator
import sys


def max_beauty(s):
    char_score = defaultdict(int)
    s = s.upper()
    for char in s:
        if ord(char) >= 65 and ord(char) <= 90:
            char_score[char] += 1

    sorted_scores = sorted(char_score.iteritems(), 
                           key=operator.itemgetter(1),
                           reverse=True)
    current_score = 26
    total = 0
    for k, v in sorted_scores:
        total += v * current_score
        current_score -= 1

    return total

if __name__ == "__main__": 
    test_cases = open(sys.argv[1], 'r')
     
    for test in test_cases:
        print max_beauty(test)

    test_cases.close()
