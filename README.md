> **WARNING!**   
이 프로그램을 사용함으로써 발생하는 모든 일에 대해 책임지지 않습니다.


### 지원되는 플랫폼
- [x] - **윈도우 10 및 11**
- [x] - **지속적인 업데이트**
- [x] - **파이썬 3.9이상**

## 어떻게 사용하나요?

### 1.
```cmd
C:\Users\user....> You can Download it from here!
> https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe
```
### 2.
```sh-session
Nuke_Python.zip파일을 다운받으세요
압축을 푸세요
check_env.bat을 실행시켜주세요
이후 프로그램이 자동으로 돌아갑니다!

NOTE: 필요한 모듈 설치 후에는 귀찮게 check_env.bat을 일일이 실행시키지 않고
-> main_start.bat을 실행시켜주세요!
```

### 이거 혹시 나 괜찮음? 바이러스 걸리거나 제대로 작동 안하지는 않고?

- [x] - **완전** 안전합니다!
- [x] - **버그가 좀 있을 수 있어요.**
- [x] - **파이썬입니다!**

### 💻〢자동 다운로드 모듈 예제:
```py
# 이 프로그램에서 특이한 알고리즘이 쓰였죠!
# 바로 '자동 다운로드' 모듈입니다!
# 반복적인 작업이 많아, 리스트로 만들어서 작업하려 했으나
# 귀찮아서 안 했다는 게 학계의 정설...
import os 
import threading

try:
    import module1
except:
    os.system("pip install module1")
    import module1

try:
    import module2
except:
    os.system("pip install module2")
    import module2
```