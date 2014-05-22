#import sqlalchemy

#from sqlalchemy import create_engine
#engine = create_engine('sqlite:///database/nyctransit', echo=True)

#from sqlalchemy.orm import sessionmaker
#Session = sessionmaker(bind=engine)

#from sqlalchemy.ext.declarative import declarative_base
#Base = declarative_base()

#from sqlalchemy import Column, Text #, Time

from app import db



class Schedule(db.Model):
    
    __tablename__ = 'q70'

    key = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Text) 
    route = db.Column(db.Text) # Q70 bus stops
    woodn = db.Column(db.Text) # Woodside Northbound (7 train, LIRR)
    jhn = db.Column(db.Text)   # Jackson Heights Northbound (E, 7 train)
    lga1 = db.Column(db.Text)  # LGA parking lot 1
    lgad = db.Column(db.Text)  # LGA Terminal D - Additional stop not on MTA schedule
    lgab = db.Column(db.Text)  # LGA Terminal B
    jhs = db.Column(db.Text)   # Jackson Heights Southbound (E, 7 train)
    woods = db.Column(db.Text) # Woodside Southbound (7 train, LIRR)

    #def __init__(self, day, route, woodn, jhn, lga1, lgad, lgab, jhs, woods):
        #self.day = day
        #self.route = route
        #self.woodn= woodn
        #self.jhn = jhn
        #self.lga1 = lga1
        #self.lgad = lgad
        #self.lgab = lgab
        #self.jhs = jhs
        #self.woods = woods

    #__tablename__ = "subway" NYC subway schedule TK
        

#session = Session()

#print 'Departure/Arrival times from LGA Terminal D to E train - Jackson Heights'

#for lgad, jhs in session.query(Schedule.lgad, Schedule.jhs) .\
#                filter(Schedule.day =='WKD', Schedule.lgad < '11:31'):

#    print lgad, jhs

#for lgad, jhs in session.query(Schedule.lgad, Schedule.jhs) .\
#                filter(Schedule.day =='WKD', Schedule.lgad > '21:30', Schedule.lgad < '22:31'):

#   print lgad, jhs

#print 'Q70 bus options for flight arrival at 9:30 pm, LGA Terminal D, Weekday'








