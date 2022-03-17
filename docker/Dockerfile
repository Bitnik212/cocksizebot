FROM python:3.10
# set work directory
WORKDIR /app/
# copy project
COPY . /app/
# install dependencies
RUN pip install -r requirements.txt
# run app
CMD ["python", "Bot.py"]
