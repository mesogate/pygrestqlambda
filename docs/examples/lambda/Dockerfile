FROM public.ecr.aws/lambda/python:3.12

RUN pip install pygrestqlambda

COPY app.py ${LAMBDA_TASK_ROOT}

CMD [ "app.handler" ]
