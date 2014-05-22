from flask import Flask, render_template, flash, redirect, g, request
from app import app
from forms import TripInfo
import models
import sqlite3


def connect_db():
  return sqlite3.connect(app.config['DATABASE'])
 
@app.route('/', methods = ['GET', 'POST'])
def home():
  form = TripInfo()
  if request.method == 'POST':
      return redirect('/trip')
  return render_template('home.html',
          title = 'Bus From LGA',
          form = form)

@app.route('/mta')
def mta():
  return render_template('mta.html')

@app.route('/q70')
def q70():
  return render_template('q70.html')

@app.route('/traffic')
def traffic():
  return render_template('traffic.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/trip', methods = ['GET', 'POST'])
def trip():
  form = TripInfo()
  g.db = connect_db()
  cur = g.db.execute('SELECT "lgad", "lgab", "jhs" FROM q70 WHERE "lgad" >= "' + (form.time.data) + '" LIMIT 5')
  trip = [dict(lgad=col[0], lgab=col[1], jhs=col[2])
          for col in cur.fetchall()]
  g.db.close    
  return render_template('trip.html', form = form, trip = trip)

   


