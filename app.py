import twint
import asyncio
import nest_asyncio
from asyncio import new_event_loop, set_event_loop
from quart import Quart, render_template, request

nest_asyncio.apply()
app = Quart(__name__)

@app.route("/")
def home(methods=['GET', 'POST']):
    return render_template('home.html')

@app.route('/my-link/')
def my_link():

    print('I got clicked!')
    c = twint.Config()
    c.Store_object = True
    twint.run.Search(c)
    c = twint.Config()
    c.Username = "KeltonMadden"
    c.Limit = 20
    c.Store_object = True
    twint.run.Followers(c)
    followers = twint.output.follows_list

    return str(followers)

if __name__ == '__main__':
    app.run(debug=True)

