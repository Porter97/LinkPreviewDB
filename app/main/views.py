from flask import render_template, request, current_app
from . import main
from .. import db, cache
from ..models import Content
from ..utils import make_cache_key
import requests


@main.route('/')
def index():
    return render_template("templates/index.html")


@main.route('/link')
@cache.cached(key_prefix=make_cache_key, timeout=60)
def get_link():

    url = request.args.get('url')

    params = {'video': True,
              'audio': True,
              'screenshot': False}

    if request.args.get('iframe'):
        params['iframe'] = True

    if url[8:11] != 'www':
        url = url[:8] + 'www.' + url[8:]

    content = Content.query.filter_by(url=url).first()

    if content:
        return {'status': 'success',
                'data': content.to_json(iframe=params['iframe'], video=params['video'], audio=params['audio'])}, 200
    else:
        headers = {'x-api-key': current_app.config['MICROLINK_API_KEY']}
        m_url = 'https://pro.microlink.io?url={}'.format(url)
        r = requests.get(m_url, headers=headers, params=params)

        if r.json().get('status') == 'success':
            content = Content.from_json(r.json().get('data'))
            db.session.add(content)
            db.session.commit()

        return r.json(), 200
