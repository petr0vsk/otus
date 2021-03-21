import json
from flask import render_template, request, redirect, url_for
from landing import app

from .forms import LandingForm, ViewItemsForm
from .models import EmailSignup

@app.route("/", methods=['GET', 'POST'])
def home():
    form = LandingForm()
    if form.validate_on_submit():
        data = {
            "full_name": form.full_name.data,
            "email": form.email.data
        }
        obj = EmailSignup.query.filter_by(email=form.email.data).first()
        if obj is None:
            obj = EmailSignup(**data) 
            obj.save()
        return redirect('/items/')
    return render_template('home.html', form=form)

@app.route("/items/", methods=['GET'])
def item_list():
    object_list = EmailSignup.query.all()
    return render_template("items/list.html", object_list = object_list)


@app.route("/items/<int:id>/", methods=['GET'])
def item_detail(id):
    instance = EmailSignup.query.filter_by(id=id).first_or_404()
    return render_template('items/detail.html', instance=instance)

@app.route("/items/<int:id>/delete/", methods=['GET', 'POST'])
def item_delete(id):
    instance = EmailSignup.query.filter_by(id=id).first_or_404()
    if request.method == "POST":
        instance.delete()
        return redirect("/")
    return render_template('items/delete.html', instance=instance)








