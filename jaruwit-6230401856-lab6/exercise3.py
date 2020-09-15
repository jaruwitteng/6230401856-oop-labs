user_input = input("Enter a filename:").lower()
with open(user_input, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.read()
    print(lines)
    f.close()

