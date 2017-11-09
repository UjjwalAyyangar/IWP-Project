from controllers.modules import *
from controllers.utilities import *

class LoginHandler(RequestHandler):

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
                self.redirect("/dashboard")
            else:
                data = {}
                data["loggedin"] = False
                self.render("login.html", data = data)
        else:
            self.render("login.html", data = data)

    @coroutine
    @removeslash
    def post(self):
        reg_no = self.get_argument("regno")
        pswd = self.get_argument("pswd")

        data = yield db.users.find_one({"regno" : reg_no, "password" : pswd})
        print(data)
        if data:
            token = tokenizeCokkie(data["_id"])
            self.set_secure_cookie('token', token)
            self.redirect("/dashboard")
        else:
            self.redirect("/login?credentials=False")
