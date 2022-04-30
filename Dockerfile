# 基本的には標準のpythonから作成する
FROM python:3.8

# APP_PATHである'/code'ディレクトリは勝手に作成される
WORKDIR /code

# コンテナのセットアップ
RUN apt-get update && \
    apt-get upgrade -y && \
    pip install poetry

COPY . .

# 必要なパッケージ等をインストールする
RUN poetry install

EXPOSE 8080
