FROM clearmatics/autonity:v0.7.0 as autonity

FROM python:3.8.2-alpine3.11

RUN apk add --no-cache --virtual .build-deps gcc musl-dev

WORKDIR /env/initiator
ADD ./initiator/requirements.txt .
RUN pip install -r ./requirements.txt
RUN apk del .build-deps gcc musl-dev
COPY ./initiator /initiator

COPY --from=autonity /usr/local/bin/autonity /usr/local/bin/autonity

ENTRYPOINT ["/initiator/main.py"]
