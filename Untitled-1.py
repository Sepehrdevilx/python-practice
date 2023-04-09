def is_leap(year):
    
    
    if year <=1900 & year >= 100000:
        print("wront input!")
    elif year % 100 == 0 & year% 400 == 0:
        return True
    elif year % 4 == 0 & year % 100 ==0:
        return False
    elif year % 4 == 0:
        return True

    else: return False

year = int(input())
print(is_leap(year))