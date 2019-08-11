import requests
from itertools import groupby as _groupby
from datetime import datetime, date, timedelta
from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)

TWO_DAYS = timedelta(days=3)
DATES = {
    str(date.year): (date, date + TWO_DAYS)
    for date in (date(2018, 8, 24), date(2019, 8, 1))
}


def groupby(iterable, key):
    return _groupby(sorted(iterable, key=key), key)


def to_time(minutes: int) -> str:
    return '%02d:%02d' % divmod(minutes, 60)


@app.route('/schedule.xml')
def schedule_xml():
    return redirect(url_for('schedule_year_xml', year='2019'))


@app.route('/<year>/schedule.xml')
def schedule_year_xml(year):
    schedule = requests.get(
        f'https://{year}.pycon-au.org/schedule/avdata.json'
    ).json()['schedule']

    schedule = [
        dict(talk, start=datetime.fromisoformat(talk['start']))
        for talk in schedule
    ]

    days = groupby(schedule, lambda talk: talk['start'].date())
    days = {
        date: groupby(talks, lambda talk: talk['room']) for date, talks in days
    }

    start_date, end_date = DATES[year]
    return (
        render_template(
            'schedule.xml',
            days=days,
            to_time=to_time,
            start_date=start_date,
            end_date=end_date,
        ),
        200,
        {'content-type': 'application/xml'},
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
