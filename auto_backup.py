###############################################################
# auto_backup.py - 자동 백업 프로그램
# 
# 설명: 이 스크립트는 매일 오후 7시에
# 지정된 디렉토리의 내용을 자동으로 백업합니다.
# 
# 사용 방법:
# 1. 이 스크립트를 Windows 작업 스케줄러에 등록
# 2. 매일 오후 7시에 자동으로 실행됨
###############################################################

import os
import time
import shutil
import logging
from datetime import datetime

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('auto_backup.log'),
        logging.StreamHandler()
    ]
)

def create_backup():
    try:
        # 백업할 소스 디렉토리 지정
        source = r'C:\Bearyy'
        
        # 백업 파일이 저장될 대상 디렉토리
        target_dir = r'C:\Backup'
        
        # 현재 날짜와 시간을 이용하여 백업 파일의 이름 생성
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        target = os.path.join(target_dir, f"auto_backup_{timestamp}.zip")
        
        print("\n=== 자동 백업 진행 상황 ===")
        print("1. 대상 디렉토리 확인 중...")
        
        # 대상 디렉토리가 존재하지 않으면 새로 생성
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            print("   - 대상 디렉토리를 생성했습니다.")
        else:
            print("   - 대상 디렉토리가 이미 존재합니다.")
        
        print("\n2. 소스 디렉토리 확인 중...")
        # 소스 디렉토리 존재 확인
        if not os.path.exists(source):
            print("   - 오류: 소스 디렉토리가 존재하지 않습니다!")
            logging.error(f"소스 디렉토리 '{source}'가 존재하지 않습니다.")
            return False
        else:
            print("   - 소스 디렉토리가 확인되었습니다.")
        
        print("\n3. 백업 파일 생성 중...")
        logging.info(f"백업 시작: {source} -> {target}")
        
        # 백업 파일 생성
        archive_name = os.path.splitext(target)[0]
        shutil.make_archive(archive_name, 'zip', source)
        
        # 백업 파일 크기 확인
        backup_size = os.path.getsize(target)
        size_mb = backup_size / (1024 * 1024)  # 바이트를 MB로 변환
        
        print("   - 백업 파일이 생성되었습니다.")
        print(f"   - 백업 파일 크기: {size_mb:.2f} MB")
        
        print("\n=== 자동 백업 완료 ===")
        print(f"백업 파일 위치: {target}")
        logging.info(f"백업 완료: {target} (크기: {size_mb:.2f} MB)")
        return True
        
    except Exception as e:
        print("\n=== 자동 백업 실패 ===")
        print(f"오류 발생: {str(e)}")
        logging.error(f"백업 중 오류 발생: {str(e)}")
        return False

def cleanup_old_backups(days=30):
    """오래된 백업 파일 정리"""
    try:
        target_dir = r'C:\Backup'
        current_time = time.time()
        
        for filename in os.listdir(target_dir):
            if filename.startswith('auto_backup_') and filename.endswith('.zip'):
                filepath = os.path.join(target_dir, filename)
                file_time = os.path.getmtime(filepath)
                
                if (current_time - file_time) > (days * 24 * 60 * 60):
                    os.remove(filepath)
                    logging.info(f"오래된 백업 파일 삭제: {filename}")
                    
    except Exception as e:
        logging.error(f"오래된 백업 파일 정리 중 오류 발생: {str(e)}")

def main():
    logging.info("자동 백업 프로그램 시작")
    
    # 백업 실행
    if create_backup():
        logging.info("자동 백업이 성공적으로 완료되었습니다.")
    else:
        logging.error("자동 백업이 실패했습니다.")
    
    # 30일 이상 된 백업 파일 정리
    cleanup_old_backups(30)
    
    logging.info("자동 백업 프로그램 종료")

if __name__ == "__main__":
    main() 