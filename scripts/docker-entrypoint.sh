#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn hackforthesea.wsgi:application \
    --bind 0.0.0.0:80 \
    --workers 3
