from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, SelectField
from wtforms.validators import Required, Email, EqualTo


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category = SelectField('Pitch Category', choices=[('Sales','Sales'),('Interview','Interview'),
    ('Elevator','Elevator'),('Promotion','Promotion'),('Personal','Personal'),
    ('Pickup-lines','Pickup-lines')],validators=[Required()])
    post = TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField('Post Pitch')


class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Comment')