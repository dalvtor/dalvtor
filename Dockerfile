FROM python:latest
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
ARG APP_ENV=${APP_ENV}
RUN mkdir /src
RUN mkdir /static
WORKDIR /src
ADD ./src /src
ADD entrypoint-${APP_ENV}.sh /entrypoint.sh
COPY ./wait_for_it.sh /wait_for_it.sh
RUN ["chmod", "+x", "/wait_for_it.sh"]
RUN pip install -r requirements.txt
ENTRYPOINT ["bash", "/entrypoint.sh"]