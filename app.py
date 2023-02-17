from flask import Flask, render_template
import markdown
import os

app = Flask(__name__, template_folder='')

def generate(page_name):
    # Look for a Markdown file with the same name as the requested page
    md_file_path = f"pages/{page_name}.md"
    if not os.path.isfile(md_file_path):
        return render_template('404.html'), 404

    # Read the Markdown file and convert it to HTML
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
    html = markdown.markdown(md_text, output_format='html5', extensions=['fenced_code', 'tables', 'pymdownx.inlinehilite', 'pymdownx.highlight'])

    # Render the HTML as a template
    return render_template('page.html', html=html, page_name=page_name)

@app.route('/<page_name>')
def show_page(page_name):
    return generate(page_name)

@app.route('/')
def main_page():
    return generate('index')
