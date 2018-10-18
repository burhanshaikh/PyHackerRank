# Program to print the number from the given string using find and slice
text = "X-DSPAM-Confidence:    0.8475"
s1 = text.find('0')
s2 = text[s1:50] #using slice stringvariable[x:y] where y is not included
fnum = float(s2)
print(fnum)
