import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPageHandler(webapp2.requestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(result_template.render())

class LogInPageHandler(webapp2.requesthandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/logInPage.html')
        self.response.write(result_template.render())

class SignUpPageHandler(webapp2.requesthandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/logInPage.html')
        self.response.write(result_template.render())
        def post(self):
            form




app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/logInPage', LogInPageHandler),
    ('/signUpPage', SignUpPageHandler)
], debug = True)
