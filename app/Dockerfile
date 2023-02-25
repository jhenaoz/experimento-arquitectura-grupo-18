# syntax=docker/dockerfile:1.4
FROM  python:3.10-alpine AS builder

WORKDIR /app

COPY . /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt


ENTRYPOINT ["python3"]
CMD ["./app/app.py"]

FROM builder as dev-envs

# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /
