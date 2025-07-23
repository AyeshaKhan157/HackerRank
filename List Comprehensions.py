if __name__ == '__main__':
    x = int(input("Enter Number"))
    y = int(input("Enter Number"))
    z = int(input("Enter Number"))
    n = int(input("Enter Number"))
    result = [[i,j,k]
        for i in range(x+1)
        for j in range(y+1)
        for k in range(z+1)
        if i + j + k != n
    ]
    print(result)
