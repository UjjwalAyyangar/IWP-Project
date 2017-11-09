from controllers.modules import *
from controllers.utilities import *

class DashboardHandler(RequestHandler):

    """
    class resposible to render the landing page
    route : /
    """

    @coroutine
    @removeslash
    def get(self):
        token = self.get_secure_cookie('token')
        data = {}
        data["loggedin"] = False
        if token:
            _id = untokenizeCokkie(token)
            data = yield db.users.find_one({"_id" : _id})
            if data:
                data["loggedin"] = True

                courses = []
                for course in data["courses"]:
                    ctemp = yield db.courses.find_one({"code" : course[0]})
                    ttemp = yield db.teachers.find_one({"id" : course[1]})
                    fdbk = yield db.feedback.find_one({"uid" : _id, "course_code" : course[0], "fac_id" : str(course[1])})
                    courses.append({"course" : ctemp, "teacher" : ttemp, "fdbk" : fdbk})

                data["courses"] = courses
                self.render("dashboard.html", data = data)
            else:
                self.clear_cookie('token')
                self.redirect("/login?session=False")
        else:
            self.redirect("/login?session=False")
