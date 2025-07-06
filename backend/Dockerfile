FROM public.ecr.aws/lambda/python:3.11

# 作業ディレクトリ
WORKDIR /var/task

# 依存インストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリコード追加
COPY app app/

# Lambda Entrypoint
CMD ["app.main.handler"]
