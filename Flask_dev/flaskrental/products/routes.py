from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskrental import db
#from flaskrental.models import Product
#from flaskrental.product.forms import ProductForm

products = Blueprint('users', __name__)

"""
Trying to make the product upload function on the website
@products.route("/product/new", methods=['GET', 'POST'])
@login_required
def new_product():
    form = ProductForm()
    if form.validate_on_submit():
        picture = request.files['image_file.data']
        product = Product(title=form.title.data, description=form.description.data, image_file=picture)
        db.session.add(product)
        db.session.commit()
        flash(f'Product has been uploaded', 'success')
        return redirect(url_for('new_product'))
    return render_template('create_product.html', title='New Product', form=form)
"""