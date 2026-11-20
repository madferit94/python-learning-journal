# 이전 실습 — 반복문과 CSV 컬럼 확인

> 참고 자료. 이전 파일에서 정리했으며 원본 작성자는 확인되지 않았습니다.

[English](practice-csv-column-inspection.en.md) · [Code](../lessons/practice/practice-csv-column-inspection.py) · [Notion](https://app.notion.com/p/41c058a09a5b81d48a0ef9c4d35ac4e4)

## 01. 목표

패스 수를 반복해 성공률을 구한 뒤, pandas로 CSV를 열고 컬럼 이름을 살펴봤습니다.

---

## 02. 사용한 문법

head()는 기본 5행을 표시합니다. columns는 컬럼 이름을 담고 for로 하나씩 꺼낼 수 있습니다.

---

## 03. 직접 작성한 코드와 복습 예제

```python
completed_passes = [54, 24, 12]
print(completed_passes)
for passes in completed_passes:
    accuracy_passes = passes / 60 * 100
    print(accuracy_passes)
    if accuracy_passes >= 80:
        print("우수")
    elif accuracy_passes >= 60:
        print("보통")
    else:
        print("개선 필요")
```

```python
numbers = [10, 20, 30]
for number in numbers:
    doubled = number * 2
    print(doubled)
```

```python
import sys
import pandas as pd

df = pd.read_csv(sys.argv[1])
print(df.head())
print(df.columns)
for column in df.columns:
    print(column)
```

---

## 04. 실행 결과

공유한 패스 성공률은 90.0, 40.0, 20.0입니다. CSV 출력에서는 첫 5행에 같은 선수 이름이 반복됐고 player_name, season_name, team 등의 컬럼을 확인했습니다. 게시 코드에는 실행 시 CSV 경로를 전달합니다.

---

## 05. 오류와 수정

리스트 전체를 60으로 나누면 TypeError가 납니다. 반복 변수로 숫자 하나를 꺼내 계산했습니다. 빈 for 블록에는 실행할 문장이 필요합니다.

---

## 06. 결과 해석

출력문이 반복문 안에 있으면 매번 표시됩니다. 같은 선수 이름이 반복되므로 행의 의미는 시즌·팀·대회 컬럼까지 함께 확인합니다.

---

## 07. 다음 복습

CSV를 읽어 첫 행과 컬럼 이름을 각각 확인해 봅니다.
