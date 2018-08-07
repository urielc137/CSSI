def count_spaces(s):
    return s.count(" ")
print(count_spaces("hello world!"))  # => 1
print(count_spaces("wow wow wow "))  # => 3

#Excersize 1
def longest_word (x,y,z):
    if len(x) >= len(y) and len(x) >= len(z):
    return x
elif len(y) >= len(x) and len(y) >= len(z):
    return y
elif len(z) >= len(x) and len(z) >= len(y):
    return z
longest = longest_word("o", "oo", "oof")
print(longest)
