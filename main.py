def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        report(text)


def count_words(text):
    return len(text.split())

def count_chars(text):
    lt = text.lower()
    out = {}
    for ch in lt:
        if ch in out:
            out[ch] += 1
        else:
            out[ch] = 1
    return out

def report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document\n")
    out = []
    for ch, count in count_chars(text).items():
        if ch.isalpha():
            out.append({ch: count})
    out.sort(reverse=True, key=lambda x: list(x.values())[0])
    for item in out:
        ch = list(item.keys())[0]
        count = list(item.values())[0]
        print(f"The '{ch}' character was found {count} times")

main()