def print_rangoli(size):
    # code
    rangoli=[]
    for i in range(size,0,-1):
        row_letters=[] 

        for j in range(size,i-1,-1):
            row_letters.append(chr((j-1)+97))

        if len(row_letters)>1:
            row_letters=row_letters+row_letters[-2::-1]
            
        rangoli.append(("-".join(row_letters).center((2*(2*size-1)-1),'-')))

    fullrangoli=rangoli+rangoli[-2::-1]
    for b in fullrangoli:
        print(b)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)