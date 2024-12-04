
def main ():
    path_to_file = "books/frankenstein.txt"

    file_contents = getText(path_to_file)
    calcLetters = letterCount(file_contents)
    sortedLetters = sort(calcLetters)
    w = wordCount(file_contents)
    log(path_to_file, w, sortedLetters)
    pass
def getText(path_to_file):
    with open(path_to_file) as f:
        return f.read()
def wordCount(text):
    count = len(text.split())
    # print(count)
    return count
# {'p': 6121, 'r': 20818,...
def letterCount(text):
    charCount = {}
    for char in text:
        # if c == " " or c == "\n" or:
        #     pass
        c = char.lower()
        if c in charCount and c.isalpha():
            charCount[c] += 1
        else: 
            if c.isalpha():
                charCount[c] = 1
    # print (charCount)
    return charCount
def sort(letterList):
    def sort_on(dict):
        print(dict["num"])
        return dict["num"]
    arr = []
    for c in letterList:
        arr.append({"letter":c, "num":letterList[c]})
    arr.sort(reverse=True, key=sort_on)
    return arr
def log(bookName, wordCount, sortedLetters):
    # --- Begin report of books/frankenstein.txt ---
    # 77986 words found in the document

    # The 'e' character was found 46043 times
    print (f"--- Begin report of {bookName} ---")
    print (f"{wordCount} words found in the document\n")
    for letter in sortedLetters:
        print(f"the {letter["letter"]} character was found {letter["num"]} times")
    print ("--- End Report ---")
main()