def third_max_numb(arr):
    sorted_arr=sorted(set(arr), reverse=True)  #'set' built-in function removes duplicates or consider that element only once.
    if len(sorted_arr)>=3:
        return sorted_arr[2]
    else:
        return sorted_arr[0]
def main():
    #arr=[3,2,1]
    #arr=[1,2]
    arr=[2,2,3,1]
    print(third_max_numb(arr))
if __name__ == '__main__':
    main()
