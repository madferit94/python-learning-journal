# 수업 02 — 문자열·정수와 형 변환

[English](lesson-02-strings-integers-conversion.en.md) · [코드 / Code](../lessons/ch02/lesson_02_strings_integers_conversion.py)
[Notion](https://app.notion.com/p/41b058a09a5b8137895eec92e5ce5a87)

> 📘 수업 분량 마무리 · 독립 재작성: 힌트 필요 · 다음 회상 미확인

## 🎯 01. 목표와 범위

변수·값·자료형을 복습하고, 문자열 연결과 정수 덧셈을 비교한 뒤 `int()`로 변환한 값을 계산에 사용했습니다.

교재 연결은 『파이썬 라이브러리를 활용한 데이터 분석』 3판 2장 Python 기초입니다. 문제는 교재 개념에 맞춰 코치가 작성했으며 교재 원문 문제는 아닙니다. 보유한 종이책 판본, 직접 읽은 페이지와 실제 학습 시간은 미확인입니다.

---

## 📖 02. 개념과 문법을 쓴 이유

| 문법 | 역할 | 이번 수업에서 쓴 이유 |
| --- | --- | --- |
| `=` | 값을 변수 이름에 대입 | 문자열과 변환 결과를 별도 이름으로 보관 |
| `print()` | 값을 출력 | 실제 결과 확인 |
| `type()` | 자료형 확인 | 같은 숫자 모양의 문자열·정수 구분 |
| `+` | 정수는 덧셈, 문자열은 연결 | `15`와 `123` 차이 비교 |
| `int()` | 변환 가능한 값을 정수로 변환 | 문자열을 수치 계산에 사용 |

`first_number = int(first_text)`는 변환 결과를 새 이름에 저장합니다. 원래 `first_text`에 다시 대입하지 않았으므로 문자열도 그대로 남습니다.

---

## ✍️ 03. 예상과 사용자 작성 코드

**복습 과정:** `item = 12`에서 값과 글자를 출력하고, 코치 안내 후 자료형 출력을 추가했습니다. 문자열 `"12"`로 다시 대입한 뒤 `str` 출력을 확인했습니다. 사용자는 “""로 시작하면 문자열이라서요”라고 설명했습니다.

**숫자와 문자열 비교 — 사용자 코드:**

```python
first = 12
second = 3
total = first + second
print(total)

first_text = "12"
second_text = "3"
joined = first_text + second_text
print(joined)
```

문자열은 연결되어 `123`이 나올 것이라고 실행 전에 설명했습니다. `total`의 사전 예상과 각 자료형 예상은 기록하지 않은 부분이 있어, 모든 결과를 먼저 예측했다고 기록하지 않습니다.

**형 변환 — 힌트 후 사용자가 수정한 최종 코드:**

```python
first_text = "12"
second_text = "3"
first_number = int(first_text)
second_number = int(second_text)
numeric_total = first_number + second_number
print(numeric_total)
print(type(first_text))
print(type(first_number))
print(type(second_text))
print(type(second_number))
```

---

## 🖥️ 04. 실제 출력과 검증 범위

**사용자가 공유한 출력**을 실행 단위별로 구분합니다.

| 실행 | 실제 확인 |
| --- | --- |
| item 첫 출력 | `12`, `item` |
| 정수 자료형 추가 확인 | `<class 'int'>` |
| 문자열로 재대입 후 별도 실행 | `<class 'str'>` |
| 정수 덧셈 / 문자열 연결 | `15`, `123` |

형 변환 코드의 사용자 최종 출력:

```text
15
<class 'str'>
<class 'int'>
<class 'str'>
<class 'int'>
```

정리된 한국어·영어 코드도 AI가 별도로 실행하여 위 다섯 줄과 일치함을 확인했습니다. 사용자 실행과 AI 검증은 구분합니다.

---

## 🛠️ 05. 최초 시도와 수정 이유

**5-1. 변환은 했지만 계산에 원래 문자열을 사용**

```python
first_text = "12"
second_text = "3"
first_number = int(first_text)
second_number = int(second_text)
numeric_total = first_text + second_text
print(numeric_total)
```

실제 출력은 `123`이었습니다. 예외가 아니라, 문자열 변수끼리 연결한 결과입니다. 코치는 “계산 줄의 두 변수를 정수가 저장된 변수 이름으로 바꾸세요”라고 힌트를 주었습니다.

사용자 수정:

```python
numeric_total = first_number + second_number
```

수정 후 실제 출력은 `15`였습니다.

**5-2. 자료형 비교 대상 보완**

처음에는 변환된 두 변수의 자료형만 출력해 `int`, `int`를 확인했습니다. 코치가 원래 변수 `first_text`와 변환 결과 `first_number`를 비교하는 두 줄을 제시했습니다. 사용자는 두 번째 문자열·정수 쌍의 확인까지 추가했습니다.

이번 세션에서는 실제 예외 메시지가 공유되지 않았습니다. 따라서 임의의 예외나 실행 시간을 덧붙이지 않습니다.

---

## 🧠 06. 이해 확인과 도움받은 범위

사용자 설명: “처음에는 문자열이고, 두번째는 정수형이고”. 코치는 계산에 사용한 변수의 자료형에 따라 `+`의 동작이 달라진다고 보완했습니다.

- 확인: 문자열 연결 `123`과 정수 덧셈 `15`, 원래 변수 `str`과 변환된 변수 `int` 출력.
- 사용자 작성: 숫자·문자열 비교, 힌트 후 계산 변수 수정, 두 번째 변수 쌍의 자료형 확인 추가.
- 도움: `type()` 출력 추가 안내, 계산할 변수 선택 힌트, 원본·변환값 자료형 비교 코드.
- 미확인: 모든 단계의 사전 예상, 대입과 형 변환 차이의 별도 설명, 다음 학습에서의 독립 재작성.

**상태는 수업 분량 마무리, 독립 재작성은 힌트 필요로 기록합니다.** 다음의 지연된 독립 재작성은 아직 확인 전입니다.

---

## 🔁 07. 다음 복습

- [ ] `price_text`에 `"25"`, `quantity_text`에 `"4"` 저장
- [ ] 두 문자열을 연결한 결과를 먼저 예상
- [ ] 각각 정수로 변환해 `price`, `quantity`에 저장
- [ ] `price * quantity`를 `amount`에 저장하고 출력 (`*`는 곱셈)
- [ ] `price_text`와 `price`의 자료형 출력
- [ ] 변환 결과를 새 변수에 저장하면 원래 변수도 바뀌는지 설명

아직 풀지 않은 문제이므로 정답·예상·실행 결과는 채우지 않습니다.
