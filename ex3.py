
def solution(arr, target):
    dic = {}
    for i in arr:
        y = 10 - i
        if y in dic:
            return (y,i)
        else:
            dic[i] = True

def main():
    res = solution([-4,-1,1,3,5,6,8,11], 10)
    print(res)


if __name__ == '__main__':
    main()