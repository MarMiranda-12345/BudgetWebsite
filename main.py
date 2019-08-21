import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(result_template.render())

class LogInPageHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/logInPage.html')
        self.response.write(result_template.render())

class SignUpPageHandler(webapp2.RequestHandler):
    def post(self):
        result_template = the_jinja_env.get_template('templates/SignUpPageHandler.html')
        user_name = self.request.get('username')
        Pass_Word = self.request.get('password')
        new_dict = {
        "username": user_name,
        "password": pass_Word
    }
        self.response.write(result_template.render(new_dict))

class EnterInfoHandler (webapp2.RequestHandler):
        def get(self):
            enterInfoTemplate = the_jinja_env.get_template("templates/welcome.html")
            self.response.write(enterInfoTemplate.render())

class SendInfoHandler (webapp2.RequestHandler):
        def get(self):
            retrieveInfoTemplate = the_jinja_env.get_template("templates/result.html")
            self.response.write(retrieveInfoTemplate.render())


app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/logInPage', LogInPageHandler),
    ('/signUpPage', SignUpPageHandler),
    ('/budget', SendInfoHandler)
], debug = True)
