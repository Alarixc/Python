Dict={
    range(90,100): 'Ex',
    range(80,90): 'A',
    range(70,80): 'B',
    range(60,70): 'C',
    range(50,60): 'D',
    range(0,49): 'F'
}
x=int(input("Enter your marks:\n"))
if(x in range(90,100)):
    print("You got "+Dict[range(90,100)]+" grade")
elif(x in range(80,90)):
    print(f"You got {Dict[range(80,90)]} grade")
elif(x in range(70,80)):
    print(f'You got {Dict[range(70,80)]} grade')
elif(x in range(60,70)):
    print(f'''You got {Dict[range(60,70)]} grade''')
elif(x in range(50,60)):
    print(f"You got {Dict[range(50,60)]} grade")
else:
    print(f"You got {Dict[range(0,49)]} grade")





