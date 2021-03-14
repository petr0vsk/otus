from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, ValidationError, HiddenField
from sqlalchemy import not_



class ViewItemsForm(FlaskForm):
    password = PasswordField('Password', validators=[
            validators.DataRequired(
                    message='You full name is required'
            )
        ])

    def validate_password(self, field):
        if field.data != 'e3@#@#3c9-06c8-4c30-8a12-08fDFA:1688f5':
            raise ValidationError("You do not have permission to view this.")


class LandingForm(FlaskForm):
    id = HiddenField('id')
    full_name = StringField('Full name', 
        render_kw={"class": "form-control", 
            "placeholder": "Full name"},
        validators=[
            validators.DataRequired(
                    message='You full name is required'
            )
        ])
    email = StringField('Email', 
        render_kw={"class": "form-control", 
            "placeholder": "Your email"},
        validators=[
            validators.DataRequired(
                    message='You email is required'
            ),
            validators.Email()
        ])

    
