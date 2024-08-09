from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

# Global dictionary to store user-created stories
user_stories = {"default": story},

@app.route('/')
def index():
    """Show form to ask for words."""
    prompts = story.prompts
    return render_template('questions.html', prompts=prompts)

@app.route('/story')
def show_story():
    """Generate and show the story."""
    answers = {prompt: request.args.get(prompt) for prompt in story.prompts}
    generated_story = story.generate(answers)
    return render_template('story.html', story=generated_story)