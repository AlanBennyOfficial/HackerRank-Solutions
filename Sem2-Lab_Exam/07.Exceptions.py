# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

for _ in range(n):
    a,b = input().split()

    try:
        a,b = int(a),int(b)
        print(a//b)

    except Exception as e:
        print("Error Code:",e)
