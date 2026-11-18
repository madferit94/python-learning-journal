# 반복문과 CSV 컬럼 확인
# 실행할 때 CSV 경로를 인수로 전달합니다. 반복문 예제 다음에 CSV를 읽습니다.

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

numbers = [10, 20, 30]
for number in numbers:
    doubled = number * 2
    print(doubled)

import sys
import pandas as pd

df = pd.read_csv(sys.argv[1])
print(df.head())
print(df.columns)
for column in df.columns:
    print(column)
