cost_computer=float(input("Enter cost of one computer:\n"))
num_computer=int(input("Enter number of computers:\n"))
cost_chair=float(input("Enter cost of one table:\n"))
num_chairs=int(input("Enter number of chairs:\n"))
num_hours=int(input("Enter number of hours worked:\n"))
wages_perhour=float(input("Enter wages per hour:\n"))
Budget=cost_computer*num_computer+cost_chair*num_chairs+num_hours*wages_perhour
print("Your budget is ",Budget)

