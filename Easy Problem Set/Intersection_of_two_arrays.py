def intersection(arr1, arr2):
    intersected_elements = []
    for i in arr1:
        for j in arr2:
            if i not in intersected_elements:  #It will take care of the duplicates, if the intersected_elements list is empty, then only it will append.
                if i == j: #If an element of one array intersects with the element of another array, then, that's the intersection point.
                    intersected_elements.append(i)
    return intersected_elements
def main():
    arr1=[1,2,2,1]
    arr2=[2,2]

    arr1=[9,4,9,8,4]
    arr2=[9,4,5]

    result=intersection(arr1,arr2)
    print(result)
if __name__ == '__main__':
    main()

