from controllers.modules import *
from controllers.utilities import *

class ContactHandler(RequestHandler):

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
            print(data)
            if data:
                data["loggedin"] = True
            else:
                data = {}
                data["loggedin"] = False
        self.render("contact.html", data = data)
