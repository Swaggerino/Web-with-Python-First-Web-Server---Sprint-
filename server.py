from flask import *
from build import *


table_magic()


app = Flask(__name__)


@app.route('/story', methods=['GET'])
def story():
    return render_template('form.html')


@app.route('/story', methods=['POST'])
def add_story():
    columns = ['title', 'story', 'criteria', 'value', 'estimation', 'status']
    data = [request.form[element] for element in columns]
    new_story = UserStory(
                story_title=data[0],
                user_story=data[1],
                acceptance_criteria=data[2],
                business_value=data[3],
                estimation=data[4],
                status=data[5],)
    new_story.save()
    return redirect(url_for('add_story'))


@app.route('/list')
def list_story():
    story = UserStory.select()
    return render_template('list.html', user_stories=story, site='http://localhost:5000/delete', site2='http://localhost:5000/story')


@app.route('/story/<story_id>', methods=['GET'])
def show_stories(story_id):
    story = UserStory.get(UserStory.id == story_id)
    return render_template("form.html", user_story=story)


@app.route('/story/<story_id>', methods=['POST'])
def edit_story(story_id):
    story = UserStory.update(story_title=request.form['title'],
                             user_story=request.form['story'],
                             acceptance_criteria=request.form['criteria'],
                             business_value=request.form['value'],
                             estimation=request.form['estimation'],
                             status=request.form['status']). \
        where(UserStory.id == story_id)
    story.execute()
    return 'Updated the database'


@app.route('/delete/<story_id>', methods=['GET'])
def delete_story(story_id):
    story = UserStory.get(UserStory.id == story_id)
    story.delete_instance()
    return redirect('http://localhost:5000/list')


app.run(debug=True)
