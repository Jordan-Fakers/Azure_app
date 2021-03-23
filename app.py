from flask import *
import logging
from bdd import *
from mailsender import *

app = Flask(__name__)

logging.basicConfig(filename='my_log.txt', level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    logging.info("return to the home page")
    return render_template('home.html') 

@app.route('/submit', methods=['GET','POST'])
def submit():
    logging.info("submit start")
    if request.method == "POST":
        send_mail = request.form['email']
        content = "test"
        go_mail(send_mail,content)
    logging.info("mail successfully send !!")
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0' ,port=4000, debug=True)