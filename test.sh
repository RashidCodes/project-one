#!/bin/bash

aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/d2s1k2q2

docker build -t project-one .

docker tag project-one:latest 850980769302.dkr.ecr.us-east-1.amazonaws.com/project-one:latest

docker push 850980769302.dkr.ecr.us-east-1.amazonaws.com/project-one:latest

