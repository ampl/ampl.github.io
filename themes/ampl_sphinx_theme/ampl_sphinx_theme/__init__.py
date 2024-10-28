import os

def setup(app):
    theme_dir = os.path.abspath(os.path.dirname(__file__))
    print(f"Theme directory: {theme_dir}")
    app.add_html_theme('ampl_sphinx_theme', theme_dir)
