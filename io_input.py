def is_palindrome(text):
    """
    문장부호, 공백 등을 포함한 문자열이 회문(palindrome)인지 검사하는 함수
    
    회문: 앞으로 읽어도 뒤로 읽어도 같은 문자열
    - 대소문자를 구분하지 않음
    - 공백, 문장부호 등은 무시함
    
    Args:
        text (str): 검사할 문자열
        
    Returns:
        bool: 회문이면 True, 아니면 False
    """
    # 알파벳, 숫자만 추출하고 소문자로 변환
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # 뒤집어서 같은지 비교
    return cleaned_text == cleaned_text[::-1]

def main():
    # 사용자로부터 문자열 입력 받기
    text = input("회문 검사할 문자열을 입력하세요: ")
    
    # 회문 검사 결과 출력
    if is_palindrome(text):
        print(f"'{text}'는 회문입니다.")
    else:
        print(f"'{text}'는 회문이 아닙니다.")
    
    # 예시 문장 테스트
    example = "Rise to vote, sir."
    print(f"\n예시: '{example}'")
    if is_palindrome(example):
        print(f"'{example}'는 회문입니다.")
    else:
        print(f"'{example}'는 회문이 아닙니다.")

if __name__ == "__main__":
    main()

