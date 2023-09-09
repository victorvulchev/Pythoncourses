numb = int(input())
down_palindrome = numb
up_palindrome = numb
reverse_numb = str(numb)[::-1]

if str(numb) == reverse_numb:
    print(numb)
else:
    while(True):
        down_palindrome -= 1
        up_palindrome += 1
        reverse_down = str(down_palindrome)[::-1]
        reverse_up = str(up_palindrome)[::-1]
        if str(down_palindrome) == reverse_down:
            print(down_palindrome)
            break
        if str(up_palindrome) == reverse_up:
            print(up_palindrome)
            break
        