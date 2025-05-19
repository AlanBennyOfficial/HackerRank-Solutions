# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
TESTER = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
for _ in range(int(input().strip())):
    print("Valid" if TESTER.search(input().strip()) else "Invalid")

# Other method

# def is_valid_card(card):
#     pattern = r"^(\d{4}[-\S]?){4}$"
#     return bool(re.match(pattern, card)) # and not re.search(r"(\d)(-?\1){3}", card) and card[0] in "456" # Hackerrank's method