from routes import routes
from controllers.modules import *

define("port",
  default = 8000,
  help = "Contact the One who made it Contact Ujjwal :P",
  type = int)

#overloading the Application
class ApplicationHandler(Application):

	def __init__(self):

		handlers = routes.routes
		settings = dict(
                    template_path = join(dirname(__file__), "templates"),
                    static_path = join(dirname(__file__), "static"),
                    debug = True,
                    cookie_secret = "35an18y3-u12u-7n10-4gf1-102g23ce04n6"
                    )
		Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
    options.parse_command_line()
    http_server = HTTPServer(ApplicationHandler())
    http_server.listen(options.port)
    IOLoop.instance().start()
