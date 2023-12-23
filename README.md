문서정보 : 2023.12.23. 작성, 작성자 [@SAgiKPJH](https://github.com/SAgiKPJH)

<br>

### 바로 사용하기
```bash
docker run -it --name vscode-container -p 18087:8080 juhyung1021/docker-python
```

<br>

# Docker_Python
- Python을 동작할 수 있는 독립적인 환경을 구성합니다.
- 아래 조건을 만족해야 합니다.
  1. gpu를 활용하여 docker로 실행합니다.
  2. docker에 vscode로 접근 가능합니다.
  3. 기본적으로 python이 설치되어 있습니다.

### 제작자
[@SAgiKPJH](https://github.com/SAgiKPJH)

<br><br>

---

# dockerfile

```dockerfile
FROM ubuntu:latest

# 필요한 패키지 설치, cache 비우기
RUN apt-get update && \
    apt-get install -y curl sudo

# 새로운 사용자 생성 및 비밀번호 설정
ENV USER="user" \
    PASSWORD="password"
RUN useradd -m ${USER} && echo "${USER}:${PASSWORD}" | chpasswd && adduser ${USER} sudo

# code-server 설치 및 세팅
ENV WORKINGDIR="/home/${USER}/vscode"
RUN curl -fsSL https://code-server.dev/install.sh | sh && \
    mkdir ${WORKINGDIR}
    
# 확장 설치
RUN code-server --install-extension "ms-python.python" \ 
                --install-extension "ms-toolsai.jupyter"

# code-server 시작
ENTRYPOINT nohup code-server --bind-addr 0.0.0.0:8080 --auth password  ${WORKINGDIR}
```

<br>

### build
```bash
docker build --no-cache -t docker-python .
```

<br>

### run

```bash
docker run -it --name vscode-container -p 8080:8080 docker-python
```
