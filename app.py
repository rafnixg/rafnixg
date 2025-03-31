"""Render README.md file with latest blog posts."""

from jinja2 import Environment, FileSystemLoader
from rafnixg import BlogPosts


# Maximum number of posts to show
MAX_POSTS = 5

# Setup Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))

# Load blog posts Instance
blog_posts = BlogPosts()


def get_latest_posts(max_posts: int) -> list:
    """Get the latest blog posts.
    Args:
        max_posts (int): Number of posts to show.
    Returns:
        list: List of latest blog posts.
    """
    # Check if max_posts is None or 0
    if not max_posts:
        max_posts = MAX_POSTS
    # Get the latest blog posts
    data = blog_posts.posts
    return data[0:max_posts]

def render_readme(data: dict) -> None:
    """Render README.md file with latest blog posts.	
    Args:
        data (dict): Data to render.
    """
    # Check if data is None
    if not data:
        raise ValueError("Data is None")
    # Load the template
    template = env.get_template('README.template')
    render = template.render(**data)
    # Write the rendered template to README.md
    with open("README.md", "w", encoding="UTF-8") as f:
        f.write(render)

def main():
    """Main function to render README.md file with latest blog posts."""
    # Get the latest blog posts
    latest_posts = get_latest_posts(MAX_POSTS)
    # Check if latest_posts is None
    if not latest_posts:
        raise ValueError("Latest posts are None")
    # Data to render
    data = {
        'latest_post': latest_posts
    }
    # Render the README.md file
    render_readme(data)

    # Print the rendered template
    print("README.md file rendered successfully.")

if __name__ == "__main__":
    main()
