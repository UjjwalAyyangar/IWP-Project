"""
module to storing all the routes
"""

from controllers import *

routes = [
    (
        r"/",
        index.IndexHandler
    ),
    (
        r"/login",
        login.LoginHandler
    ),
    (
        r"/about",
        about.AboutHandler
    ),
    (
        r"/contact",
        contact.ContactHandler
    ),
    (
        r"/dashboard",
        dashboard.DashboardHandler
    ),
    (
        r"/logout",
        logout.LogoutHandler
    ),
    (
        r"/submitfdbk",
        feedback.FeedbackHandler
    ),
    (
        r"/teachers",
        teachers.TeachersHandler

    ),
]
