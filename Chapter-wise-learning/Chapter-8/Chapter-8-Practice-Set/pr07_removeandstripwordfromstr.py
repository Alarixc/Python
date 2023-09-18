def remove_and_strip(st,word):
    Newstr=st.replace(word," ")
    print(Newstr.strip())



st=input("Enter your string:\n")
word=input("Enter the word that you wanna remove:\n")
remove_and_strip(st,word)