#using stretch-slim
FROM debian:stretch-slim
LABEL maintainer=danielltoidy@outlook.com
#run update
RUN apt-get update && apt-get install -y python3 build-essential python3-setuptools python3-pip python3-dev default-libmysqlclient-dev 
#copy project files over
COPY ./project /project
#Working Directory
WORKDIR /project
#install requirements
RUN pip3 install --no-cache-dir -r requirements/prod.txt
#copy entrypoint for default configuration
COPY ./dockerfile/dev/web/entrypoint.sh /entrypoint.sh
#make file executable
RUN chmod +x /entrypoint.sh
#set entrypoint
ENTRYPOINT ["/entrypoint.sh"]