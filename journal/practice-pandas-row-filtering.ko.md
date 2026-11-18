# 이전 실습 — pandas 열 선택과 득점 필터

[English](practice-pandas-row-filtering.en.md) · [Code](../lessons/practice/practice-pandas-row-filtering.py) · [Notion](https://app.notion.com/p/41c058a09a5b8182b671d1d94b9f4bfa)

## 01. 목표

축구 CSV를 읽어 선수 이름·득점 열을 확인하고 10골 이상과 20골 이상인 행을 골랐습니다.

---

## 02. 사용한 문법

조건 비교는 행별 참·거짓을 만듭니다. df[조건]으로 참인 행을 선택하고 head()로 처음 다섯 행을 봅니다.

---

## 03. 직접 작성한 코드와 복습 예제

```python
import sys
import pandas as pd
df = pd.read_csv(sys.argv[1])
print(df.head())
print(df['player_name'])
print(df['player_name'].head())
print(df['goals'].head())
goals_10_plus = df[df['goals'] >= 10]
print(goals_10_plus.head())
goals_20_plus = df[df['goals'] >= 20]
print(goals_20_plus.head())
print(df[df['goals'] >= 20].head())
```

---

## 04. 실행 결과

공유한 20골 이상 미리보기의 득점은 22, 39, 29, 21, 26이었습니다. 게시 코드는 샘플 CSV로 재검증했습니다. 실행 시 CSV 경로를 인수로 받습니다.

---

## 05. 오류와 수정

read_csv에 경로를 대입한 줄은 함수 호출로 수정했습니다. 파일 이름을 컬럼명으로 넣은 KeyError와 player_name 오타도 수정했습니다.

---

## 06. 결과 해석

처음 다섯 행은 현재 행 순서에 따릅니다. 시즌·대회를 합산하려면 먼저 행 단위를 확인해야 합니다.

---

## 07. 다음 복습

다른 기준을 적용한 뒤 조건을 만족하는 행을 확인해 봅니다.
