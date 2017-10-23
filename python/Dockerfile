FROM python:3.5

ARG gyazai_dir=/gyazai/
RUN mkdir $gyazai_dir
WORKDIR $gyazai_dir

COPY requirements.txt $gyazai_dir/requirements.txt
RUN pip install -r requirements.txt

COPY script $gyazai_dir/script
COPY logs $gyazai_dir/logs
