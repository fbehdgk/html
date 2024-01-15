''' round 함수 : 반올림할 자리수를 지정해 숫자를 반올림 
round(숫자, 소수점 밑 자리수)
실수를 입력받아 제곱해 출력
소수점 밑 첫째자리까지 출력(소수점 밑 둘째자리에서 반올림)'''
#num = float(input('실수를 입력:'))

#print(round(num,1))

#print('-----')
   # round 함수 : 반올림할 자리수를 지정해 숫자를 반올림
        # round(숫자, 소수점 밑 자리수)

        # 실수를 입력받아 제곱해 출력
        # 소수점 밑 첫째자리까지 출력(소수점 밑 둘째자리에서 반올림)
#num = float(input('실수를 입력:'))

#print(round(num*num,1))
#print('-----')
#        1~100사이의 랜덤한 정수를 출력하시오
'''
import random
print(int(random.random()*100+1))

string = '동서남북동서남북동서남북'
print(string[0]*4)
print(string[0::2])
print(string[0:4])
 # 문자열이나 리스트 슬라이싱 방법 [시작위치:끝위치:step]이다

        # 시작위치와 끝위치를 생략하면 문자열 전체가 대상이 된다
        # 순서대로 접근 :  0   1   2   3
        # 거꾸로 접근 :    -4 -3  -2  -1 
        #                 동  서  남  북 
        
        # string 문자열을 거꾸로 출력
        # string 문자열에서 '북서'를 출력(거꾸로 출력한다)
        # string 문자열에서 '남동'를 출력(거꾸로 출력한다)
string = '동서남북'
print(string[-4::])
print(string[-1::-2])
print(string[-2::-2])
        # 전화번호를 '010.1234.5678'과 같은 형식으로 출력

phone = '010-1234-5678'
new_phone = phone.replace('-','.')
print(new_phone)
        # 정수를 입력받아 짝수인지 홀수인지 출력하시오
        # 정수를 입력하지 않은 경우 예외처리하시오
num = int(input('정수를 입력하시오'))
if num %2 == 0:
    print('짝수')
elif num % 2 == 1:
    print('홀수')
else:print('정수를 입력하시오')
        # 년도를 입력받아 그 해에 월드컵이 열리는지 또는 올림픽이 열리는 지 아니면 월드컵도 올림픽도 열리지 않는지 출력
        # 잘못된 입력에 대해 예외처리하시이
try:
    year = int(input('년도를 입력 : '))
    if year%4==2:
        print('월드컵이 열리는 해입니다')
    elif year%4==0:
        print('하계 올림픽이 열리는 해입니다')
    else:
        print('월드컵도 올림픽도 열리지 않는 해입니다')
except:
    print('년도를 정확하게 입력하세요') 
      
# 4의 배수면 윤년이다. 단 100의 배수이면 윤년이 아니다
# 윤년여부를 출력
year = int(input('년도를 입력 : '))
윤년 = year%4==0 != year%100
if 윤년 == True:
    print('윤년이다')
else:print('윤년이아니다')
#년도를 입력받아 다음 올림픽이 열리는 해를 출력
year = int(input('년도를 입력 : '))
if year%4==0:
    print(f'올해{year}년에 열립니다')
elif year%4==1:
    print(f'3년후인{year+3}년에 열립니다')
elif year%4==2:
    print(f'2년후인{year+2}년에 열립니다')
elif year%4==3:
    print(f'1년후인{year+1}년에 열립니다')
        # 년도를 입력받아 다음 윤년을 출력
        # 2020입력 : 다음 윤년은 2000년입니다
        # 2021입력 : 다음 윤년은 2024년입니다
year = int(input('연도를 입력 : '))
if year%4==0:
    print(f'올해{year}년이 윤년입니다')
elif year%4==1:
    print(f'3년후인{year+3}년이 윤년입니다')
elif year%4==2:
    print(f'2년후인{year+2}년이 윤년입니다')
elif year%4==3:
    print(f'1년후인{year+1}년이 윤년입니다')
      # 1~12까지 달을 입력받아서, 입력받은 달은 몇 일까지 있는지 출력하는 코드를 작성(윤년은 고려하지 않음)
        # 2월: 28일
        # 4월, 6월, 9월, 11월: 30일
        # 1월, 3월, 5월, 7월, 8월, 10월, 12월: 31일   
year = int(input('월을 입력 : '))
if year== 2:
    print(f'{year}월은 28일까지 있습니다')
elif year== (4 or 6 or 9 or 11):
    print(f'{year}월은 30일까지 있습니다')
elif year== (1 or 3 or 5 or 7 or 8 or 10 or 12):
    print(f'{year}월은 31일까지 있습니다')
# 사각형의 너비와 높이를 입력받아 면적을 출력하는 함수
        # 너비와 높이는 실수로 처리
        # 면적은 round 함수를 이용해 소수점 첫째자리까지 출력
width = float(input('너비 입력 : '))
hight = float(input('높이 입력 : '))
sqear= width * hight
print(f'{round(sqear,1)}제곱미터입니다')
        # 학생들의 이름과 나이가 적힌 명단이 있다. 이 명단을 파이썬 타입으로 표현하고 출력하시오
        #  이름     나이
        #  우진     19
        #  시은     20
        # 제임스    19
명단 = {'우진':19, '시은':20, '제임스':19}
print(명단)
 # 다음 리스트에서 중복된 데이터를 제거하고 출력하시오
number_list = [1, 2, 1, 1, 2, 3, 4, 1, 5, 2, 1, 5]
number_list = set(number_list)      
print(number_list)
     # 아래와 같은 내용을 저장하는 파이썬 변수 s로 만드시오
        # 사는 곳 : 서울
        # 성별 : 여자
        # 이름 : 시은

        # 나이와 혈액형을 입력받아 저장 후 출력하시오
s = {'사는곳':'서울', '성별':'여자', '이름':'시은'}
nai = int(input('나이를 입력하시오:'))
s['나이'] = nai
b_type = input('혈액형 입력하시오:')
s['혈액형'] = b_type
print(s)
'''
        # 상품의 이름을 입력하면 가격을 알려주는 코드를 작성
        # 단, 없는 상품을 입력하면 오류 메시지 출력
상품들 = {'칙촉':1000,'가나':1700,'포스틱':1500,'홈런볼':1400,'오징어땅콩':1200}
print(상품들)
상품명 = input('상품명 입력')
상태 = 'n'
for 상품 in 상품들:
    b = 상품==상품명
    if b == True:
        print(f'{상품명}는 {상품들[상품명]}원 입니다') 
        상태 = 'y'
if 상태 == 'n':
    print('그런거없다')
'''
# 급여를 인자로 받아 소득세, 국민연금, 건강보험를 제외한 실수령액을 계산하는 함수를 정의하고 호출
# 소득세율은 3.3%, 국민연금은 4.5%, 건강보험은 3.5%로 한다
# 소수점 이하 금액은 절사한다
salary = int(input('급여입력:')) 
소득세율= 3.3
국민연금= 4.5
건강보험= 3.5 
real_salary = (salary-((소득세율+국민연금+건강보험)*(salary/100)))
real_salary = int(round(real_salary,0))
print(f'{real_salary}원입니다')
# 두 숫자를 인자로 받아 큰수를 리턴하는 함수를 정의하고 호출
num1 = int(input('숫자1입력:'))
num2 = int(input('숫자2입력:'))
if num1 > num2:
    print(num1)
elif num1 < num2:
    print(num2)
else:print('같다')
 # 세 숫자를 인자로 받아 큰수를 리턴하는 함수를 정의하고 호출
def large(param1, param2, param3):
# 제일 큰 수를 param1이라고 가정
    large = param1
# param2, param3 차례대로 현재 최대값인 large와 비교
    if param2>large:
       large = param2
    if param3>large:
        large = param3
        return large
print(large(10, 300, 20))    
        # bmi 지수를 계산하는 함수를 작성
        # bmi는 체중 / 키의제곱인데 이때 키는 m단위이다(175cm이면 1.75)
        # 체중은 kg 단위, 키는 cm 단위로 전달받는다
        # bmi는 소수점 첫째자리까지 
kg = int(input('kg입력:'))
cm = (int(input('cm입력:')))/100
bmi = kg/(cm*cm)
print(round(bmi,1))
   # 리스트를 인자로 받아 합계를 리턴하는 함수를 정의하고 호출
my_list=[1,2,3]
sum_list = sum(my_list)
print(sum_list)
# 리스트를 인자로 받아 최대값을 리턴하는 함수를 정의하고 호출
my_list=[1,2,3]
max_list = max(my_list)
print(max_list)
#모범답안:
def get_max(list_param):
    max = 0
    for value in list_param:
        if value>max:
            max = value
        return max

print(get_max([1,2,3,4,5]))

    # 문자열 리스트을 입력받아 가장 긴 문자열의 길이를 리턴하는 함수
my_list=['1','12','123','1234','12345','123456']
max_len = 0
for value in my_list:
    if len(value)>max_len:
        max_len = len(value)
print(max_len)
max_len = int(max_len)'''
# 문자열 리스트을 입력받아 가장 긴 문자열을 리턴

def get_longest_string(list_param):
    max = 0
    result=''
    for string in list_param:
        if len(string)>max:
            max = len(string)
            result = string
    return result

print(get_longest_string(['hello', 'hello python', 'java']))