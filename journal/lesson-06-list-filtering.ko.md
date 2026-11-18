# 수업 06 — 교재 3장 리스트와 조건

[English](lesson-06-list-filtering.en.md) · [수업 코드](../lessons/ch03/lesson_06_ch03_list_filtering.py) · [Notion](https://app.notion.com/p/41c058a09a5b81588b11e6038c474fae)

## 01. 목표

수량 조건에 맞는 주문만 골라 금액을 모으고 합계를 구했습니다.

---

## 02. 사용한 문법

`for`로 수량을 하나씩 꺼내고 `if`로 기준을 확인했습니다. `append()`로 금액을 모아 `sum()`으로 더했습니다.

---

## 03. 직접 작성한 코드

세 블록을 순서대로 실행합니다. 3번은 2번에서 만든 리스트를 사용합니다.

### 1. 조건에 맞는 주문만 계산하기

```python
price = 40  # 단가를 40으로 정합니다.
quantities = [3, 5, 0, 8, 4]  # 주문 수량을 리스트에 담습니다.

for quantity in quantities:  # 수량을 하나씩 꺼냅니다.
    if quantity >= 5:  # 현재 수량이 5 이상인지 확인합니다.
        amount = price * quantity  # 단가와 수량을 곱합니다.
        print(amount)  # 조건에 맞는 주문 금액을 바로 출력합니다.
```

### 2. 금액을 리스트에 모으기

```python
price = 40  # 단가를 40으로 정합니다.
quantities = [3, 5, 0, 8, 4]  # 주문 수량을 리스트에 담습니다.

amounts = []  # 금액을 모을 빈 리스트를 만듭니다.

for quantity in quantities:  # 수량을 하나씩 꺼냅니다.
    if quantity >= 5:  # 현재 수량이 5 이상인지 확인합니다.
        amount = price * quantity  # 단가와 수량을 곱합니다.
        amounts.append(amount)  # 계산한 금액을 리스트 끝에 추가합니다.

print(amounts)  # 반복이 끝난 뒤 리스트를 한 번 출력합니다.
```

### 3. 총금액 합계 구하기

```python
print(sum(amounts))  # 리스트에 담긴 금액을 모두 더해 출력합니다.
```

---

## 04. 실제 출력

조건을 통과한 수량은 `5`와 `8`입니다. 민섭님이 공유한 최종 출력과 정리본의 실행 결과가 일치했습니다.

```text
200
320
[200, 320]
520
```

---

## 05. 중간 오류와 수정한 이유

- `for quantity in quantities >= 5:` → `TypeError`. 리스트 전체를 정수와 비교했습니다. `for`로 수량을 하나씩 꺼낸 뒤 `if quantity >= 5:`에서 비교했습니다.
- `if quantity >= 5` → `SyntaxError`. 줄 끝에 빠진 `:`를 추가해 조건문 블록을 시작했습니다.
- 중간에 긴 반복 리스트가 출력됐습니다. 정수와 리스트를 곱하면 리스트가 반복되므로, `price * quantity`로 수량 하나의 금액을 계산했습니다.
- 중간에 빈 리스트 `[]`도 출력됐습니다. 최종 코드에서는 반복문 전에 빈 리스트를 만들고, 조건을 통과할 때마다 `append()`한 뒤 반복문 밖에서 출력했습니다.
- `sum(amounts = [])` → `TypeError`. 이미 모은 금액 리스트를 첫 번째 인수로 넘기도록 `sum(amounts)`로 수정했습니다.

---

## 06. 반복문 안과 밖

조건문 안에서는 통과한 주문마다 금액을 추가하고, 반복문이 끝나면 리스트와 합계를 한 번씩 출력합니다.

---

### 로컬의 리스트·합계 출력 방식

1번의 개별 금액 출력을 주석으로 꺼 두면 리스트와 합계만 출력됩니다. 아래 실행 범위에서 [200, 320]과 520을 확인했습니다.

```python
price = 40
quantities = [3, 5, 0, 8, 4]
amounts = []
for quantity in quantities:
    if quantity >= 5:
        amount = price * quantity
        amounts.append(amount)
print(amounts)
print(sum(amounts))
```

---

## 07. 다음 복습

최소 수량을 `6`으로 바꿔 리스트와 합계를 먼저 예상하고 실행해 봅니다.
