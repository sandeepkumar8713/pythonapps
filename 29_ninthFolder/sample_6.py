# https://www.db-fiddle.com/f/2oBnepc45fVTauWNy8E9XZ/1
# https://www.db-fiddle.com/f/naYe8qoayEDtDUxHLvRX3w/2

def solution(S):
    # Implement your solution here
    freq_dict = dict()
    for i, ch in enumerate(S):
        if ch == 'a':
            freq_dict[ch] = i
        if ch == 'b':
            if ch not in freq_dict:
                freq_dict[ch] = i

    a_occr = freq_dict.get('a', None)
    b_occr = freq_dict.get('b', None)

    if a_occr is None or b_occr is None:
        return True

    if b_occr > a_occr:
        return True

    return False

if __name__ == "__main__":
    S = "aabbbb"
    print (solution(S))

    S = "ba"
    print (solution(S))

    S = "aaa"
    print (solution(S))

    S = "b"
    print (solution(S))

    S = "abba"
    print (solution(S))

    S = ""
    print (solution(S))

