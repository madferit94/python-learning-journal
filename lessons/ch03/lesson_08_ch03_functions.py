# 수업 08 — 주문 금액을 함수로 계산하기
# 실행하면 1~4번 결과가 차례로 나옵니다. 한 문제만 보려면 해당 코드 블록을 따로 실행하세요.

# def는 계산 방법을 정합니다. 주문 A를 order_amount(orders)에 넣을 때 비로소 함수 안에서 40 × 3을 계산합니다.
# return은 답을 코드로 돌려줍니다. amounts = order_amount(order)에서 금액을 amounts에 저장해서 append()에 넘길 수 있습니다. print()는 입력받은 값을 화면에 보여줍니다.
# if problem == 4:는 제가 넣은 실행 선택용 코드였습니다. problem = 4는 값을 저장하고 == 4는 그 값이 4인지 확인합니다. 민섭님이 작성한 마지막 코드에서 조건에 속한 줄은 print(problem) 하나였고, 주문 계산은 바깥에 있었습니다. 정리본에서는 이 선택 줄을 빼고 각 문제 코드를 따로 복사해 실행할 수 있게 했습니다.

# 문제 1 — 단가 꺼내 리스트에 한 번 넣기
orders = {"name": "A", "price":40, "quantity": 3}  # 주문 A의 정보를 저장합니다.
print(orders["price"])  # 주문에서 꺼낸 단가를 출력합니다.
selected_order = []  # 꺼낸 값을 넣을 빈 리스트를 만듭니다.
selected_order.append(orders["price"])  # 단가 하나를 리스트 끝에 추가합니다.
print(selected_order)  # 가격을 담은 리스트를 출력합니다.

# 40
# [40]
# 처음에는 딕셔너리를 반복해서 같은 40을 세 번 넣었습니다. 딕셔너리를 그대로 반복하면 키 세 개가 나오므로, for를 빼고 append()를 한 번만 실행했습니다. append() 다음 줄에서 리스트를 출력했습니다.


# 문제 2 — 주문 한 건의 금액을 함수로 구하기
orders = {"name": "A", "price":40, "quantity": 3}  # 주문 A의 정보를 저장합니다.
def order_amount(order_amount):  # 주문 한 건을 받는 함수를 정의합니다.
    return order_amount["price"] * order_amount["quantity"]  # 단가와 수량을 곱한 값을 돌려줍니다.
print(order_amount(orders))  # 주문을 함수에 넣고 돌려받은 금액을 출력합니다.

# 120
# def는 함수 정의를 시작하는 문장이라 = def처럼 값 자리에 쓸 수 없습니다. 정의 아래에서 함수를 호출하고, print()는 return 뒤의 함수 본문 밖에 뒀습니다. 함수와 받는 값에 같은 이름을 써도 제출한 코드는 실행됐습니다. 읽을 때는 괄호 앞이 함수 이름, 괄호 안이 주문을 받는 이름입니다.


# 문제 3 — 여러 주문에 같은 함수 쓰기
def order_amount(order_amount):  # 주문 한 건을 받는 함수를 정의합니다.
    return order_amount["price"] * order_amount["quantity"]  # 단가와 수량을 곱한 값을 돌려줍니다.
orders = [{"name":"A" ,"price":40, "quantity":3},  # 주문 세 건을 리스트에 담습니다.
         {"name":"B", "price":25, "quantity":8},  # 주문 한 건의 정보입니다.
         {"name":"C", "price":30, "quantity":2}]  # 주문 한 건의 정보입니다.
selected_amounts = []  # 주문 금액을 모을 빈 리스트를 만듭니다.
for order in orders:  # 주문을 한 건씩 꺼냅니다.
    amounts = order_amount(order)  # 함수가 돌려준 주문 금액을 저장합니다.
    selected_amounts.append(amounts)  # 이번 주문 금액 하나를 리스트에 넣습니다.
print(selected_amounts)  # 반복이 끝나고 완성된 금액 리스트를 출력합니다.
print(sum(selected_amounts))  # 리스트의 모든 금액을 더해 출력합니다.

# [120, 200, 60]
# 380
# order_amount 정의를 주석으로 꺼 둔 채 호출해 NameError가 실제로 났습니다. 이 문제 안에서 먼저 함수를 정의한 뒤 for 안에서 불렀습니다. 처음 만든 딕셔너리 하나에 키를 반복하면 마지막 값만 남아서, 주문을 딕셔너리 세 개로 나눠 리스트에 담았습니다.


# 문제 4 — C 수량을 바꾸고 전후 비교하기
orders = [{"name":"A", "price":40, "quantity":3},  # 주문 세 건을 리스트에 담습니다.
          {"name":"B", "price":25, "quantity":8},  # 주문 한 건의 정보입니다.
          {"name":"C", "price":30, "quantity":5}]  # 주문 한 건의 정보입니다.
selected_amounts = []  # 주문 금액을 모을 빈 리스트를 만듭니다.
def order_amount(order):  # 주문 한 건을 받는 함수를 정의합니다.
    return order["price"] * order["quantity"]  # 단가와 수량을 곱한 값을 돌려줍니다.
for order in orders:  # 주문을 한 건씩 꺼냅니다.
    amounts = order_amount(order)  # 함수가 돌려준 주문 금액을 저장합니다.
    selected_amounts.append(amounts)  # 이번 주문 금액 하나를 리스트에 넣습니다.
print(selected_amounts)  # 반복이 끝나고 완성된 금액 리스트를 출력합니다.
print(sum(selected_amounts))  # 리스트의 모든 금액을 더해 출력합니다.

# [120, 200, 150]
# 470
# ["quantity"]만 쓰자 글자 하나가 든 리스트를 단가 30번 반복했습니다. order["quantity"]로 바꿔 숫자 5를 꺼냈습니다. 리스트 출력은 for 밖으로 옮겨 세 주문을 처리한 뒤 한 번만 나오게 했고, C만 따로 확인하던 출력도 마무리 코드에서는 뺐습니다. C가 60에서 150으로 바뀌어 합계가 380에서 470으로 90 늘었습니다.
