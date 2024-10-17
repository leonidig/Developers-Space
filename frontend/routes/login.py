# from aiohttp import ClientSession
from quart import (render_template,
                   redirect,
                   url_for,
                   request, 
                   flash)
from quart_auth import AuthUser
from sqlalchemy import select
from ..forms import (LoginForm,
                     RegisterForm)
from ..db import (Session,
                  User)
from .. import app


def get_current_user():
    return 1 

current_user_id = get_current_user()
auth_user = AuthUser(auth_id=current_user_id)


@app.get('/register')
async def get_register():
    return await render_template("register.html")


@app.post('/register')
async def register():
    form = RegisterForm()
    if form.validate_on_submit():
        async with Session.begin() as session:
                user = await session.scalar(select(User).where(User.email == form.email.data))
                if user:
                    flash('Email already registered.', 'danger')
                    return await render_template('register.html', form=form)

                nickname = form.email.data.split('@')[0]
                new_user = User(email=form.email.data, nickname=nickname)
                new_user.set_password(form.password.data)
                await session.add(new_user)

                flash('Registration successful. Please log in.', 'success')
                return redirect(url_for('login'))

    return await render_template('register.html', form=form)


@app.get("/login")
async def get_login():
    return await render_template("login.html")



@app.post("/login")
async def login():
    form = LoginForm()
    if form.validate_on_submit():
        async with Session.begin() as session:
                user = await session.scalar(select(User).where(User.email == form.email.data))

                if user and user.check_password(form.password.data):
                    flash('Logged in successfully.', 'success')
                    return redirect(url_for('dashboard'))
                else:
                    flash('Invalid email or password.', 'danger')

    return await render_template('login.html', form=form)