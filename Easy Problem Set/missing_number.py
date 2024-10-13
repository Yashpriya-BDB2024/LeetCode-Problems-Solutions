def find_missing_number(arr, arr1):
#arr=original array(no missing element)
#arr1=given array(an element is missing)
    sum=0
    sum1=0
    for i in arr:
        sum=i+sum
    for j in arr1:
        sum1=j+sum1
#Missing no. = sum of all the elements in original array - sum of all the elements in the given array
    missing_num=sum-sum1
    return missing_num
def main():
    #n=3; range=[0,3] - since, range = [0, n]
    #arr=[3,0,1,2] #original
    #arr1=[3,0,1] #given

    #n=2; range=[0,2]
    #arr=[0,1,2]
    #arr1=[0,1]

    #n=9; range=[0,9]
    arr=[9,8,6,7,2,3,5,4,1,0]
    arr1=[9,6,4,2,3,5,7,0,1]

    result=find_missing_number(arr,arr1)
    print(result)
if __name__ == '__main__':
    main()