# Create a function called "find_substring" that takes a string and a substring as arguments, and returns True if the substring is present in the string, and False otherwise.
def find_substring(string, substring):
    if substring in string:
        return True
    else:
        return False

find_substring("Computer", "Com")