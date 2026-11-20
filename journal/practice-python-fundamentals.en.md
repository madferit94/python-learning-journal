# Earlier practice — Python fundamentals and rates

> Reference material compiled from older files. Learner authorship is unconfirmed.

[한국어](practice-python-fundamentals.ko.md) · [Code](../lessons/practice/practice-python-fundamentals.en.py) · [Notion](https://app.notion.com/p/41c058a09a5b818b9d40f99f36e03afd)

## 01. Goal

Review variables, conversions, conditions and list indexes with football examples.

---

## 02. Concepts

Convert strings with int() and check the denominator before calculating a rate.

---

## 03. Practice code and review examples

```python
print('01. 변수와 출력')
goals = 5
player_name = 'Son'
print(goals)
print(player_name)
print('goals')
print('02. 계산 결과 저장')
goals = 5
assists = 3
goal_contributions = goals + assists
print(goal_contributions)
goals = 7
print(goal_contributions)
goal_contributions = goals + assists
print(player_name, goal_contributions)
print('03. 문자열과 숫자')
print(7 + 3)
print('7' + '3')
goals_text = '12'
assists_text = '5'
print(goals_text + assists_text)
goals = int(goals_text)
assists = int(assists_text)
goal_contributions = goals + assists
print(goal_contributions)
print('04. 평균과 비교')
total_goals_text = '18'
matches_text = '6'
total_goals = int(total_goals_text)
matches = int(matches_text)
goals_per_match = total_goals / matches
print(goals_per_match)
print(goals_per_match >= 2)
print(goals_per_match < 2)
print('05. 조건에 따른 출력')
total_goals_text = '9'
matches_text = '6'
total_goals = int(total_goals_text)
matches = int(matches_text)
goals_per_match = total_goals / matches
print(goals_per_match)
if goals_per_match >= 2:
    print('기준 충족')
else:
    print('기준 미달')
print('06. 경기 수 검증')
total_goals_text = '12'
matches_text = '0'
total_goals = int(total_goals_text)
matches = int(matches_text)
if matches <= 0:
    print('경기 수 확인 필요')
else:
    goals_per_match = total_goals / matches
    print(goals_per_match)
print('07. 슈팅 전환율')
goals_text = '3'
shots_text = '10'
goals = int(goals_text)
shots = int(shots_text)
if shots <= 0:
    print('슈팅 수 확인 필요')
else:
    rate = goals / shots
    print(rate)
print('08. 패스 성공률과 등급')
completed_passes_text = '48'
attempted_passes_text = '60'
completed_passes = int(completed_passes_text)
attempted_passes = int(attempted_passes_text)
if attempted_passes <= 0:
    print('패스 시도 수 확인 필요')
else:
    pass_accuracy = completed_passes / attempted_passes * 100
    print(pass_accuracy)
    if pass_accuracy >= 80:
        print('우수')
    elif pass_accuracy >= 60:
        print('보통')
    else:
        print('개선 필요')
print('09. 리스트와 위치 번호')
completed_passes = [48, 42, 30]
player_names = ['Son', 'Kim', 'Lee']
print(player_names)
print(player_names[0])
print(player_names[1])
print(player_names[2])
print('10. Kim의 패스 성공률')
kim_completed = completed_passes[1]
print(kim_completed)
kim_accuracy = kim_completed / 60 * 100
print(kim_accuracy)
print('11. Lee의 패스 성공률과 등급')
lee_completed = completed_passes[2]
print(lee_completed)
lee_accuracy = lee_completed / 60 * 100
print(lee_accuracy)
if lee_accuracy >= 80:
    print('우수')
elif lee_accuracy >= 60:
    print('보통')
else:
    print('개선 필요')
print('11. Son의 패스 성공률과 등급')
son_completed = completed_passes[0]
print(son_completed)
son_accuracy = son_completed / 60 * 100
print(son_accuracy)
if son_accuracy >= 80:
    print('우수')
elif son_accuracy >= 60:
    print('보통')
else:
    print('개선 필요')
```

---

## 04. Output

A fresh run confirmed 3.0 goals per match, a 30.0 shot conversion percentage and Kim’s 70.0 pass completion percentage.

---

## 05. Corrections

Check spelling and definition order for NameError, guard against division by zero, and pass the variable to print() to display its value.

---

## 06. Interpretation

The practice uses illustrative numbers.

---

## 07. Next practice

Set the match count to zero and check the warning branch.
