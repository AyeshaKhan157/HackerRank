if __name__ == '__main__':
    N = int(input('enter command'))
    list = []

    for _ in range(N):
        parts = input().split()
        command = parts[0]
        
        if command == 'insert':
            list.insert(int(parts[1]), int(parts[2]))
        elif command == 'print':
            print(list)
        elif command == 'remove':
            list.remove(int(parts[1]))
        elif command == 'append':
            list.append(int(parts[1]))
        elif command == 'sort':
            list.sort()
        elif command == 'pop':
            list.pop()
        elif command == 'reverse':
            list.reverse()
