from flask import Flask, request, render_template, send_from_directory
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
app = Flask(__name__)
with open('file.txt','r') as file:
    conversation = file.read()
print(conversation)
bott = ChatBot("Root5 Resume ChatBot")
trainer2 = ListTrainer(bott)
trainer2.train([    "Hey",
    "Hi there!",
    "Hi",
    "Hi!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "What is your name?", "My name is Root5 Resume ChatBot",
    "Who created you?", "Venkatasubramani",
    "Tell me about yourself",
    "My name is Venkatasubramani Karthikeyan. I am a machine learning engineer and a web developer",
    "Contact",
    "Email : venkykasprov@gmail.com, Mobile number : +91 9994329789 Location : Ranipet, Tamilnadu",
    "Education",
    "Bachelor of Engineering (B.E), Electricals & Engineering\n Sri Sairam Engineering College'\n'2014 - 2018 '\n'CGPA: 7.89/10 '\n'Senior Secondary (XII), DAV BHEL SCHOOL Ranipet (CBSE board) Year of completion: 2014 Percentage: 86.20% Secondary (X) DAV BHEL SCHOOL (CBSE board) Year of completion: 2012 grade: 8.4/10",
    "Projects",
    ])
trainer = ChatterBotCorpusTrainer(bott)
trainer.train("chatterbot.corpus.english")
#trainer2.train(["Thank You","Welcome"])


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    name = "Venkatasubramani Karthikeyan"
    return render_template("index.html",name = name)

@app.route("/home")
def home():
    name = "Venkatasubramani Karthikeyan"
    return render_template("index.html",name = name)

@app.route("/edu")
def edu():
    name = "Venkatasubramani Karthikeyan"
    return render_template("edu.html",name = name)

@app.route("/exp")
def exp():
    name = "Venkatasubramani Karthikeyan"
    return render_template("exp.html",name = name)

@app.route("/skillset")
def skillset():
    name = "Venkatasubramani Karthikeyan"
    return render_template("skillset.html",name = name)

@app.route("/hobbies")
def hobbies():
    name = "Venkatasubramani Karthikeyan"
    return render_template("hobbies.html",name = name)

@app.route("/edu_exp")
def venky():
    return render_template("edu_exp.html")

@app.route("/get")
def get_bot_response():
    print(request.args.get('msg'))
    userText = request.args.get('msg')
    return str(bott.get_response(userText))

# @app.route('/files/<path:filename>', methods=['GET', 'POST'])
# def download(filename):
#     return send_from_directory(directory=os.getcwd()+"/files", filename="/venky_resume.pdf")

# @app.route("/files/Venky_resume.pdf")
# def DownloadLogFile ():
#     try:
#         return send_file("/static/Venky_resume.pdf", as_attachment=True)
#     except Exception as e:
#         self.log.exception(e)
#         self.Error(400)

@app.route('/static/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    static = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=static, filename=filename)

# @app.route('/download')
# def downloadFile ():
#     #For windows you need to use drive name [ex: F:/Example.pdf]
#     path = "/static/Venky_resume.pdf"
#     return send_file(path, as_attachment=True)
