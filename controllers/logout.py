from controllers.modules import *
from controllers.utilities import *

class LogoutHandler(RequestHandler):

    """
    class resposible to render the landing page
    route : /
    """

    @coroutine
    @removeslash
    def get(self):
        self.clear_cookie('token')
        self.redirect("/")
