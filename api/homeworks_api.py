from flask import render_template, redirect

from db.HomeworksEntity import HomeworkEntity
from forms import HomeworkForm
from data import fetch_homeworks
from app import db
from flask import Blueprint

homeworks_blueprint = Blueprint('homeworks_blueprint', __name__)


def render_homework(homework):
    value = ""
    date = homework.date
    mini_template = """
       <div>
            <h4>%s</h4>
            <p>%s</p>
            <p>%s</p>
       </div>
    """ % (date, homework.subject, homework.description)
    value += mini_template

    return value


@homeworks_blueprint.route("/HA")
def ha():
    homeworks = fetch_homeworks()
    homeworks_rendered = ""
    for homework in homeworks:
        homeworks_rendered += render_homework(homework)

    rendered_value = render_template("ha.html", homeworks_html=homeworks_rendered)
    return rendered_value


@homeworks_blueprint.route("/addtask", methods=['GET', 'POST'])
def addtask():
    form = HomeworkForm()
    if form.validate_on_submit():
        homework = {
            "subject": form.subject.data,
            "date": form.date.data,
            "description": form.description.data,
            "author": {
                "userId": "kacpero",
                "displayName": "Kacper Lis"
            }
        }

        homework = HomeworkEntity(
            form.subject.data,
            form.date.data,
            form.description.data
        )
        db.session.add(homework)
        db.session.commit()

        return redirect('/HA')

    return render_template('addtask.html', form=form)
