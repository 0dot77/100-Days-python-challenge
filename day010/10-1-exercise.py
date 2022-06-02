# Days in Month Exercise

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False



def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month"
    # 1. year로 들어오는 값은 bool값 True일 때 윤년
    # 2. False일 때 윤년이 아니다.
        # 윤년일 때 2월의 값은 29   
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    leap_year = is_leap(year)
    """ else를 사용할 때
    if leap_year:
        month_days[1] = 29
        return month_days[month-1]
    else:
        return month_days[month-1]
    """
    # else를 사용하지 않아도 return을 만나면 함수가 끝난다는 것을 이용할 수 있다.
    if leap_year:
        month_days[1] = 29
        return month_days[month-1]
    return month_days[month-1]


#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

