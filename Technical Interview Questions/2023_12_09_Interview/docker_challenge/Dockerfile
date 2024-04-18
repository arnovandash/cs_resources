FROM node:20.10.0-alpine

# Create the cowsay directory inside the container
RUN mkdir /opt/cowsay

# Set the working directory inside the container
WORKDIR /opt/cowsay

# Copy the cowsay file into the container
COPY main ./main.js

EXPOSE 8080

CMD [ "node", "main.js" ]
