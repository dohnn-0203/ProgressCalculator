from datetime import datetime

class ProgressCal:
  def progress(startDate, endDate, currentDate):
    total = (endDate - startDate).days  # 프로젝트 총 기간 (일 단위)
    elapsed = (currentDate - startDate).days  # 현재까지 진행된 기간 (일 단위)
    progress = (elapsed / total) * 100

    return progress

if __name__ == '__main__':
  startDate = datetime(2025, 2, 1)  # 프로젝트 시작일
  endDate = datetime(2025, 4, 30)   # 프로젝트 종료일 (4월 30일)
  currentDate = datetime(2025, 2, 20)  # 오늘 날짜
  progress = ProgressCal.progress(startDate, endDate, currentDate)
  print(f"현재까지의 공정률: {progress:.2f}%")