import logging
import cv2
import pyfirmata_test
import os
import movement 

from flask import Flask
from flask_ask import Ask, request, session, question, statement

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

@ask.launch
def launch():
    speech_text = 'Hi, I am Rocky. I can draw things.'
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)

@ask.intent('GpioIntent', mapping = {'status':'status'})
def Gpio_Intent(status,room):
    if status == 'high':
        return statement('turning {} lights'.format(status))
    elif status == 'low':
        return statement('turning {} lights'.format(status))
    else:
        return statement('Sorry not possible.')

@ask.intent('DrawIntent', mapping = {'item':'item'})
def Draw(item):
    img = cv2.imread('images/' + item + '.jpg', 0)
    points = movement.image_to_direction(img)
    pyfirmata_test.move_rock(points)
    return statement('I will draw {}'.format(item))
    

@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can say hello to me!'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)


@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
