# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

FROM continuumio/miniconda3

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser


# Copy the source code into the container.
# IMPORTANT --
# This will copy _all_ files not defined in ./.dockerignore
# Meaning that files like *.token files or *.ini files will be copied
# We get around this by having those files be imported _prior_ to the build step
# when running from the GH/A runner.
#
# For testing locally, you ***MUST*** supply your own files of:
# `database.ini` & `run.token`
# Otherwise the bot ***will not run*** and will throw an exception
# As of -- `585f484`
COPY . .

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
ARG BOTNAME="OpossumBot"
RUN conda env create -f environment.yml -n ${BOTNAME}
RUN activate ${BOTNAME}
RUN pip install -r requirements.txt

# Switch to the non-privileged user to run the application.
USER appuser

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
CMD activate ${BOTNAME} \
&& python3 src/py/opossum_bot.py
