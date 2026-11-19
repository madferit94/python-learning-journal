# 수업 07 — 교재 3장 딕셔너리로 주문 분석하기

[English](lesson-07-dictionaries.en.md) · [수업 코드](../lessons/ch03/lesson_07_ch03_dictionaries.py) · [Notion](https://app.notion.com/p/41d058a09a5b819190bee70d32a9e9ca)

- **딕셔너리 `{}`** — 키와 값을 짝지어 저장합니다. `order["price"]`는 키 `"price"`에 연결된 값 `40`을 꺼냅니다.
- **대괄호 `[]`** — `[]`는 빈 리스트를 만듭니다. 변수 뒤에서는 `orders[0]`처럼 리스트의 위치로, `order["price"]`처럼 딕셔너리의 키로 값을 꺼냅니다.
- **소괄호 `()`** — `append()`, `sum()`, `print()`를 호출할 때 전달할 값을 넣습니다.
- **`append()`와 `sum()`** — `selected_amounts.append(amounts)`는 이번 금액 하나를 기존 리스트 끝에 붙입니다. `sum(selected_amounts)`는 리스트 전체를 받아 합계 숫자 하나를 돌려줍니다. `print(sum(...))`에서는 안쪽 `sum()`부터 실행됩니다.

## 문제 1 — 주문 한 건 만들고 값 꺼내기

주문 A의 이름, 단가, 수량을 키로 꺼냅니다.

```python
order = {"name": "A", "price": 40,"quantity":3}  # 주문 한 건을 키와 값으로 묶습니다.
print(order["name"])  # 키로 꺼낸 값과 함께 넘긴 값이 있으면 같은 줄에 출력합니다.
print(order["price"])  # 키로 꺼낸 값과 함께 넘긴 값이 있으면 같은 줄에 출력합니다.
print(order["quantity"])  # 키로 꺼낸 값과 함께 넘긴 값이 있으면 같은 줄에 출력합니다.
```

```text
A
40
3
```

`order["name"]`처럼 키 이름으로 값을 꺼냈습니다.

---

## 문제 2 — 수량 변경 전후의 금액 계산

수량을 3에서 5로 바꾸고 두 금액을 비교합니다.

```python
order = {"name": "A", "price": 40, "quantity": 3}  # 주문 한 건을 키와 값으로 묶습니다.
amounts = order["price"] * order["quantity"]  # 현재 주문의 단가와 수량을 곱합니다.
print(amounts)  # 현재 금액을 출력합니다.
order["quantity"] = 5  # 수량에 새 값 5를 저장합니다.
amounts = order["price"] * order["quantity"]  # 현재 주문의 단가와 수량을 곱합니다.
print(amounts)  # 현재 금액을 출력합니다.
```

```text
120
200
```

처음에는 `for`를 쓰고 `["price"] * ["quantity"]`를 시도했습니다. 이 두 값은 리스트입니다. `order["price"]`처럼 키로 숫자를 꺼냈습니다. 수량을 먼저 바꿨을 때는 `200`만 나와서, 변경 전후에 계산과 출력을 각각 뒀습니다.

---

## 문제 3 — 세 주문을 리스트에 담아 출력

각 주문의 이름과 금액을 한 줄에 출력합니다.

```python
orders = [{"name": "A", "price":40, "quantity":5},  # 주문 딕셔너리들을 리스트에 담습니다.
          {"name": "B", "price":25, "quantity":8},  # 주문 한 건의 정보를 담습니다.
          {"name": "C", "price":30, "quantity":2}]  # 주문 한 건의 정보를 담습니다.
for order in orders:  # 주문을 한 건씩 꺼냅니다.
    amounts = order["price"] * order["quantity"]  # 현재 주문의 단가와 수량을 곱합니다.
    print(order["name"],amounts)  # 키로 꺼낸 값과 함께 넘긴 값이 있으면 같은 줄에 출력합니다.
```

```text
A 200
B 200
C 60
```

`orders`에 세 번 대입하면 마지막 주문만 남고, 같은 딕셔너리에서 키를 반복하면 뒤의 값이 남습니다. 딕셔너리 세 개를 리스트에 담았습니다. 출력문을 `for` 안으로 옮기고 금액만 찍던 줄을 빼서 주문당 한 줄을 출력했습니다.

---

## 문제 4 — 조건에 맞는 주문만 합산

수량이 5 이상인 주문의 금액을 모아 합계를 구합니다.

```python
orders = [{"name": "A", "price":40, "quantity":5},  # 주문 딕셔너리들을 리스트에 담습니다.
         {"name": "B", "price":25, "quantity":8},  # 주문 한 건의 정보를 담습니다.
         {"name":"C", "price":30, "quantity":2}]  # 주문 한 건의 정보를 담습니다.
selected_amounts = []  # 조건을 통과한 금액을 모을 빈 리스트입니다.
for order in orders:  # 주문을 한 건씩 꺼냅니다.
    if order["quantity"] >= 5:  # 현재 주문의 수량을 확인합니다.
        amounts = order["price"] *  order["quantity"]  # 현재 주문의 단가와 수량을 곱합니다.
        selected_amounts.append(amounts)  # 이번 금액 하나를 리스트 끝에 붙입니다.
print(selected_amounts)  # 반복이 끝난 뒤 리스트를 한 번 출력합니다.
print(sum(selected_amounts))  # 안쪽 sum()으로 합계를 구해 출력합니다.
```

```text
[200, 200]
400
```

처음에는 `print()`만 써서 빈 리스트에 금액이 들어가지 않았습니다. 조건문 안에서 `append()`로 모으고 반복문 밖에서 리스트와 합계를 출력했습니다. 정리본에서는 계산 결과를 사용하지 않던 `sum(selected_amounts)` 한 줄을 덜었습니다.

---

## 문제 5 — 주문 C의 수량을 바꿔 검증

C의 수량만 2에서 5로 바꿔 합계를 다시 확인합니다.

```python
orders = [{"name":"A", "price":40, "quantity":5},  # 주문 딕셔너리들을 리스트에 담습니다.
          {"name":"B", "price":25, "quantity":8},  # 주문 한 건의 정보를 담습니다.
          {"name":"C", "price":30, "quantity":5}]  # 주문 한 건의 정보를 담습니다.
selected_amounts = []  # 조건을 통과한 금액을 모을 빈 리스트입니다.
for order in orders:  # 주문을 한 건씩 꺼냅니다.
    if order["quantity"] >= 5:  # 현재 주문의 수량을 확인합니다.
        amounts = order["price"] * order["quantity"]  # 현재 주문의 단가와 수량을 곱합니다.
        selected_amounts.append(amounts)  # 이번 금액 하나를 리스트 끝에 붙입니다.
print(selected_amounts)  # 반복이 끝난 뒤 리스트를 한 번 출력합니다.
print(sum(selected_amounts))  # 안쪽 sum()으로 합계를 구해 출력합니다.
```

```text
[200, 200, 150]
550
```

C의 수량 `5`가 `>= 5` 조건을 통과했습니다. `30 × 5 = 150`이 추가돼 합계가 `400`에서 `550`이 됐습니다.
