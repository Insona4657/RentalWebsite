from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired

"""        
class ProductForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(message='Please Enter a Product Title'), Length(min=2, max=30)])
    description = StringField('Description', validators=[DataRequired(message='Please Enter a Description of the product'), Length(min=2, max=100)])
    image_file = FileField('Upload Product Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Upload')
"""