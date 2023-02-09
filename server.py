import cherrypy
import win32com.client
import random

qng = win32com.client.Dispatch("QWQNG.QNG")


class RandomBox(object):


    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        deviceId = qng.DeviceId
        return {"deviceid": deviceId}
    

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def fived(self):
        random_numbers = abs(qng.RandInt32)
        nums_list = list(map(int, str(random_numbers)))
        output_numbers = random.sample(nums_list, k=5)

        return {"draw_number": output_numbers}
    

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def threed(self):
        random_numbers = abs(qng.RandInt32)
        nums_list = list(map(int, str(random_numbers)))
        output_numbers = random.sample(nums_list, k=3)

        return {"draw_number": output_numbers}


    @cherrypy.expose
    @cherrypy.tools.json_out()
    def fast3(self):
        random_numbers = abs(qng.RandInt32)
        # if(random_numbers is None):
        nums_list = list(map(int, str(random_numbers)))
        output_numbers = random.sample(range(1, 7), k=3)

        return {"draw_number": output_numbers}


    @cherrypy.expose
    @cherrypy.tools.json_out()
    def pc_28(self):
        random_numbers = abs(qng.RandInt32)
        nums_list = list(map(int, str(random_numbers)))
        output_numbers = random.sample(nums_list, k=3)

        return {"draw_number": output_numbers}


    @cherrypy.expose
    @cherrypy.tools.json_out()
    def pk_10(self):
        # random_numbers = abs(qng.RandInt32)
        output_numbers = random.sample(range(1, 11), 10)
        
        return {"draw_number": output_numbers}


    @cherrypy.expose
    @cherrypy.tools.json_out()
    def eleven5(self):
        random_numbers = abs(qng.RandInt32)
        # nums_list = list(map(int, str(random_numbers)))
        output_numbers = random.sample(['01', '02', '03', '04', '05', '07', '08', '09', '10', '11'], 5)

        return {"draw_number": output_numbers}

    
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def fortynine7(self):
        random_numbers = abs(qng.RandInt32)
        # nums_list = list(map(int, str(random_numbers)))
        output_numbers = random.sample(range(1, 50), 7)

        return {"draw_number": output_numbers}




if __name__ == '__main__':
    cherrypy.quickstart(RandomBox())