def check_anagram(str1, str2):
    if len(str1) != 0 and len(str2) != 0:
        sorted_str1=sorted(str1)
        sorted_str2=sorted(str2)
    else:
        return None
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False
def main():
    str1=input("Enter the first string: ")
    str2=input("Enter the second string: ")
    result=check_anagram(str1,str2)
    print(result)
if __name__ == '__main__':
    main()