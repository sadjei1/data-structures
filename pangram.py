import re
def pangram(s):
    s = s.lower()
    letters = re.findall(r'[a-z]', s)
    alphabetical_order = set(letters)

    return "Pangram" if len(alphabetical_order) == 26 else "Not pangram"

print(pangram("sam"))
