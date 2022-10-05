'''
키와 몸무게를 입력받아서 비만도를 측정하는 프로그램을 완성하시오.
BMI 지수를 구하는 공식은 다음과 같다.
BMI지수 = 몸무게(70kg) / (키(1.7m) * 키(1.7m))

BMI 지수에 따른 결과는 다음과 같다.
고도 비만 : 35 이상
중(重)도 비만 (2단계 비만) : 30 - 34.9
경도 비만 (1단계 비만) : 25 - 29.9
과체중 : 23 - 24.9
정상 : 18.5 - 22.9
저체중 : 18.5 미만

이름, 키, 몸무게를 입력받으면 다음과 같이 출력되도록 하시오.

***************************
이름 키(cm) 몸무게(kg) 비만도
***************************
홍길동 170 79 정상
***************************
'''

"""비만도 계산"""
class Solution:
    def solution(self, name, cm, kg):
        title = " ### 비만도 계산 ### "
        aster = "*"*30
        schema = "이름 키(cm) 몸무게(kg) 비만도"
        m = cm / 100
        bmi = kg / (m*m)
        if bmi >= 35:
            biman = "고도 비만"
        elif bmi >= 30:
            biman = "중(重)도 비만 (2단계 비만)"
        elif bmi >= 25:
            biman = "경도 비만 (1단계 비만)"
        elif bmi >= 23:
            biman = "과체중"
        elif bmi >= 18.5:
            biman = "정상"
        else:
            biman = "저체중"        
        values = f'{name} {cm} {kg} {biman}'
        return f"{aster} \n {title} \n {aster} \n {schema} \n {aster} \n {values} \n {aster}"

if __name__=="__main__":
    solution = Solution()
    name = input("이름을 입력하세요 : ")
    cm = int(input("키를 입력하세요 : "))
    kg = int(input("체중을 입력하세요 : "))
    print(solution.solution(name, cm, kg))