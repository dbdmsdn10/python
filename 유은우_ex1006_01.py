#input()함수
# c= input("인사말 함수를 입력하시오")
# print(c)

# num_a=int(input("숫자를 입력하시오> "))
# num_b=1000
# print(num_a+num_b)
#단 소수점을 int로 바꾸려 하면 오류가 생김

# output_a=str(52)
# output_b=str(52.273)
# print(type(output_a),output_a)
# print(type(output_b),output_b)

# string_a="{}만원".format(10)
# format_c="{} {} {}".format(3000, 4000, 5000)
# print(type(string_a),string_a)
# print(format_c)

# output_b="{:5d}".format(52) #앞에5개 빈칸
# output_d="{:10d}".format(52) #앞에10개 빈칸

# output_e="{:05d}".format(52) #앞에 00 보이게 하기
# output_f="{:010d}".format(-52) #앞에 00 보이게 하기

# print(output_b)
# print(output_d)
# print(output_e)
# print(output_f)

# output_e="{:+d}".format(52)#숫자 기호 보이게 하기
# output_f="{:+d}".format(-52)#숫자 기호 보이게 하기

# print(output_e)
# print(output_f)


# a="{:.3f}".format(52.621314328)
# b="{:g}".format(52.20000000)
# print(a)
# print(b)
# a="12345abc"
# b="%12345abc"
# c="12345"

# print(a.isalnum()) #알파뱃 또는 숫자인가
# print(b.isalnum())
# print(c.isdecimal()) #정수인가 확인


# aaa="선문의 자랑 해달이"
# print(aaa.find("선문"))

# print("선문" in "선문대학교")

# a="a,b,c,d,e"
# b=a.split(",")
# print(b)

# print(not True)

# x=10
# b=x<20
# print(b)

# if조건문

# x=10
# y=20
# z=0
# if(x<y):
#     print("수업을 그만할게요")
#     print("2")
#     z=x+y
# print("3")
# print("z=",z)

# a=int(input("정수입력"))
# if(a>0):
#     print("양수이다")
# if(a==0):
#     print("0이다")
# if(a<0):
#     print("음수이다")

#날짜 시간 활용하기
import datetime
now=datetime.datetime.now()
# print(now)

# print(now.year,"년")
# print(now.month,"월")
# print(now.day,"일")
# print(now.hour,"시")
# print(now.minute,"분")
# print(now.second,"초")

# if(now.hour<12):
#     print("{}시이니 오전입니다".format(now.hour))
    
# if(now.hour>12):
#     print("{}시이니 오후입니다".format(now.hour))

#계절 비교
# import datetime
# bbb=datetime.datetime.now()
# if(3<=bbb.month<=5):
#     print("{}월은 봄입니다".format(bbb.month))
# if(6<=bbb.month<=8):
#     print("{}월은 여름입니다".format(bbb.month))
# if(9<=bbb.month<=10):
#     print("{}월은 가을입니다".format(bbb.month))
# if(11<=bbb.month and bbb.month<=2):
#     print("{}월은 겨울입니다".format(bbb.month))

# if(now.hour<12):
#     print("{}시이니 오전입니다".format(now.hour))
# else:
#     print("{}시이니 오후입니다".format(now.hour))

# num=int(input("정수입력\n"))
# if(num%2==0):
#     print("짝수이다")
# if(num%2==1):
#     print("홀수이다")

import datetime
bbb=datetime.datetime.now()
if(3<=bbb.month<=5):
    print("{}월은 봄입니다".format(bbb.month))
elif(6<=bbb.month<=8):
    print("{}월은 여름입니다".format(bbb.month))
elif(9<=bbb.month<=10):
    print("{}월은 가을입니다".format(bbb.month))
elif(11<=bbb.month and bbb.month<=2):
    print("{}월은 겨울입니다".format(bbb.month))