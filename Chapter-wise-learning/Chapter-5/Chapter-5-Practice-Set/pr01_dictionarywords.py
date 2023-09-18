myDict={
    "Exculpate" :  "Absolve,exonerate,acquit,vindicate",
    "Garrulous" : "Talkitive,locquacious,voluble",
    "Ameliorating" : "Improve,better,help,enrich",
    "Abnegation" : "Denial(Self-Denial),Renunciation,Renouncement",
    "Quibbling" : "To evade the point of an argument by caviling about words,fuss,niggle",
    "Prurient"  : "Showing too much interest in sexual matters,obscene,smutty"
}
print("Options are:",myDict.keys())
a=input("Enter the word whose meaning you want to search:\n")
print(myDict.get(a))
#OR
# print(myDict[a])
