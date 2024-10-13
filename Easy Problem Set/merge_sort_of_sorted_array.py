def merge_arrays(nums1, nums2):
    result = []
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        elif nums2[j] < nums1[i]:
            result.append(nums2[j])
            j += 1
#If both elements are same -
        else:
            result.append(nums2[j])
            result.append(nums1[i])
            i += 1
            j += 1
    # append remaining elements from both.
    while i < len(nums1):
        result.append(nums1[i])
        i += 1
    while j < len(nums2):
        result.append(nums2[j])
        j += 1
    return result

def main():
    #nums1=[0]
    #nums2=[1]

    nums1=[1,2,3]
    nums2=[2,5,6]

    #nums1=[]
    #nums2=[1]

    result = merge_arrays(nums1, nums2)
    print(result)
if __name__ == "__main__":
    main()