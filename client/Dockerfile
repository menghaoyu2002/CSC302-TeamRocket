FROM node:18-alpine3.15

WORKDIR /app

# install app dependencies
COPY package.json .
COPY package-lock.json .
RUN npm ci
RUN npm install -g serve

COPY . .
RUN npm run build

ENV NODE_ENV production

EXPOSE 3000

# start app
CMD ["serve", "build"]