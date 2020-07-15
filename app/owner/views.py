from flask import Blueprint, render_template, request, redirect, url_for
from app.db import owners
from .forms import RegisterOwner, RegisterPet
# from .models import Owner
from app import db

owner = Blueprint('owner', __name__, 'static', template_folder='templates')
# from .models2 import Owners


@owner.route('/')
def show_all():
    return render_template('owner/show_all.html', owners=owners)


@owner.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterOwner(request.form)
    db.create_all()
    name = ''
    age = ''
    city = ''
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        own = Owners(name=name, age=age, city=city)
        db.session.add(own)
        db.session.commit()
        return redirect(url_for('owner.show_all'))

# @owner.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegisterOwner(request.form)
#     if request.method == 'POST' and form.validate():
#         data = dict(request.form)
#         del data['save']
#         owners.append(Owner(**data))
#         return redirect(url_for('owner.show_all'))
#     return render_template('owner/register.html', form=form)
#


@owner.route('/<int:index>/pets')
def show_pets_by_owner(index):
    data = owners[index]
    if not data.pets:
        return redirect(url_for('owner.register_pet', index=index))
    return render_template('owner/show_pets.html', owner=data, index=index)


@owner.route('/<int:index>/pets/register', methods=["GET", "POST"])
def register_pet(index):
    form = RegisterPet(request.form)
    if request.method == 'POST' and form.validate():
        data = dict(request.form)
        del data['save']
        owners[index].add_pet(**data)
        return redirect(url_for('owner.show_pets_by_owner', index=index))
    return render_template('owner/register_pet.html', form=form)


@owner.route('/<int:index>/pets/<int:pet_index>')
def del_pet(index, pet_index):
    owners[index].del_pet_by_index(pet_index)
    return redirect(url_for('owner.show_pets_by_owner', index=index))


@owner.route('/pets/<types>')
def show_owners_by_animal_type(types):
    result = []
    count = 0
    for owner_item in owners:
        for pet in owner_item.pets:
            if pet.animal_type == types:
                count += 1
                result.append(owner_item)
    return render_template('owner/show_all.html', owners=result, count=count, types=types)
