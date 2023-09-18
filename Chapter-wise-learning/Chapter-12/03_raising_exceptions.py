def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good - Harry") from None

a = increment('df364')
print(a)