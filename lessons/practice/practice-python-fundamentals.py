# Python 기초 실습 복습
# 원본: # 문제 1.py
# 사용자가 연습한 코드를 바탕으로 AI가 설명과 구조를 정리한 복습 자료입니다.
# 원래의 시도와 오류 기록은 원본 파일에 그대로 남아 있습니다.
# 실제 선수 기록이 아닌 학습용 가상 숫자를 사용합니다.
#
# 사용 방법
# 1. 코드는 VS Code의 편집기에 작성합니다.
# 2. Cmd + S로 저장합니다.
# 3. 터미널에 >>>가 보이면 exit()을 입력해 Python 입력창에서 나옵니다.
# 4. % 또는 $ 뒤에서 다음 명령으로 파일 전체를 실행합니다.
# 이 파일은 아래의 복습 예제가 모두 위에서 아래로 실행됩니다.
# 한 부분만 연습하려면 나머지 부분을 선택하고 Cmd + /로 주석 처리하세요.
# 단, 사용하는 변수를 먼저 만드는 줄도 함께 실행해야 합니다.
#
# 함수와 문법 구분
# print(), int()는 함수입니다. 괄호 안의 값을 받아 정해진 작업을 합니다.
# if, elif, else, for는 함수가 아니라 실행 흐름을 정하는 문법입니다.
# =는 값을 저장하는 기호이고, ==는 두 값이 같은지 비교하는 기호입니다.
# # 뒤의 글은 설명용 주석이므로 실행되지 않습니다.


# 01. 변수에 저장하고 출력하기
# 목적: 숫자와 이름을 저장한 뒤 화면에서 확인합니다.
# =의 오른쪽 값을 왼쪽 변수 이름에 저장합니다.
# 숫자 5는 계산할 수 있는 정수이고, "Son"은 글자인 문자열입니다.
print("01. 변수와 출력")
goals = 5
player_name = "Son"
print(goals)        # print()는 변수에 저장된 값을 화면에 보여줍니다. 예상: 5
print(player_name)  # 예상: Son
print("goals")     # 따옴표 안은 변수 이름이 아니라 글자 자체입니다. 예상: goals


# 02. 계산 결과 저장과 재계산
# 목적: 변수 값을 바꿔도 앞에서 계산한 다른 변수는 자동으로 바뀌지 않음을 확인합니다.
print("02. 계산 결과 저장")
goals = 5
assists = 3
goal_contributions = goals + assists  # 지금 계산한 결과 8을 저장합니다.
print(goal_contributions)             # 예상: 8
goals = 7
print(goal_contributions)             # 예상: 8. 자동으로 재계산되지 않습니다.
goal_contributions = goals + assists  # 새 goals 값으로 직접 다시 계산합니다.
print(player_name, goal_contributions)  # 쉼표로 여러 값을 함께 출력합니다. 예상: Son 10


# 03. 문자열과 숫자의 차이, int() 변환
# 목적: 숫자로 보이는 문자열을 계산 가능한 정수로 바꿉니다.
print("03. 문자열과 숫자")
print(7 + 3)      # 숫자끼리 +는 덧셈입니다. 예상: 10
print("7" + "3")  # 문자열끼리 +는 이어 붙이기입니다. 예상: 73

goals_text = "12"
assists_text = "5"
print(goals_text + assists_text)  # 예상: 125
# int()는 "12"처럼 정수로 해석 가능한 문자열을 정수로 바꿉니다.
# 모든 글자를 바꿀 수 있는 것은 아닙니다. int("Son")은 오류가 납니다.
goals = int(goals_text)
assists = int(assists_text)
goal_contributions = goals + assists
print(goal_contributions)  # 예상: 17


# 04. 나눗셈과 참·거짓 비교
# 목적: 경기당 평균 득점을 계산하고 기준을 만족하는지 확인합니다.
print("04. 평균과 비교")
total_goals_text = "18"
matches_text = "6"
total_goals = int(total_goals_text)
matches = int(matches_text)
goals_per_match = total_goals / matches
# /는 나눗셈입니다. 이 예제에서는 정수끼리 나눠도 결과가 실수 3.0입니다.
print(goals_per_match)       # 예상: 3.0
print(goals_per_match >= 2)  # >=는 이상입니다. 예상: True(참)
print(goals_per_match < 2)   # <는 미만입니다. 예상: False(거짓)


# 05. if / else로 실행할 내용 선택하기
# 목적: 평균이 기준을 충족하는 경우와 그렇지 않은 경우를 구분합니다.
print("05. 조건에 따른 출력")
total_goals_text = "9"
matches_text = "6"
total_goals = int(total_goals_text)
matches = int(matches_text)
goals_per_match = total_goals / matches
print(goals_per_match)  # 예상: 1.5

# if 뒤에는 참·거짓으로 판단할 조건을 씁니다.
# :는 아래에 이 조건에서 실행할 코드 묶음이 시작된다는 표시입니다.
# 들여쓴 print()만 해당 조건에 속합니다. 들여쓰기는 공백 4칸으로 통일합니다.
if goals_per_match >= 2:
    print("기준 충족")
else:  # 앞의 조건이 거짓이면 실행하므로 별도 조건식이 필요하지 않습니다.
    print("기준 미달")  # 이 예제의 예상 출력


# 06. 나누기 전에 분모 검사하기
# 목적: 경기 수가 0일 때 나눗셈 오류가 발생하지 않도록 계산 순서를 정합니다.
print("06. 경기 수 검증")
total_goals_text = "12"
matches_text = "0"
total_goals = int(total_goals_text)
matches = int(matches_text)

# Python은 위에서 아래로 실행합니다.
# 검사보다 먼저 total_goals / matches를 계산하면 0으로 나누는 오류가 납니다.
# == 0은 0과 같은지만 검사하고, <= 0은 0과 음수를 모두 검사합니다.
# 이 예제는 경기 수가 양수일 때만 평균을 계산하도록 <= 0을 사용합니다.
if matches <= 0:
    print("경기 수 확인 필요")  # 이 예제의 예상 출력
else:
    goals_per_match = total_goals / matches
    print(goals_per_match)
# 이 실행에서는 else가 실행되지 않아 평균이 새로 계산되지 않습니다.
# REPL에 남아 있는 이전 goals_per_match 값과 혼동하지 않도록 주의합니다.


# 07. 슈팅 전환율 계산하기
# 목적: 슈팅 중 득점으로 이어진 비율을 구합니다.
# 원본에서 '슈팅 정확도'라고 부른 지표의 이름을 바로잡았습니다.
# 득점 / 슈팅은 슈팅 전환율이고, 유효슈팅 / 슈팅과는 다른 지표입니다.
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
# 복습: shots_text를 "0", "-2"로 바꾸고 출력이 어떻게 달라질지 예상하세요.


# 08. 패스 성공률 계산과 if / elif / else
# 목적: 입력 검사 → 성공률 계산 → 학습용 등급 분류를 연결합니다.
# 아래 등급 기준은 연습용이며 실제 축구 평가의 보편적 기준이 아닙니다.
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
# 검증용 입력: 42/60 → 70.0, 보통 / 48/60 → 80.0, 우수
# 시도 수가 0이면 검사 메시지만 출력되고 계산과 등급 판정은 건너뜁니다.
# 주의: 이 코드는 성공 횟수가 시도 횟수보다 큰 경우까지 검사하지는 않습니다.


# 09. 리스트에 여러 값 저장하고 하나 선택하기
# 목적: 선수별 값을 한 변수에 모으고 위치로 선택합니다.
print("09. 리스트와 위치 번호")
completed_passes = [48, 42, 30]  # [] 안에 값을 쉼표로 구분해 저장합니다.
player_names = ["Son", "Kim", "Lee"]
print(player_names)     # 전체 목록 출력. 예상: ['Son', 'Kim', 'Lee']
print(player_names[0])  # 위치 번호는 0부터 시작합니다. 첫 번째: Son
print(player_names[1])  # 두 번째: Kim
print(player_names[2])  # 세 번째: Lee
# completed_passes[1]은 두 번째 값 하나를 선택한다는 뜻입니다.
# 이 두 리스트에서 같은 위치가 같은 선수라는 것은 이번 예제의 가정입니다.
# 이름과 기록의 순서가 달라지면 잘못 연결되므로 주의해야 합니다.


# 10. 리스트에서 선택한 값으로 계산하기
# 목적: 값 선택 → 새 변수에 저장 → 비율 계산을 연결합니다.
# 모든 선수의 패스 시도 수가 60회라고 가정합니다.
print("10. Kim의 패스 성공률")
kim_completed = completed_passes[1]  # 두 번째 값 42를 저장합니다.
print(kim_completed)                # 예상: 42
kim_accuracy = kim_completed / 60 * 100
print(kim_accuracy)                 # 예상: 70.0


# 11. 리스트에서 선택한 선수의 성공률과 등급
# 원본의 Lee_completed / Son_completed는 소문자 변수명으로 정리했습니다.
# 대문자로 시작해도 문법 오류는 아니지만, 대소문자가 다르면 다른 변수입니다.
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
# 원본에서 son_completed에 [1]을 넣어 '보통'을 확인하는 실험도 했습니다.
# 변수 이름이 son_completed여도 오른쪽 [1]이 선택하는 값은 Kim의 42입니다.
# 실행 결과는 변수 이름의 뜻이 아니라 실제 저장된 값에 따라 결정됩니다.


# 12. 반복해서 만났던 오류와 해결 방법 — 설명용 기록
# NameError: 변수를 만들기 전에 쓰거나 이름의 철자·대소문자가 다른 경우 확인합니다.
# ZeroDivisionError: 0으로 나눴습니다. 계산 전에 분모를 검사합니다.
# IndentationError: 들여쓰기 위치가 잘못됐거나 if 아래 실행 내용이 없습니다.
# - 맨 바깥 if / elif / else는 맨 왼쪽에서 시작합니다.
# - 각 조건에 속하는 코드는 한 단계 들여씁니다.
# - if 한 줄만 보내지 말고 편집기에 전체를 작성해 파일을 실행합니다.
# SyntaxError: Python 입력창 >>>에 /usr/local/bin/python3 같은 셸 명령을 넣었는지 확인합니다.
# zsh: command not found / bad pattern / number expected:
# - 셸 입력 줄 %에 Python 코드를 입력한 상황이었습니다.
# - Python 코드는 편집기에, 파일 실행 명령은 셸에 작성합니다.
# print("pass_accuracy")는 변수값이 아닌 글자 pass_accuracy를 출력합니다.
# 계산식만 작성하면 .py 파일에서는 화면에 결과가 자동 출력되지 않습니다.
# 값을 저장하고 print(변수명)으로 확인합니다.


# 13. 다음 학습: for 반복문 — 설명만 제시됨, 사용자 실행은 아직 확인되지 않음
# 목적: 리스트의 각 값을 하나씩 선택해 같은 작업을 반복합니다.
# 아래 예제는 아직 주석 상태입니다. 수업에서 설명을 확인한 뒤 실행하세요.
# for와 in은 반복문 문법이고, passes는 직접 정한 변수 이름입니다.
# 매번 리스트의 다음 값이 passes에 저장되고, 들여쓴 print가 실행됩니다.
# completed_passes = [48, 42, 30]
# for passes in completed_passes:
#     print(passes)
# 예상 출력: 48, 42, 30이 각각 한 줄씩 표시됩니다.


# 14. 혼자 다시 작성하는 연습 공간
# 위 예제를 잠시 가리고 아래 순서대로 작성해보세요.
# 1. 성공한 패스 수 [48, 42, 30]을 리스트에 저장합니다.
# 2. 두 번째 값을 골라 변수에 저장합니다.
# 3. 시도 수 60회 기준으로 성공률을 계산합니다.
# 4. if / elif / else로 연습용 등급을 출력합니다.
# 5. 선택 위치를 바꿨을 때 결과를 먼저 예상하고 실행합니다.
# 실행 전 예상:
# 실제 출력:
# 예상과 달랐다면 원인:
