from . import db

import ast
from datetime import datetime


class Content(db.Model):
    __tablename__ = 'content'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    title = db.Column(db.Text, default=None)
    date = db.Column(db.String, default=None)
    description = db.Column(db.Text, default=None)
    publisher = db.Column(db.Text, default=None)
    image_url = db.Column(db.String, default=None)
    image_type = db.Column(db.String, default=None)
    image_size = db.Column(db.Integer, default=None)
    image_height = db.Column(db.Integer, default=None)
    image_width = db.Column(db.Integer, default=None)
    image_size_pretty = db.Column(db.String, default=None)
    lang = db.Column(db.String, default=None)
    author = db.Column(db.String, default=None)
    audio = db.Column(db.String, default=None)
    audio_url = db.Column(db.String, default=None)
    audio_type = db.Column(db.String, default=None)
    audio_duration = db.Column(db.Float, default=None)
    audio_size = db.Column(db.Integer, default=None)
    audio_duration_pretty = db.Column(db.String, default=None)
    audio_size_pretty = db.Column(db.String, default=None)
    logo_url = db.Column(db.String, default=None)
    logo_type = db.Column(db.String, default=None)
    logo_size = db.Column(db.Integer, default=None)
    logo_height = db.Column(db.Integer, default=None)
    logo_width = db.Column(db.Integer, default=None)
    logo_size_pretty = db.Column(db.String, default=None)
    video = db.Column(db.String, default=None)
    video_url = db.Column(db.String, default=None)
    video_type = db.Column(db.String, default=None)
    video_duration = db.Column(db.Float, default=None)
    video_size = db.Column(db.Integer, default=None)
    video_height = db.Column(db.Integer, default=None)
    video_width = db.Column(db.String, default=None)
    video_duration_pretty = db.Column(db.String, default=None)
    video_size_pretty = db.Column(db.String, default=None)
    iframe = db.Column(db.Boolean, default=False)
    iframe_html = db.Column(db.String, default=None)
    iframe_scripts = db.Column(db.Text, default=None)
    url = db.Column(db.String, nullable=False)

    def to_json(self, video=True, iframe=True, audio=True):
        json_content = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'lang': self.lang,
            'author': self.author,
            'publisher': self.publisher,
            'image': {'url': self.image_url,
                      'type': self.image_type,
                      'size': self.image_size,
                      'height': self.image_height,
                      'width': self.image_width,
                      'size_pretty': self.image_size_pretty},
            'date': self.date,
            'url': self.url,
            'logo': {'url': self.logo_url,
                     'type': self.logo_type,
                     'size': self.logo_size,
                     'height': self.logo_height,
                     'width': self.logo_width,
                     'size_pretty': self.logo_size_pretty},
            'audio': self.audio,
            'video': self.video,
            'iframe': self.iframe,
        }

        if audio:
            json_content['audio'] = {'url': self.audio_url,
                                     'type': self.audio_type,
                                     'duration': self.audio_duration,
                                     'size': self.audio_size,
                                     'duration_pretty': self.audio_duration_pretty,
                                     'size_pretty': self.audio_size_pretty,
                                      } if self.audio else self.audio
        if iframe:
            json_content['iframe'] = {'html': self.iframe_html,
                                      'scripts': ast.literal_eval(self.iframe_scripts) if self.iframe_scripts else []
                                      } if self.iframe else self.iframe
        if video:
            json_content['video'] = {'url': self.video_url,
                                     'type': self.video_type,
                                     'duration': self.video_duration,
                                     'size': self.video_size,
                                     'height': self.video_height,
                                     'width': self.video_width,
                                     'duration_pretty': self.video_duration_pretty,
                                     'size_pretty': self.video_size_pretty
                                     } if self.video else self.video,

        return json_content

    @staticmethod
    def from_json(json_content):
        c = Content(title=json_content.get('title'),
                    url=json_content.get('url'),
                    description=json_content.get('description'),
                    lang=json_content.get('lang'),
                    author=json_content.get('author'),
                    publisher=json_content.get('publisher'),
                    date=json_content.get('date'),
                    )

        if json_content.get('audio'):
            c.audio = True
            c.audio_url = json_content['audio'].get('url')
            c.audio_type = json_content['audio'].get('type')
            c.audio_duration = json_content['audio'].get('duration')
            c.audio_size = json_content['audio'].get('size')
            c.audio_duration_pretty = json_content['audio'].get('duration_pretty')
            c.audio_size_pretty = json_content['audio'].get('size_pretty')

        if json_content.get('video'):
            c.video = True
            c.video_url = json_content['video'].get('url')
            c.video_type = json_content['video'].get('type')
            c.video_duration = json_content['video'].get('duration')
            c.video_size = json_content['video'].get('size')
            c.video_height = json_content['video'].get('height')
            c.video_width = json_content['video'].get('width')
            c.video_duration_pretty = json_content['video'].get('duration_pretty')
            c.video_size_pretty = json_content['video'].get('size_pretty')

        if json_content.get('iframe'):
            c.iframe = True
            c.iframe_html = json_content['iframe'].get('html')
            c.iframe_scripts = str(json_content['iframe'].get('scripts'))

        if json_content.get('image'):
            c.image_url = json_content['image'].get('url')
            c.image_type = json_content['image'].get('type')
            c.image_size = json_content['image'].get('size')
            c.image_height = json_content['image'].get('height')
            c.image_width = json_content['image'].get('width')
            c.image_size_pretty = json_content['image'].get('size_pretty')

        if json_content.get('logo'):
            c.logo_url = json_content['logo'].get('url')
            c.logo_type = json_content['logo'].get('type')
            c.logo_size = json_content['logo'].get('size')
            c.logo_height = json_content['logo'].get('height')
            c.logo_width = json_content['logo'].get('width')
            c.logo_size_pretty = json_content['logo'].get('size_pretty')

        return c



