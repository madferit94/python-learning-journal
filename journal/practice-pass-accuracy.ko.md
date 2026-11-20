# 이전 실습 — 패스 성공률과 등급

> 참고 자료. 이전 파일에서 정리했으며 원본 작성자는 확인되지 않았습니다.

[English](practice-pass-accuracy.en.md) · [Code](../lessons/practice/practice-pass-accuracy.py) · [Notion](https://app.notion.com/p/41c058a09a5b814cbf45ec97705537d0)

## 01. 목표

리스트에서 패스 기록을 한 건씩 꺼내 성공률과 등급을 출력했습니다.

---

## 02. 사용한 문법

for 안에서 성공률을 계산하고 if, elif, else로 등급을 정했습니다.

---

## 03. 직접 작성한 코드와 복습 예제

```python
completed_passes = [48, 36, 30]
for passes in completed_passes:
    accuracy_passes = passes / 60 * 100
    print(accuracy_passes)
    if accuracy_passes >= 80:
        print('우수')
    elif accuracy_passes >= 60:
        print('보통')
    else:
        print('개선 필요')
```

---

## 04. 실행 결과

정리본 실행 결과입니다.

```text
80.0
우수
60.0
보통
50.0
개선 필요
```

---

## 05. 오류와 수정

반복문 아래 실행 코드가 비어 IndentationError가 발생했습니다. 계산과 출력을 반복문 안에 들여써 매번 실행되도록 했습니다.

---

## 06. 결과 해석

패스 성공 수 48, 36, 30을 각각 60으로 나눠 80.0, 60.0, 50.0을 얻었습니다. 등급 기준은 실습용입니다.

---

## 07. 다음 복습

출력만 반복문 밖으로 옮겼을 때 출력 횟수를 예상합니다.
