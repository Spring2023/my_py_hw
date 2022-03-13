#1.
word = 'by'
print(len(word))

empty = ''
print(len(empty))

i_am = 'I\'m'
print(len(i_am))

#2.
multiline = 'Line
Line'

print(len(multiline))

#3.
multiline = '''Line #1
Line #2'''

print(len(multiline))
        
multiline1 = """Line #1
Line #2"""

print(len(multiline1))

#4.
str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

#5.
char_1 = 'a'
char_2 = ' '

print(ord(char_1))
print(ord(char_2))

char_greek = 'α'
char_polish = 'ę'

print(ord(char_greek))
print(ord(char_polish))

#6.
print(chr(97))
print(chr(945))

#7.
x = "a"
x1 = 97
print(type(x))
print(type(ord(x)))
print(type(chr(x1)))

print(chr(ord(x)), x)
print(chr(ord(x)) == x)

print(ord(chr(x1)), x1)
print(ord(chr(x1)) == x1)

#8.
the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()

#9.
the_string = 'silly walks'

for ix in range(len(the_string) - 1, - 1, -1):
    print(the_string[ix], end=' ')

print()

#10.
the_string = 'silly walks'

for character in the_string:
    print(character, end='\n')

print()

#11.
alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])        
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::3])

#12.
alphabet = "abcdefghijklmnopqrstuvwyz"

print("f" in alphabet)
print("F" in alphabet)
print("l" in alphabet)        
print("ghi" in alphabet)
print("Xyz" in alphabet)

#13.
alphabet = "abcdefghijklmnopqrstuvwyz"

print("f" not in alphabet)
print("F" not in alphabet)
print("l" not in alphabet)        
print("ghi" not in alphabet)
print("Xyz" not in alphabet)

#14.
alphabet = "abcdefghijklmnopqrstuvwyz"

print(alphabet)
print()

del alphabet
print(alphabet)

#15.
alphabet = "bcdefghijklmnopqrstuvwy"
alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)

#16.
print(min("aAbByYzZ"))

t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

space = min(t)
print("is a space:", "\"", space, "\"", sep="")
print(ord(space))
print()

t = [0, 1, 2]
print(min(t))

#17.
print(max("aAbByYzZ"))

t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

#18.
print("aAbByYzZ".index("b")+1)
print("aAbByYzZ".index("Z")+1)
print("aAbByYzZ".index("A")+1)

#19.
st = "abcabc"
print(st, type(st), list(st))
print()

di = {1: "1", 2: "2"}
print(di, type(di), list(di))
print()

tup1 = ("1", "2")
print(tup1, type(tup1), list(tup1))
print()

#20.
print("abcabc".count("b"))
print("abcabc".count("d"))
print()

#21.
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("Alpha".capitalize())

#22.
print('[' + 'alpha'.center(10) + ']')
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')

print('[' + 'gamma'.center(20, '*') + ']')

#23.
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")

#24.
t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

#25.
print("Eta".find("ta"))
print("Eta".find("mma"))
print()

#26.
t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))
print()

#27.
the_text = """A variation of the ordinary lorem ipsum text has been used in typesetting since the 1960s or earlier, when it was popularized by advertisements for Letraset transfer sheets. It was introduced to the Information Age in the mid-1980s by Aldus Corporation, which employed it in graphics and word processing templates for its desktop publishing program, PageMaker"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)
print()

#28.
print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))

#29.
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

#30.
t = 'Six lambdas'
print(t.isalnum())

t = '20E1'
print(t.isalnum())

#31.
print("Moooo".isalpha())
print('Mu40'.isalpha())

print('2018'.isdigit())
print("Year2019".isdigit())

#32.
print("Moooo".islower())
print("moooo".islower())
print('\n'.isspace())
print(" ".isspace())
print("moooo moooo moooo".isspace())
print('Moooo'.isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

#33.
print(",".join(["omicron", "pi", "rho"]))

#34.
print("SiGma=60".lower())

#35.
print("[" + " tau ".lstrip() + "]")
print("www.vk.com".lstrip("w."))
print("python.org".lstrip(".org"))

#36.
print("www.vk.com".replace("vk.com", "python.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))

#37.
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

#38.
print("[" + " upsilon ".rstrip() + "]")
print("vk.com".rstrip(".com"))

#39.
print("phi     chi\npsi".split())
print("omega".startswith("meg"))
print("omega".startswith("om"))
print()
print("[" + "   aleph    ".strip() + "]")

#40.
print("I know that I know nothing.".swapcase())
print()
print("I know that I know nothing. Part 1.".title())
print()
print("I know that I know nothing. Part 2.".upper())

