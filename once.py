# once
def main():
    pass
    inp=input()
    n=list(map(int,input().split()))
    list_1=[]
    for num in n:
        count=n.count(num)
        if (count>1):
            list_1.append(num)
        else:
            print(num,end=" ")

if __name__ == '__main__':
    main()
