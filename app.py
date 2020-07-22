import json
import urllib3
from jinja2 import Environment, FileSystemLoader

MAX_POSTS = 5

# Setup
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('README.template')
http = urllib3.PoolManager()

def get_latest_posts():
    r = http.request('GET', 'https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Frafnixg.dev%2Frss%2F')
    data = json.loads(r.data.decode('utf-8'))['items']
    return data[0:MAX_POSTS]

def render_readme(data):
    render = template.render(**data)
    with open("README.md", "w") as f:
        f.write(render)

def main():

    latest_posts = get_latest_posts()
    data = {
        'latest_post': latest_posts
    }
    render_readme(data)


if __name__ == "__main__":
    main()