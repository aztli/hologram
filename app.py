from sanic import Sanic
from hologram.server import server, jinja

app = Sanic("hologram")

app.blueprint(server)
jinja.init_app(app)

app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
