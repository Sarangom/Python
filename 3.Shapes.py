# Read number of test cases
t = int(input().strip())

for _ in range(t):
    # Read rows and columns
    n, m = map(int, input().split())
    
    # Read the matrix
    matrix = []
    for _ in range(n):
        row = input().strip()
        matrix.append(row)
    
    max_border = 0
    
    # Check rows
    for i in range(n):
        count = 0
        for j in range(m):
            if matrix[i][j] == '#':
                count += 1
                if count > max_border:
                    max_border = count
            else:
                count = 0
    
    # Check columns
    for j in range(m):
        count = 0
        for i in range(n):
            if matrix[i][j] == '#':
                count += 1
                if count > max_border:
                    max_border = count
            else:
                count = 0
    
    print(max_border)
