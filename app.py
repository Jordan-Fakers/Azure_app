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
    send_mail = request.form.get('email')
    data = select_from_db()
    check_mail = go_mail(send_mail,data)
    if check_mail == "success" :
        logging.info("mail successfully send !!")
        return succesroad()
    else:
        logging.info("Something went Wrong")
        return failroad()

@app.route('/succes')
def succesroad():
    return render_template('succes.html')

@app.route('/fail')
def failroad():
    return render_template('fail.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0' ,port=4000, debug=True)