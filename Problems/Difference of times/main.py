a_hour = int(input())
a_minute = int(input())
a_second = int(input())

b_hour = int(input())
b_minute = int(input())
b_second = int(input())

seconds = (b_second - a_second) + ((b_minute - a_minute) * 60) + ((b_hour - a_hour) * 3600)
print(seconds)
