# If you have to modify this file, it will trigger a build of quay.io/vincentrouvreau/quay_automated_build
# docker image used by .github/workflows/test_sample.yml
# Please consider making a separate PR for docker to be built, and your changes in the code

# minimal docker containers for python applications
# https://blog.realkinetic.com/building-minimal-docker-containers-for-python-applications-37d0272c52f3
FROM python:3.7-alpine

# required for numpy
RUN apk add g++

# 1st solution
#RUN pip install numpy pytest
# Not really DRY

# 2nd solution
COPY requirements.txt /
RUN pip install -r /requirements.txt
# How to build the docker image when dockerfile and requirements.txt change ?