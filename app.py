from flask import Flask, render_template,request
import embedchainbot as bot


app= Flask(__name__)



#homepage 
@app.route('/')
def homepage():
    return render_template('index.htm')


#Uploading and training embedchain bot on the files same time and
# saving it into file folder in static/FILE
@app.route('/', methods=['POST'] )
def upload():
    if request.method == 'POST':
         # GET the list of files from webpage
         files=request.files.getlist("file")
         #iterate for each file in the files list and save them
         for file in files:
             bot.train("file")
             file.save('static/FILE/'+str(file.filename))
    return render_template('index.htm')
         

#get response of our query from the embedchain bot
@app.route("/get")
def get_bot_response():
    userText= request.args.get('msg')
    bot_response=bot.query(userText)
    return bot_response


if __name__=="__main__":
    app.run()
