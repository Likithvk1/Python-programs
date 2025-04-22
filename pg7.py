a= "!!!Harry!!!!  !!!!!! @@@@@@"
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.rstrip("!!!"))
print(a.endswith("!!!"))
print(a.count("r"))
print(a.center(50))
print(a.replace("Harry","John"))
print(a.split(" "))
str1="He's name is Dan.He's  good boy."
print(str1.find("is"))
print(str1.find("ishhh"))
# print(str1.index("ishhh"))
str1="welcometothechannel"
print(str1.isalnum())   #reutrns true if the string exsits bewteen A-Z,a-z,0-9 
str1="welcome"
print(str1.isalpha())# returns true only if exists alphabets from a-z,A-z and no numeric characters
str1="welcome"
print(str1.isprintable())# reurns false if there are any escape squnce characters
str1="welcome"
print(str1.islower())
str1="      "#using space 
print(str1.isspace())
str1="World Health Organization"
print(str1.istitle())#checks if the first letter of every word is captial or not
str1="welcome"
print(str1.isupper())
str1="welcome"
print(str1.startswith("welcome"))#cheks if the string starts with sentence or character 
str1="welcome"
print(str1.swapcase())#converts lowercase letters to uppercase and vice versa
str1="His name is Dan.He's  good boy."
print(str1.title())#converts every first letter to upper case

