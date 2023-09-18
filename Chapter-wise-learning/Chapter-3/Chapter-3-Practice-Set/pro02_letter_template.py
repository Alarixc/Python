letter='''Dear <|NAME|>,
you have been selected!
<|DATE|>'''
a=input("Enter your name:\n")
b=input("Enter today's date:\n")
letter=letter.replace("<|NAME|>",a)
letter=letter.replace("<|DATE|>",b)
print("\n")
print(letter)

