import requests
from datetime import datetime, timedelta
from xml.dom import minidom

class api:
    def skill_check(self,codes):
        r = requests.get('https://api.eveonline.com/char/SkillQueue.xml.aspx', params=codes)
        print r.text
        xmldoc = minidom.parseString(r.text)
        skills = xmldoc.getElementsByTagName('row')
        lastskill = len(skills) -1
        endtime = skills[lastskill].attributes['endTime'].value

        currenttime = xmldoc.getElementsByTagName('currentTime')[0].firstChild.nodeValue

        print 
        print 'CURRENT TIME: ' + currenttime
        print 'SKILL END TIME: ' + endtime

        c_time = datetime.strptime(currenttime, "%Y-%m-%d %H:%M:%S")
        t_time = c_time + timedelta(days=1)
        s_time = datetime.strptime(endtime, "%Y-%m-%d %H:%M:%S")

        if t_time > s_time:
            time_delta = (t_time - s_time) 
            print 'CHANGE NOW!!!!!!'
            print time_delta
        if s_time > t_time:
            time_delta = (s_time - t_time) 
            print 'SAFE'
            print time_delta
