#Write a python script to check if a string contains only characters of the alphabet.

str="iNeuron"
for i in str:
    if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
        pass
    else:
        print("string not contains all characters of alphabet")
        break
else:
    print("string contains only characters of alphabet")