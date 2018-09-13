# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3-onbuild

ENV PYTHONUNBUFFERED 1
ENV DEBUG True
ENV DATABASE_NAME hackforthesea_dev

ADD requirements.txt /
RUN apt-get update
RUN apt-get install apt-utils -y
RUN apt-get install postgresql-client -y

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

# CMD specifcies the command to execute to start the server running.
CMD ["/usr/src/app/scripts/docker/entrypoint"]
# done!
