def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    k=0
    m=0
    i=0
    while i<len(s):
        if s[i].isdigit():
             k+=1
        if s[i].isalpha():
            m+=1
        i+=1
    return len(s)-(k+m)
print(main('sal om%%10'))