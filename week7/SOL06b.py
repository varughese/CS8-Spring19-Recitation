# function to check string is
# palindrome or not


def isPalindrome(word):
    # Run loop from 0 to len/2
    for i in range(0, len(word) // 2):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True


# main function
while True:
    s = input("Give word or exit:")
    ans = isPalindrome(s)
    if s == "exit":
        break
    if ans:
        print("Yes")
    else:
        print("No")
