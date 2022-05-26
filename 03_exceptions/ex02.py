l = [1,2,3,4,5]

for i in range(6):
    try:
        print(f"l[{i}] = {l[i]}")
    except Exception:
        print("Something went wrong")

print("Program ended correctly")