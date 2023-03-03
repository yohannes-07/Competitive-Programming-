
test_c = int(input())

for _ in range(test_c):
    a, b = map(int, input().split())
    left, right = 0, (a + b) // 4
    

    while left <= right:
        mid = left + (right - left) // 2

        #if either a or b are less than 0.... not  enoug persons to
        #for the group so find less number of groups
        if a - mid >= 0 and b - mid >= 0:
            left_persons = a - mid  + b - mid
            # mid  = no of groups
            # after taking 1 person from a and b... mid * 2 persons are taken
            # if total taken persons > left persons...it means we don't have enough persons left
            # to form the group

            if mid * 2 <= left_persons:
                left = mid + 1
            else:
                right = mid - 1
        else:
            right = mid - 1

    print(right)
        
    
    

