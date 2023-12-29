FROM ubuntu:20.04

# 필요한 패키지 설치, cache 비우기
RUN apt-get update && \
    apt-get install -y curl sudo pip

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

# docker build --no-cache -t docker-python .
# docker run -it --gpus all --name docker-python -p 18087:8080 juhyung1021/docker-python