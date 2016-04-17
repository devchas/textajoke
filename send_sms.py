from twilio.rest import TwilioRestClient
from flask import Flask, url_for, request, render_template, send_from_directory, redirect
import re
import random
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/send', methods=['POST'])
def send(): 
	if request.method == 'POST':
		num = request.form['number']
		if (isValPhone(num)):
			num = getClnNum(num)
			account_sid = "[ACCOUNT]"
			auth_token = "[TOKEN]"
			client = TwilioRestClient(account_sid, auth_token)
		 	
			message = client.messages.create(to="+1" + num, from_="+19143713084", body=getJoke())

			return redirect(url_for('index'))
		else:
			return 'Looks like something went wrong.  Try typing in that number again.'

def isValPhone(num):
	reg = r'(\(?[0-9]{3}[).\s-]?\s?[0-9]{3}[.\s-]?[0-9]{4})'
	if re.match(reg, num):
		return True
	else:
		return False

def getClnNum(num):
	numStr = ""
	numReg = '[0-9]'
	for i in num:
		if re.match(numReg, i):
			numStr += i
	return numStr

def getJoke():
	joke = [
		'A man walks into a zoo and the only animal in the zoo is a a dog. It\'s a shitszu.',
		'Where did Noah keep his bees? In the ARK HIVES!',
		'What did the pirate say when he turned 80? Aye matey!!!',
		'A Mexican magician tells the audience he will disappear on the count of 3.  He says UNO, DOS... and he disappeared without a tres.',
		'If I had a dollar for every girl that found me unattractive, they would eventually find me attractive.',
		'A recent study has found that women who carry a little extra weight live longer than the men who mention it.',
		'When an employment application asks who is to be notified in case of emergency, I always write, "A very good doctor".',
		'I\'d tell you a chemistry joke but I know I wouldn\'t get a reaction.',
		'My first child has gone off to college and I feel a great emptiness in my life. Specifically, in my checking account.',
		'I\'m against picketing, but I don\'t know how to show it.',
		'You know, I\'m sick of following my dreams, man. I\'m just going to ask where they\'re going and hook up with \'em later.',
		'My friend asked me if I wanted a frozen banana, I said "no, but I want a regular banana later, so ... yeah".',
		'I haven''t slept for ten days, because that would be too long.',
		'Is a hippopotamus a hippopotamus, or just a really cool Opotamus?',
		'Rice is great if you\'re really hungry and want to eat two thousand of something.',
		'My belt holds my pants up, but the belt loops hold my belt up. I don\'t really know what\'s happening down there. Who is the real hero?',
		'The dyslexic devil worshipper sold his soul to Santa.',
		'What did Jay-Z call his girlfriend before they got married? Feyonce.',
		'What do you call dangerous precipitation? A rain of terror.',
		'What\'s the best part about living in Switzerland? Not sure, but the flag is a big plus.'
	]
	n = random.randrange(len(joke) - 1)
	return(joke[n])

if __name__ == '__main__':
    #app.debug = True
    app.run()