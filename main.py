from flask import Flask , render_template , session ,request,redirect

app=Flask(__name__)
app.secret_key="super_secret"
@app.route('/')
def index():
    if 'visits' not in session:
        session['visits'] = 0
    if 'counter' not in session:
        session['counter'] = 0
    session['visits'] += 1
    return render_template("index.html",
        visits=session['visits'],
        counter=session['counter'],
    )

@app.route('/increment')
def increment():
    if 'counter' not in session:
        session['counter']=0
    session['counter']+=2
    return redirect('/')
@app.route('/reset')
def reset():
    session['counter']=0
    return redirect('/')

@app.route('/set_increment',methods=['POST'])
def set_increment():
    if 'counter' not in session:
        session['counter']=0
    amount=request.form['amount']
    if amount.lstrip('-').isdigit():
        session['counter']+=int(amount)
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":
 app.run(debug=True,port=5001)