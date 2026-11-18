# 수업 04 — 교재 2장 핵심 복습
# 파일을 실행하면 1~3회차의 결과가 순서대로 나옵니다.

# 1회차. 형 변환과 곱셈
price_text = "35"  # 가격을 문자열로 저장합니다.
quantity_text = "6"  # 수량을 문자열로 저장합니다.

price_number = int(price_text)  # 가격 문자열을 정수로 바꿉니다.
quantity_number = int(quantity_text)  # 수량 문자열을 정수로 바꿉니다.

print(price_number)  # 변환한 가격을 출력합니다.
print(quantity_number)  # 변환한 수량을 출력합니다.

amount = price_number * quantity_number  # 정수 가격과 수량을 곱해 총금액을 저장합니다.
print(amount)  # 총금액을 출력합니다.

# 공유한 실행 결과
# 35
# 6
# 210


# 2회차. 조건문
price = 35  # 가격을 35로 정합니다.
quantity = 0  # 수량이 0인 경우를 확인합니다.

if quantity <= 0:  # 수량이 0 이하인지 확인합니다.
    print("수량 확인 필요")  # 조건이 참이면 확인 메시지를 출력합니다.
else:  # 수량이 양수일 때 아래 코드를 실행합니다.
    amount = price * quantity  # 가격과 수량을 곱해 총금액을 저장합니다.
    print(amount)  # 총금액을 출력합니다.

# 공유한 실행 결과
# 수량 확인 필요
# 수량을 3으로 바꾼 별도 실행에서는 105가 나왔습니다.


# 3회차. 반복문
price = 35  # 모든 계산에 같은 가격 35를 씁니다.
quantities = [2, 5, 8]  # 계산할 수량을 리스트로 모읍니다.

for quantity in quantities:  # 리스트에서 수량을 하나씩 꺼냅니다.
    amount = price * quantity  # 이번 수량에 가격을 곱합니다.
    print(amount)  # 반복할 때마다 총금액을 한 줄씩 출력합니다.

# 공유한 실행 결과
# 70
# 175
# 280

# 민섭님 설명을 정리한 내용
# 가격 35는 그대로이고, quantities에서 꺼낸 값이 quantity에
# 2, 5, 8 순서로 들어갑니다.
# 반복문 안에서 매번 곱하고 출력해서 70, 175, 280이 한 줄씩 나옵니다.
