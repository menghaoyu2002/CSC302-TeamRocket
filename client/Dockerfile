FROM node:18-alpine3.15

WORKDIR /app

# install app dependencies
COPY package.json .
COPY package-lock.json .
COPY ./scripts/create-env-file.sh .
RUN npm ci
RUN npm install -g serve

ARG BACKEND_URL

RUN sh create-env-file.sh REACT_APP_BACKEND_URL=$BACKEND_URL

COPY . .
RUN npm run build

ENV NODE_ENV production

EXPOSE 3000

# start app
CMD ["serve", "build"]