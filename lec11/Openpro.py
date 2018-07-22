from flask import Flask,request
from pymessenger.bot import Bot
bot=Bot("EAAHWok6dD5UBAPWR7XXk20gYanJupg6XRyPbSJzg6GrQKZARXd0Xm4S67OZC1ZBPvx9CjMzcPpDjwSoLrYlxF4aPwc3mGa7SGRQC8Ju1bPf1Cpo5KMZBH7qxFD6njNfO9EMZBPvVZCODPB2Q4a9G2BBKfwEOOw1DqNOQPQkZBgnFQZDZD")
pop=Flask(__name__)

@pop.route("/",methods=["GET"])
def verify():
    if request.args.get("hub.challenge"):
        return request.args.get("hub.challenge")
    else:
        return "please run "

@pop.route("/",methods=["POST"])
def msg():
    data=request.get_json()
    print(data)
    for entry in data["entry"]:
        for messaging in entry["messaging"]:
            #text=(messaging["message"]["text"])
            text=("is it you??")
            user=(messaging["sender"]["id"])
            bot.send_text_message(user,text)
            bot.send_image_url(user,"https://www.flyingduchess.com/wp-content/uploads/2013/09/535804-1680x1050-e1380228899264.jpg")
            # print(messaging["message"]["text"])
            # print(messaging["sender"]["id"])

    return "Message recieved"

@pop.after_request# for clearing previous cache
def add_header(response):

    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

pop.run(debug=True)
