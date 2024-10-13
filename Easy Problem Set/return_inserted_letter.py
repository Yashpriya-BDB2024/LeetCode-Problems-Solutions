def return_inserted_letter(str1, str2):
#Problem statement: str2 is formed after reshuffling the letters of str1 & then adding an extra letter to it. So, we need to retrieve that extra one.
    if len(str1)==0 or len(str2)==0:
        return None
    elif len(str1) == len(str2):
        return False
    else:
        for char in str2:
            if str2.count(char) >  str1.count(char):
                return  char
def main():
    str1=input("Enter the first string: ")
    str2=input("Enter the second string: ")
    print(return_inserted_letter(str1,str2))
if __name__ == '__main__':
    main()
