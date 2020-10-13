## false로 변환되는값 0은 fasle 은 true
# print("if 조건문에 0넣기")
# if True:{
#     print("0은 true입니다")
#     }
# else:{
#     print("0은 false인가")
#     }
# #0과 false 빼고는 전부 true


# ##pass키워드 이해하기
# zero=0
# a=4
# b=3
# c=0
# if zero==0:
#     pass


# aaa=[273,32,103,"문자열",True,False]

# print(aaa,"입니다")
# print(type(aaa[0]),"입니다")
# print(aaa[1:4],"입니다")
# print(aaa[-1],"입니다")

#list 연산자 +-*
# list_a=[1,2,3]
# list_b=[10,20,30]

# print("list_a=",list_a)
# print("list_b=",list_b)
# print("list_a+list_b=",list_a*3)

#list에 요소추가

list_c=[4,5,6]
list_c.append(4444)
list_c.append(5555)
list_c.append("선문대")
list_c.insert(0,1)

# print(list_c)

# del list_c[0]
# print(list_c)

# # list_c.remove("선문대")
# # print(list_c)

# # list_c.clear()
# # print(list_c)

# print("선문대" in list_c)

# for i in range(10):
#     print("{}".format(i))

# for element in list_c:
#     print(element)
# count=0
# for aa in list_c:
#     count=count+1
#     print("count=",count,"list_c=",aa)

#dictionary 실습
dict_a={
    "name" : "선문대",
    "type" : "교육기관",
    "rank" : "1",
    "list" : [1,2,3,4,5,6]
}

# print(dict_a["list"][0])

# dict_a["추가내용"]=200
# print(dict_a)

# del dict_a["list"]
# print(dict_a)

key=input("아이디를 입력하시오")
if key in dict_a["list"]:
    print("id 있음")
else:
    print("id없음")