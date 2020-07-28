import json
import urllib3
from jinja2 import Environment, FileSystemLoader

# Cantidad maxima de posts a mostrar
MAX_POSTS = 5

# Setup
env = Environment(loader=FileSystemLoader('.'))
http = urllib3.PoolManager()

def get_latest_posts(max_posts=5):
    r = http.request('GET', 'https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Frafnixg.dev%2Frss%2F')
    data = json.loads(r.data.decode('utf-8'))['items']
    return data[0:max_posts]

def render_readme(data):
    template = env.get_template('README.template')
    render = template.render(**data)
    with open("README.md", "w") as f:
        f.write(render)

def main():

    latest_posts = get_latest_posts(MAX_POSTS)
    data = {
        'latest_post': latest_posts
    }
    render_readme(data)


if __name__ == "__main__":
    main()