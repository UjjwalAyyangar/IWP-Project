from controllers.modules import *
from controllers.utilities import *

class FeedbackHandler(RequestHandler):

    """
    class resposible to render the landing page
    route : /
    """

    @coroutine
    @removeslash
    def post(self):

        token = self.get_secure_cookie('token')
        _id = untokenizeCokkie(token)
        course_id = self.get_argument("course_id")
        fac_id = self.get_argument("fac_id")
        concepts = int(self.get_argument("q1"))
        allTopics = int(self.get_argument("q2"))
        weak = int(self.get_argument("q3"))
        avail = int(self.get_argument("q4"))
        tuts = int(self.get_argument("q5"))
        avg = (concepts + allTopics + weak + avail + tuts)/5

        problems = []
        if allTopics < 3:
            problems.append("You felt that not all the topics were coverted properly in the class")
        

        if  concepts < 3 :
            problems.append("You found it difficult to understand the concepts in the class ")
        

        if weak < 3 :
            problems.append("You believe that the teacher should pay more attention to weak students")
        

        if avail < 3 :
            problems.append("You found it difficult to find the teacher after the classes")
        

        if tuts < 3 :
            problems.append("You think that the teacher should give weekly tutorials regularly")
        




        yield db.feedback.insert({
            "uid" : _id,
            "course_code" : course_id,
            "fac_id" : fac_id,
            "fdbk" : {
                "q1" : concepts,
                "q2" : allTopics,
                "q3" : weak,
                "q4" : avail,
                "q5" : tuts,
                "avg" : avg,
                "problems":problems

            }
        })
        self.redirect("/dashboard")
