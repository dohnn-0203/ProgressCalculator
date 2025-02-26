from datetime import datetime

# 공정률 계산기 프로그램
# 터미널에 공정률이 표시됩니다.
# 시작날짜, 종료날짜, 현재날짜를 각각 입력하세요.
start = "2025-02-01" # 시작날짜
end = "2025-04-30" # 종료날짜
current = "2025-02-20" # 현재날짜







# 코드부분입니다.
# 아래코드 수정 금지
##################################################################################################################

class ProgressCal:
  def progress(startDate, endDate, currentDate):
    total = (endDate - startDate).days  # 프로젝트 총 기간 (일 단위)
    elapsed = (currentDate - startDate).days  # 현재까지 진행된 기간 (일 단위)
    progress = (elapsed / total) * 100

    return progress

if __name__ == '__main__':
  startDate = datetime.strptime(start, "%Y-%m-%d")  # 프로젝트 시작일
  endDate = datetime.strptime(end, "%Y-%m-%d")   # 프로젝트 종료일 (4월 30일)
  currentDate = datetime.strptime(current, "%Y-%m-%d")  # 오늘 날짜

  progress = ProgressCal.progress(startDate, endDate, currentDate)

  print(f"현재까지의 공정률: {progress:.2f}%") # 터미널에 출력
