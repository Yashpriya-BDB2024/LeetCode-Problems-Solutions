def check_duplicate_presence(arr):
    for i in arr:
        if arr.count(i)==2:
            return True
            break
        else:
            return False
def main():
    arr=[1,2,3,1]
    #arr=[1,2,3,4]
    result=check_duplicate_presence(arr)
    print(result)
if __name__ == '__main__':
    main()