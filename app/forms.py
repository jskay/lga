from flask.ext.wtf import Form
from wtforms import TextField, SelectField
from wtforms.validators import Required

class TripInfo(Form):
    day = SelectField('Day', choices=[('WKD', 'Weekday'),
                                      ('SAT', 'Saturday'),
                                      ('SUN', 'Sunday')])
    time = SelectField('Departure time', choices=[('08:00', '8am'),
                                                  ('09:00', '9am'),
                                                  ('10:00', '10am'),
                                                  ('11:00', '11am'),
                                                  ('12:00', 'Noon'),
                                                  ('13:00', '1pm'),
                                                  ('14:00', '2pm'),
                                                  ('15:00', '3pm'),
                                                  ('16:00', '4pm'),
                                                  ('17:00', '5pm'),
                                                  ('18:00', '6pm'),
                                                  ('19:00', '7pm'),
                                                  ('20:00', '8pm'),
                                                  ('21:00', '9pm'),
                                                  ('22:00', '10pm'),
                                                  ('23:00', '11pm'),                                            
                                                  ('00:00', 'Midnight')])
    depart = SelectField('Departing from', choices=[('lgab', 'LGA Terminal B'),
                                                    ('lgad', 'LGA Terminal D')])
    dest = SelectField('Destination', choices=[('jhs', 'E train - Jackson Heights, Roosevelt Avenue')])
    
