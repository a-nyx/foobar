# Level 2b
# Question:
# Given a list of digits, find the highest number that can be made with them which
# is divisible by 3. If none, return 0. 

def solution(l):
    '''
    Solution: If a number is not divisible by 3, number % 3 is equal to 1 or 2.
    If it is 1, we can remove 1 item with the remainder 1, or 2 items with the remainders 2
    If it is 2, we can remove 1 item with the remainder 2, or 2 items with the remainders 1
    Finally, just sort the numbers left descending and put them together

    rem1a, rem1b: two digits with the remainder 1. if there is not, keep it 10.
    '''
    listSum = sum(l)
    remainder = listSum % 3
    l.sort()
    if remainder != 0:
        rem1a, rem1b, rem2a, rem2b = 10, 10, 10, 10
        for i in l:
            if i % 3 == 2:
                if rem2a == 10: rem2a = i
                elif rem2b == 10: rem2b = i
                elif rem2a <= rem2b and i < rem2b: rem2b = i
                elif i < rem2a: rem2a = i
            elif i % 3 == 1:
                if rem1a == 10: rem1a = i
                elif rem1b == 10: rem1b = i
                elif rem1a <= rem1b and i < rem1b: rem1b = i
                elif i < rem1a: rem1a = i
            elif rem1a != 10 and rem1b != 10 and rem2a != 10 and rem2b != 10:
                break

        if remainder == 2:
            if rem2a != 10 or rem2b != 10:
                l.remove(min(rem2a, rem2b))
            elif rem1a != 10 and rem1b != 10:
                l.remove(rem1a)
                l.remove(rem1b)
            else:
                l = []

        if remainder == 1:
            if rem1a != 10 or rem1b != 10:
                l.remove(min(rem1a, rem1b))
            elif rem2a != 10 and rem2b != 10:
                l.remove(rem2a)
                l.remove(rem2b)
            else:
                l = []

    if not l:
        return 0
    l.reverse()
    return int("".join(map(str, l)))

# Test Cases
print(solution([5, 5, 5, 7]))           # 555
print(solution([3, 1, 4, 1]))           # 4311
print(solution([3, 1, 4, 1, 5, 9]))     # 94311
print(solution([1, 2, 1]))              # 21

