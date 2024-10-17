from quart_auth import login_required
from quart import render_template
from .. import app


@app.get("/")
@login_required
async def index():
    return await render_template("index.html")