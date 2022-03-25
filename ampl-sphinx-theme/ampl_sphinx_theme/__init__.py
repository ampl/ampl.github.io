import pydata_sphinx_theme


def setup(app):
    from os import path

    theme_path = path.abspath(path.dirname(__file__))
    app.add_html_theme("ampl_sphinx_theme", theme_path)
    app.config.templates_path.append(path.join(theme_path, "_templates"))
    pydata_sphinx_theme.setup(app)
