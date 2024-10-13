def majority_element(arr):
    max_count=0
    max_elem=arr[0]
    for num in arr:
        count=arr.count(num)
        if count>max_count:
            max_count=count
            max_elem=num
#To check if the max_elem is actually the majority element, as it will cover approx. half of the array length.
    if max_count==len(arr)//2:
        return max_elem
    else:
        return None

def main():
    arr=[2,1,1,1,1,3,3,2,2]
    result=majority_element(arr)
    print(result)
if __name__ == '__main__':
    main()