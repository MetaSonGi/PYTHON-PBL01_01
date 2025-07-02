# Python PBL 과제 - 로그 분석 소프트웨어 개발

## 📚 과제 개요

본 프로젝트는 **로그 분석 소프트웨어 개발**을 목표로 합니다. Python 언어를 사용하여 로그 데이터를 분석하고, 분석 결과를 Markdown 보고서로 작성합니다.

---

## ✅ 수행 과제

- Python 설치
- Python 개발 도구 조사 및 비교 후 하나 선정하여 설치
- 설치 검증을 위한 ‘Hello Mars’ 출력
- `mission_computer_main.log` 파일을 열어 전체 내용을 출력 (main.py)
- 파일 처리 시 발생할 수 있는 예외 처리 구현
- 로그 내용 분석 후 사고 원인 분석 보고서 작성 (`log_analysis.md`)

---

## 🛠 개발 환경 및 규칙

- **Python 버전:** 3.x
- **라이브러리 사용 금지**
  - Python 기본 제공 명령어만 사용
- **코딩 스타일**
  - [PEP 8 – 파이썬 코드 스타일 가이드](https://peps.python.org/pep-0008/) 준수
  - 문자열은 `' '` (single quotes) 사용을 기본으로 하되, 문자열 내 `'` 사용 시 `" "` (double quotes) 사용
  - 대입문의 `=` 앞뒤로 공백 사용
    ```python
    foo = (0,)
    ```
  - 들여쓰기는 **공백**으로 작성

---

## 💻 실행 방법

1. Python 설치
2. 개발 도구 설치
3. `main.py` 실행
    ```bash
    python main.py
    ```
4. 로그 출력 확인
5. `log_analysis.md` 에 사고 원인 분석 내용 작성

---

## 📝 결과물

- `main.py`  
  → 로그 파일을 열어 전체 내용을 출력하며, 예외 처리를 포함한 Python 스크립트

- `log_analysis.md`  
  → 로그를 기반으로 한 사고 원인 분석 보고서 (Markdown 형식)

- 'mission_computer_main.log'
 → 사고 원인 로그

---

> 🚀 **Note:**  
> 로그 데이터 파일(`mission_computer_main.log`)은 별도로 제공되며, 본 저장소에는 포함되지 않습니다.
