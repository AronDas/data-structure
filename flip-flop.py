def palindrome(r):
    end = len(r) - 1
    start = 0
    while (start<end):
        if (r[start]!=r[end]):
            return False
        start+=1
        end-=1
    return True
r = (1, 2, 3, 3, 7, 1)

if palindrome(r):
    print("The tuple is flip-flop")
else:
    print("The tuple is not flip-flop")
