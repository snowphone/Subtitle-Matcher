FROM python:3.10-alpine
COPY requirements.txt ./requirements.txt
COPY subtitle_matcher.py /usr/bin/match_subtitles

RUN pip install -r requirements.txt
RUN chmod +x /usr/bin/match_subtitles

ENTRYPOINT [ "match_subtitles" ]
CMD [ "-h" ]

