FROM node:lts-slim

RUN mkdir /app

WORKDIR /app

COPY src /app

CMD [ "yarn", "install"]

EXPOSE 3000

CMD [ "yarn", "start" ]
