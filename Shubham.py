from collections import Counter
def is_permutation_exists(pattern, text):
    pattern_len = len(pattern)
    text_len = len(text)

    if pattern_len > text_len:
        return "NO"

    pattern_counter = Counter(pattern)
    current_window_counter = Counter(text[:pattern_len])
    for i in range(pattern_len, text_len):
        if pattern_counter == current_window_counter:
            return "YES"
        current_window_counter[text[i - pattern_len]] -= 1
        current_window_counter[text[i]] += 1

    if pattern_counter == current_window_counter:
        return "YES"
    return "NO"
T = int(input("Enter the number of test cases: "))
for _ in range(T):
    pattern = input().strip()
    text = input().strip()
    result = is_permutation_exists(pattern, text)
    print(result)