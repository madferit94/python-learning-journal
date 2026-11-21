# 수업 09 — CSV 파일 읽기
# 실행하면 1번과 2번 출력이 차례로 나옵니다. 각 코드 블록은 따로 실행할 수 있습니다.
# 실행할 때 첫 줄의 파일 이름을 본인의 CSV 경로로 바꾸세요. 옆 주석은 코치가 추가했습니다.

# open()은 CSV를 엽니다. as file은 열린 파일에 이름을 붙이고, with 안의 작업이 끝나면 파일이 자동으로 닫힙니다. readline()은 호출할 때마다 다음 줄 하나를 문자열로 읽습니다. read()는 현재 위치부터 남은 내용을 모두 읽습니다.

# 문제 1 — 열 이름과 첫 기록 읽기
with open("f1_2026_results.csv", encoding="utf-8") as file:  # CSV를 열고 열린 파일에 file이라는 이름을 붙입니다.
    first_line = file.readline()  # 첫 줄에 있는 열 이름을 읽습니다.
    first_record = file.readline()  # 다음 줄에 있는 첫 데이터 기록을 읽습니다.
    print(first_line)  # 열 이름을 화면에 표시합니다.
    print(first_record)  # 첫 데이터 기록을 화면에 표시합니다.

# round,race,circuit,driver,team,grid,position,status,points
#
# 1,Australian GP,Albert Park Grand Prix Circuit,RUS,Mercedes,1,1,Finished,25.0
# 둘째 줄에서 read()를 쓰면 첫 데이터 줄부터 끝까지 읽습니다. readline()으로 바꿔 한 줄만 읽었습니다. 한 시도에서는 저장할 때 fisrt_record, 출력할 때 first_record라고 적었습니다. 두 곳을 first_record로 맞췄습니다. 출력 사이의 빈 줄은 readline()이 가져온 줄바꿈에 print()의 줄바꿈이 더해진 결과입니다.

# 문제 2 — 제목 줄을 빼고 데이터 줄 세기
with open("f1_2026_results.csv", encoding="utf-8") as file:  # 첫 줄부터 읽도록 같은 CSV를 다시 엽니다.
    first_line = file.readline()  # 제목 줄을 먼저 읽어서 반복에서 건너뜁니다.
    count = 0  # 데이터 줄을 세기 전에 개수를 0으로 둡니다.
    for line in file:  # 열린 파일에서 남은 줄을 하나씩 읽습니다.
        count = count + 1  # 데이터 줄 하나를 읽을 때마다 개수를 1 늘립니다.
    print(count)  # for가 끝난 뒤 최종 개수를 한 번만 출력합니다.

# 418
# 처음에는 readline()을 두 번 호출해 첫 데이터 줄까지 지나갔습니다. 한 번만 호출해 제목 줄만 건너뛰었습니다. for를 with 밖에 두면 파일이 닫힌 뒤 읽게 되므로 with 안으로 옮겼습니다. print(count)를 for 안에 두었을 때는 1부터 418까지 출력됐습니다. print(count)를 for와 같은 들여쓰기로 옮기자 418이 한 번만 나왔습니다.

# 문제 3 — 한 행의 의미 설명하기
# 민섭님은 한 행을 드라이버 결과라고 설명했습니다. 정리하면 한 행은 한 드라이버의 한 경기 결과입니다. 같은 드라이버가 여러 경기에 나오므로 418은 경기 결과 기록 수입니다. 이 CSV를 그대로 표로 불러온 뒤 SQL에서 COUNT(*)를 쓰면 같은 단위의 행을 셉니다.

# 다음 복습
# 다음 수업은 4장 4.1절 NumPy 배열 기초입니다. 교재의 작은 숫자 예제로 리스트와 배열의 곱셈을 비교하고, 배열의 모양(shape)을 확인합니다.
