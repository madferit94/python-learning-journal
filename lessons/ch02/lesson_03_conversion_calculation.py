# 수업 03 — 문자열을 정수로 바꿔 총금액 계산하기
# 오늘 할 것: 가격과 수량을 정수로 바꿔 곱합니다.
# 왜 하나요? 숫자처럼 보이는 문자열을 계산에 쓰려면 자료형을 확인해야 합니다.
# 파일을 실행하면 4번 풀이가 실행됩니다.

# 1. 복습 — 문자열을 정수로 바꾸기
# price_text = "25"  # 가격을 문자열로 저장합니다.
# quantity_text = "4"  # 수량을 문자열로 저장합니다.
# print(type(price_text))  # 원래 가격의 자료형을 출력합니다.
# print(type(quantity_text))  # 원래 수량의 자료형을 출력합니다.
# price = int(price_text)  # 가격을 정수로 바꿔 price에 저장합니다.
# quantity = int(quantity_text)  # 수량을 정수로 바꿔 quantity에 저장합니다.
# print(price)  # 변환한 가격을 출력합니다.
# print(quantity)  # 변환한 수량을 출력합니다.
# print(type(price))  # 변환한 가격의 자료형을 출력합니다.
# print(type(quantity))  # 변환한 수량의 자료형을 출력합니다.
# 공유한 결과: str, str, 25, 4, int, int.

# 2. 계산 — 총금액 구하기
# amount = price * quantity  # 정수 가격에 수량을 곱해 총금액을 저장합니다.
# print(amount)  # 총금액을 출력합니다.
# 실행 전 예상과 실제 출력: 100.

# 3. 확인 — 원래 값과 변환한 값 비교
# print(type(price_text))  # 원래 가격의 자료형을 출력합니다.
# print(type(price))  # 변환한 가격의 자료형을 출력합니다.
# 공유한 결과: str, int.
# 내 설명 (피드백 후 정리): int(price_text)로 변환한 정수 25는 = 왼쪽의 price에 저장됩니다. price_text에는 다시 대입하지 않았으므로 문자열 "25"가 그대로 남습니다.
# 처음에는 원래 값도 바뀐다고 답했다가, 피드백 후 그대로라고 답했습니다.

# 4. 다시 작성 — 값을 바꾸어 총금액 구하기
# 처음에는 18과 3을 출력했습니다. 안내 후 곱셈과 총금액 출력을 추가했습니다.
# 사전 예상란은 비어 있었습니다. 최종 두 실행에서 총금액 54를 확인했습니다.
price_text = "18"  # 가격을 문자열로 저장합니다.
quantity_text = "3"  # 수량을 문자열로 저장합니다.
print(type(price_text))  # 원래 가격의 자료형을 출력합니다.
print(type(quantity_text))  # 원래 수량의 자료형을 출력합니다.
price = int(price_text)  # 가격을 정수로 바꿔 price에 저장합니다.
quantity = int(quantity_text)  # 수량을 정수로 바꿔 quantity에 저장합니다.
print(price)  # 변환한 가격을 출력합니다.
print(quantity)  # 변환한 수량을 출력합니다.
print(type(price))  # 변환한 가격의 자료형을 출력합니다.
print(type(quantity))  # 변환한 수량의 자료형을 출력합니다.
amount = price * quantity  # 정수 가격에 수량을 곱해 총금액을 저장합니다.
print(amount)  # 총금액을 출력합니다.
