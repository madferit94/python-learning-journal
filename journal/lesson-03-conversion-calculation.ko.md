# 수업 03 — 문자열을 정수로 바꿔 총금액 계산하기

[English](lesson-03-conversion-calculation.en.md) · [수업 코드](../lessons/ch02/lesson_03_conversion_calculation.py) · [Notion](https://app.notion.com/p/41c058a09a5b81b19b1fd52e4ec17553)

## 🎯 01. 목표와 범위

문자열로 저장한 가격과 수량을 정수로 바꾸고, 두 값을 곱해 총금액을 구했습니다.

---

## 📖 02. 개념

`int()`는 정수로 변환한 결과를 돌려줍니다. `type()`으로 원래 값과 변환 결과의 자료형을 확인했고, `*`로 정수 가격과 수량을 곱했습니다.

---

## ✍️ 03. 직접 작성한 코드

첫 실습에서는 `"25"`와 `"4"`를 정수로 바꿔 곱했습니다. 실행 전 예상은 `100`이었습니다. 아래는 값을 `"18"`과 `"3"`으로 바꾼 최종 풀이입니다.

```python
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
```

---

## 🖥️ 04. 실제 출력

첫 실습에서 총금액 `100`과 원래 가격 `str`, 변환한 가격 `int`를 확인했습니다. 값을 바꾼 뒤 두 번 실행해 아래 결과를 공유했습니다.

```text
<class 'str'>
<class 'str'>
18
3
<class 'int'>
<class 'int'>
54
```

---

## 🛠️ 05. 처음 시도와 수정

4번의 첫 코드는 정수 변환까지 작성해 `18`, `3`을 출력했습니다. 총금액을 계산하라는 안내를 받은 뒤 곱셈과 `print(amount)`를 추가했습니다. 최종 출력은 `54`였고, 사전 예상란은 비어 있었습니다.

---

## 🧠 06. 3번 설명과 이해 확인

처음에는 원래 변수도 바뀐다고 답했다가, 질문의 뜻을 확인한 뒤 자료형이 바뀌지 않는다고 설명했습니다.

`int(price_text)`로 변환한 정수 `25`는 `=` 왼쪽의 `price`에 저장됩니다. `price_text`에는 다시 대입하지 않았으므로 문자열 `"25"`가 그대로 남습니다.

정수 변환 코드는 직접 작성했고, 3번 설명과 4번 마무리는 안내를 받았습니다.

---

### 로컬 파일에 들어 있던 후속 실습

가격 "35"와 수량 "6"으로 작성한 아래 코드는 수업 04의 1회차입니다. 확인한 출력은 35, 6, 210입니다.

```python
price_text = "35"
quantity_text = "6"

price_number = int(price_text)
quantity_number = int(quantity_text)

print(price_number)
print(quantity_number)

amount = price_number * quantity_number
print(amount)
```

---

## 🔁 07. 다음 복습

- [ ] 새 가격과 수량으로 총금액을 먼저 예상한 뒤 변환·곱셈·출력을 한 번에 작성하기
- [ ] 원래 문자열과 변환한 정수의 자료형을 각각 확인하기
