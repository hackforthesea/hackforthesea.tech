# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3-onbuild

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

# CMD specifcies the command to execute to start the server running.
CMD ["./scripts/docker-entrypoint.sh"]
# done!