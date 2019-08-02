import json
import requests
from itertools import groupby as _groupby
from datetime import datetime
from flask import Flask, render_template


app = Flask(__name__)


def groupby(iterable, key):
    return _groupby(sorted(iterable, key=key), key)


def to_time(minutes: int) -> str:
    return '%02d:%02d' % divmod(minutes, 60)


@app.route('/schedule.xml')
def schedule_xml():
    schedule = requests.get('https://2019.pycon-au.org/schedule/avdata.json').json()[
        'schedule'
    ]
    schedule = [
        dict(talk, start=datetime.fromisoformat(talk['start'])) for talk in schedule
    ]

    days = groupby(schedule, lambda talk: talk['start'].date())
    days = {date: groupby(talks, lambda talk: talk['room']) for date, talks in days}

    return (
        render_template(
            'schedule.xml', days=days, enumerate=enumerate, to_time=to_time
        ),
        200,
        {'content-type': 'application/xml'},
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
