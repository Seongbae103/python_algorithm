'''
* 금액을 입력받은 후 우리나라 화폐종류별로 해당 갯수를 표기하는 프로그램
* [요구사항] 금융업을 하는 고객사로부터 프로그램 개발요청이 들어왔습니다.
* 금액을 입력받은 후 우리나라 화폐종류별로 해당 갯수를 표기하는 프로그램입니다.
* 예를들어, 125,520 원을 입력하면 화면에 이렇게 보이게 하면 됩니다.
* 표시하고 10원미만은 절삭
      ******************************************************
         요청금액 : 126520 원
         5만원 : 2매
         1만원 : 2매
         5천원 : 1매
         1천원 : 1매
         5백원 : 1개
         백원 : 0개
         오십원 : 0개
         십원 : 2개
      ********************************************************
'''

class Solution:
   def solution(self, money):
      title = " ### 화폐교환 ### "
      aster = "*" * 30
      answer = f'요청금액 : {money}원'
      unit = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
      for i in unit:
         print(i)
      a = int(money / unit[0])
      b = int(money % unit[0] / unit[1])
      c = int(money % unit[1] / unit[2])
      d = int(money % unit[2] / unit[3])
      e = int(money % unit[3] / unit[4])
      f = int(money % unit[4] / unit[5])
      g = int(money % unit[5] / unit[6])
      h = int(money % unit[6] / unit[7])

      return f' {title} \n {aster} \n {answer} \n 5만원 : {a}매 \n 1만원 : {b}매 \n 5천원 : {c} \n 1천원 : {d}매 \n 5백원 : {e}매 \n 백원 : {f}매 \n 오십원 : {g}매 \n 십원 : {h}매'
      
if __name__=="__main__":
   solution = Solution()
   money = int(input( " 요청금액 : "))
   print(solution.solution(money))