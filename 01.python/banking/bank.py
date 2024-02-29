# 뱅킹 시스템 모듈 만들기
# 계좌를 관리하는 클래스
class Account:
    def __init__(self, owner, accNo, balance):   # 멤버변수를 초기화하기 위한 생성자
        self.owner = owner
        self.accNo = accNo
        self.balance = balance

    # 잔고조회
    def getBalance(self):
        return self.balance

    # 입금
    def deposit(self, amount):
        self.balance += amount

    # 계좌 정보 조회
    def showAccountInfo(self):
        return f'계좌주: {self.owner}, 계좌번호: {self.accNo}, 잔고: {self.balance}'

    # 출금
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise InvalidTransactionException('출금 잔고가 부족합니다.')  

    # 이체 (내 계좌는 출금, 상대 계좌는 입금)
    def transfer(self, amount, target):
        if self.balance >= amount:
            self.balance -= amount
            target.deposit(amount)
        else:
            raise InvalidTransactionException('이체 잔고가 부족합니다.')

    # 계좌번호 조회
    def getAccNo(self):
        return self.accNo

# Banking System의 업무관리 로직 클래스
# 계좌 등록, 계좌 검색, 등록된 전체 계좌 목록 조회
import random
import pickle, os

class BankManager:
    def __init__(self):
        self.account_list = []    # 뱅크 매니저 객체 생성시 내부적으로 빈 리스트가 하나 만들어짐
        self.accNo_list = []   # 생성된 계좌번호 저장 리스트

    # 계좌번호 자동 생성
    # 계좌번호 형식 : xxx-xxx  -> xxx:100~999 사이의 값
    def genAccNo(self):
        while True:
            n1 = random.randint(100, 999)
            n2 = random.randint(100, 999)
            accNo = str(n1)+'-'+str(n2)
            if accNo not in self.accNo_list:
                self.accNo_list.append(accNo)
                return accNo   # 함수이기 때문에 return으로 함수 실행 중지 가능

    # 신규 계좌 등록
    def addAccount(self, a):      # 등록할 계좌 받기
        self.account_list.append(a)

    # 계좌 검색
    def searchAccount(self, accNo):  # 검색할 계좌번호
        result = None   # 검색된 Account 객체를 할당
        for a in self.account_list:    # 계좌 번호 리스트에 있는 항목 검색
            if a.getAccNo() == accNo:  # 조회한 번호가 검색한 계좌번호와 같다면
                result = a
                break
        return result

    # 등록된 모든 계좌 정보를 반환
    def getAllAccountList(self):
        return self.account_list

    # 데이터 저장
    def saveData(self):
        with open('data.dat', 'wb') as f:
            pickle.dump(self.account_list, f)  # (저장하고자 하는 객체, 파일객체), 파일에 리스트의 모든 객체를 기록

    # 데이터 읽기
    def readData(self):
        if os.path.exists('data.dat'):
            with open('data.dat', 'rb') as f:
                self.account_list = pickle.load(f)   # 파일을 읽고 객체를 반환, ;그것을 계좌 리스트에 넣기
        
# 비정상적 거래가 발생됐을 때 사용할 사용자 정의 예외
class InvalidTransactionException(Exception):
    def __init__(self, message):
        super().__init__(message)   # 부모 클래스에서 멤버변수 초기화
        self.message = message

    def __str__(self):
        return '[Invalid Transaction Exception]'+self.message

