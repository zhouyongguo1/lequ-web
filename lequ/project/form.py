from wtforms import Form, StringField
from wtforms.validators import DataRequired


class ProjectForm(Form):
    name = StringField(validators=[DataRequired()])

    def to_project(self):
        pass
        # pro = Project()
        # return pro
