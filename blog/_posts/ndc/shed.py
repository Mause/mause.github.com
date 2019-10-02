import json
import requests
from datetime import datetime
from lxml.html import fromstring, Element
from typing import Dict, List, Tuple
from functools import wraps
from flask import Flask, render_template
from itertools import groupby as _groupby, chain

BASE = 'https://ndcsydney.com/'
DAYS = {
    'Wednesday': datetime(2019, 10, 16),
    'Thursday': datetime(2019, 10, 17),
    'Friday': datetime(2019, 10, 18),
}
app = Flask(__name__)


def groupby(iterable, key):
    return _groupby(sorted(iterable, key=key), key)


def cached(func):
    @wraps(func)
    def wrapper(*args):
        slug = func.__name__ + '.json'
        try:
            with open(slug) as fh:
                return json.load(fh)
        except FileNotFoundError:
            pass

        result = func(*args)

        with open(slug, 'w') as fh:
            json.dump(result, fh, indent=2, default=datetime.isoformat)

        return result

    return wrapper


def dotime(day: str, string: str) -> datetime:
    hour, minute = map(int, string.split(':'))
    return DAYS[day].replace(hour=hour, minute=minute)


def process_talk(talk: Element) -> Dict:
    link, = talk.xpath('.//a/@href')
    title, = talk.xpath('.//h2/text()')
    venue, = talk.xpath('.//*[contains(@class, "venue")]')
    speakers, = talk.xpath('.//*[contains(@class, "speaker")]')

    day, time = venue.attrib['data-time'].split('<br/>')
    start, end = time.split(' - ')

    start = dotime(day, start)
    end = dotime(day, end)

    return {
        'name': title,
        'start': start,
        'end': end,
        'duration': (end - start).total_seconds() // 60,
        'conf_url': link,
        'room': venue.text,
        'authors': [speaker.strip() for speaker in speakers.itertext()],
    }


@cached
def get_talks() -> List[Dict]:
    html = get('agenda/')

    talks = html.xpath('.//div[contains(@class, "msnry-item")]')

    return list(map(process_talk, talks))


def get(path: str) -> Element:
    if not path.startswith('http'):
        path = BASE + path
    r = requests.get(path)
    r.raise_for_status()
    return fromstring(r.content)


def get_slug(speaker: str) -> str:
    if speaker == 'Victoria Almazova':
        speaker = 'Viktorija Almazova'
    elif speaker == 'Filip Ekberg':
        speaker += ' 1'

    return speaker.lower().replace(' ', '-')


def process_speaker(speaker: str) -> Dict:
    path = 'speaker/' + get_slug(speaker)
    html = get(path)

    twitter = html.xpath('.//span[contains(text(), "Twitter")]')
    if twitter:
        _, twitter = twitter[0].getparent().itertext()
        twitter = twitter.strip(' @')
    else:
        twitter = None

    print(speaker, twitter)

    return {'name': speaker, 'twitter': twitter, 'url': BASE + path}


@cached
def speakers(talks: List[Dict]) -> List[Dict]:
    speakers = set(chain.from_iterable(talk['authors'] for talk in talks))

    return [process_speaker(speaker) for speaker in speakers if speaker]


def get_talk_description(talk: Dict) -> Tuple[str, str]:
    html = get(talk['conf_url'])
    article, = html.xpath('.//article')

    text = '\n'.join(article.itertext())
    text = '\n'.join(text.split('\n\n')).strip()

    return talk['conf_url'], text


@cached
def get_talk_descriptions(talks: List[Dict]) -> Dict[str, str]:
    return dict(get_talk_description(talk) for talk in talks)


def to_time(minutes: int) -> str:
    return '%02d:%02d' % divmod(minutes, 60)


@app.route('/schedule.xml')
def index():
    schedule = get_talks()

    print({talk['start'] for talk in schedule})

    schedule = [
        dict(talk, start=datetime.fromisoformat(talk['start']))
        for talk in schedule
    ]

    days = groupby(schedule, lambda talk: talk['start'].date())
    days = {
        date: groupby(talks, lambda talk: talk['room']) for date, talks in days
    }

    return (
        render_template(
            'schedule.xml',
            days=days,
            speakers={
                speaker['name']: speaker for speaker in speakers(schedule)
            },
            descriptions=get_talk_descriptions(schedule),
            start_date=DAYS['Wednesday'],
            end_date=DAYS['Friday'],
            to_time=to_time,
        ),
        200,
        {'content-type': 'application/xml'},
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5004)
