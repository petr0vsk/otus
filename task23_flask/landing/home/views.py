import json
from flask import render_template, request, redirect, url_for
from landing import app



from .forms import LandingForm, ViewItemsForm


@app.route("/", methods=['GET', 'POST'])
def home():
    form = LandingForm()
    if form.validate_on_submit():
        return render_template('success.html',name=form.full_name.data, email=form.email.data)
    return render_template('home.html', form=form)

 
