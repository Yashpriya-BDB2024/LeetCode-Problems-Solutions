#Problem statement: Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j].
# If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content.
# Your goal is to maximize the number of your content children and output the maximum number.

def assign_cookies(s, g):
    i=0
    j=0
    content_children=0
    while i<len(g) and j<len(s):
        if s[j] >= g[i]:
            content_children+=1
            i+=1
        j+=1
    return content_children
def main():
    s=[1,1] #cookies size
    g=[1,2,3] #greed factor of 3 childs

    #s=[1,2,3]
    #g=[1,2]
    print(assign_cookies(s,g))
if __name__ == '__main__':
    main()