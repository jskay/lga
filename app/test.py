import models


for lgad, jhs in models.session.query(models.Schedule.lgad, models.Schedule.jhs) .\
                filter(models.Schedule.day =='WKD', models.Schedule.lgad > '23:45') .\
                limit(10):

    print lgad, jhs



#for lgad, jhs in session.query(Schedule.lgad, Schedule.jhs) .\
#                filter(Schedule.day =='WKD', Schedule.lgad > '21:30', Schedule.lgad < '22:31'):

#   print lgad, jhs
