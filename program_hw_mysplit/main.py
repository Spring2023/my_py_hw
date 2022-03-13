from sys import path

path.append("..\\packages")

from packages.mysplit.module_mysplit import mysplit


print(mysplit("To be or not to be, that is the question "))
print(mysplit("To be or not to be,that is the question "))
print(mysplit(" "))
print(mysplit(" abc "))
print(mysplit(""))
