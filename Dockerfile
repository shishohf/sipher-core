FROM python:3.7
COPY Pipfile .
RUN pip install --upgrade pip pipenv-to-requirements
RUN pip install pipenv
RUN pipenv lock
RUN pipenv run pipenv_to_requirements -o requirements.txt
RUN pip install -r requirements.txt
COPY . .