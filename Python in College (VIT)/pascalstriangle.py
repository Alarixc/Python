def get_next_row(row):
    new_row = []
    prev = 0
    for num in row:
        new_row.append(num + prev)
        prev = num
    new_row.append(prev)
    return new_row

row = [1]
n=int(input("Enter the number of rows you want in your element:\n"))
for i in range(n):
    print(*row)
    row = get_next_row(row)
    