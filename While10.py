def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    sum1=0
    i=0
    while i<len(s):
        if s[i].isdigit():
            if int(s[i])%2==1:
                sum1+=int(s[i])
        i+=1
    return sum1
print(main('19mixuai7172783'))