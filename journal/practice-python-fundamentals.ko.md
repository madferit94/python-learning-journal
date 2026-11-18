# 이전 실습 — Python 기초와 비율 계산

[English](practice-python-fundamentals.en.md) · [Code](../lessons/practice/practice-python-fundamentals.py) · [Notion](https://app.notion.com/p/41c058a09a5b818b9d40f99f36e03afd)

## 01. 목표

변수, 형 변환, 조건문, 리스트 위치 번호를 앞서 사용한 축구 예제로 복습했습니다.

---

## 02. 사용한 문법

문자열에 int()를 적용하고, 분모를 확인한 뒤 비율을 계산했습니다.

---

## 03. 직접 작성한 코드와 복습 예제

```python
print("01. 변수와 출력")
goals = 5
player_name = "Son"
print(goals)        # print()는 변수에 저장된 값을 화면에 보여줍니다. 예상: 5
print(player_name)  # 예상: Son
print("goals")     # 따옴표 안은 변수 이름이 아니라 글자 자체입니다. 예상: goals


print("02. 계산 결과 저장")
goals = 5
assists = 3
goal_contributions = goals + assists  # 지금 계산한 결과 8을 저장합니다.
print(goal_contributions)             # 예상: 8
goals = 7
print(goal_contributions)             # 예상: 8. 자동으로 재계산되지 않습니다.
goal_contributions = goals + assists  # 새 goals 값으로 직접 다시 계산합니다.
print(player_name, goal_contributions)  # 쉼표로 여러 값을 함께 출력합니다. 예상: Son 10


print("03. 문자열과 숫자")
print(7 + 3)      # 숫자끼리 +는 덧셈입니다. 예상: 10
print("7" + "3")  # 문자열끼리 +는 이어 붙이기입니다. 예상: 73

goals_text = "12"
assists_text = "5"
print(goals_text + assists_text)  # 예상: 125
goals = int(goals_text)
assists = int(assists_text)
goal_contributions = goals + assists
print(goal_contributions)  # 예상: 17


print("04. 평균과 비교")
total_goals_text = "18"
matches_text = "6"
total_goals = int(total_goals_text)
matches = int(matches_text)
goals_per_match = total_goals / matches
print(goals_per_match)       # 예상: 3.0
print(goals_per_match >= 2)  # >=는 이상입니다. 예상: True(참)
print(goals_per_match < 2)   # <는 미만입니다. 예상: False(거짓)


print("05. 조건에 따른 출력")
total_goals_text = "9"
matches_text = "6"
total_goals = int(total_goals_text)
matches = int(matches_text)
goals_per_match = total_goals / matches
print(goals_per_match)  # 예상: 1.5

if goals_per_match >= 2:
    print("기준 충족")
else:  # 앞의 조건이 거짓이면 실행하므로 별도 조건식이 필요하지 않습니다.
    print("기준 미달")  # 이 예제의 예상 출력


print("06. 경기 수 검증")
total_goals_text = "12"
matches_text = "0"
total_goals = int(total_goals_text)
matches = int(matches_text)

if matches <= 0:
    print("경기 수 확인 필요")  # 이 예제의 예상 출력
else:
    goals_per_match = total_goals / matches
    print(goals_per_match)


print("07. 슈팅 전환율")
goals_text = "3"
shots_text = "10"
goals = int(goals_text)
shots = int(shots_text)
if shots <= 0:
    print("슈팅 수 확인 필요")
else:
    rate = goals / shots
    print(rate)  # 예상: 0.3. 비율 0.3은 백분율로 30%입니다.


print("08. 패스 성공률과 등급")
completed_passes_text = "48"
attempted_passes_text = "60"
completed_passes = int(completed_passes_text)
attempted_passes = int(attempted_passes_text)

if attempted_passes <= 0:
    print("패스 시도 수 확인 필요")
else:
    # 성공 횟수 / 시도 횟수에 100을 곱해 백분율로 표시합니다.
    pass_accuracy = completed_passes / attempted_passes * 100
    print(pass_accuracy)  # 예상: 80.0

    # 바깥 else 안에 있으므로 시도 수가 양수일 때만 등급을 판정합니다.
    # 위에서부터 확인하고, 처음 참인 조건의 코드만 실행합니다.
    # 높은 기준부터 검사해야 80 이상이 먼저 '보통'으로 분류되지 않습니다.
    if pass_accuracy >= 80:
        print("우수")  # 정확히 80도 포함합니다. 이 예제의 예상 출력
    elif pass_accuracy >= 60:  # 앞 조건이 거짓일 때 다음 조건을 검사합니다.
        print("보통")
    else:
        print("개선 필요")


print("09. 리스트와 위치 번호")
completed_passes = [48, 42, 30]  # [] 안에 값을 쉼표로 구분해 저장합니다.
player_names = ["Son", "Kim", "Lee"]
print(player_names)     # 전체 목록 출력. 예상: ['Son', 'Kim', 'Lee']
print(player_names[0])  # 위치 번호는 0부터 시작합니다. 첫 번째: Son
print(player_names[1])  # 두 번째: Kim
print(player_names[2])  # 세 번째: Lee


print("10. Kim의 패스 성공률")
kim_completed = completed_passes[1]  # 두 번째 값 42를 저장합니다.
print(kim_completed)                # 예상: 42
kim_accuracy = kim_completed / 60 * 100
print(kim_accuracy)                 # 예상: 70.0


print("11. Lee의 패스 성공률과 등급")
lee_completed = completed_passes[2]
print(lee_completed)  # 예상: 30
lee_accuracy = lee_completed / 60 * 100
print(lee_accuracy)   # 예상: 50.0
if lee_accuracy >= 80:
    print("우수")
elif lee_accuracy >= 60:
    print("보통")
else:
    print("개선 필요")  # 예상 출력

print("11. Son의 패스 성공률과 등급")
son_completed = completed_passes[0]
print(son_completed)  # 예상: 48
son_accuracy = son_completed / 60 * 100
print(son_accuracy)   # 예상: 80.0
if son_accuracy >= 80:
    print("우수")  # 예상 출력
elif son_accuracy >= 60:
    print("보통")
else:
    print("개선 필요")
```

---

## 04. 실행 결과

정리본 재실행에서 경기당 3.0골, 슈팅 전환율 30.0, Kim 패스 성공률 70.0을 확인했습니다.

---

## 05. 오류와 수정

정의 전에 사용한 이름은 NameError가 납니다. 0으로 나누기 전 경기 수나 시도 수를 확인했습니다. print()에 변수 이름을 따옴표로 감싸면 이름이 그대로 출력됩니다.

---

## 06. 결과 해석

가상 숫자로 문법을 확인하는 복습 예제입니다.

---

## 07. 다음 복습

경기 수를 0으로 바꿔 계산 없이 확인 메시지가 나오는지 살펴봅니다.
