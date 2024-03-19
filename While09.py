def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    sum1=0
    i=0
    while i<len(s):
        if s[i].isdigit():
                sum1+=int(s[i])
        i+=1
    return sum1
print(main('19ghj,2'))