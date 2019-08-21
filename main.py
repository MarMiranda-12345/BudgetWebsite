import webapp2
import jinja2
import os
from google.appengine.api import users
from google.appengine.ext import ndb


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



#this is not complete
# everything below is supposed to be the data
class SimpleBudgetUser(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()

class SignUpPageHandler(webapp2.RequestHandler):
    def get(self):
        user = user.get_current_user()
        #if the user logged in
        if user:
            email_address = user.nickname()
            Simple_Budget_User = SimpleBudgetUser.get_by_id(user.user_id())
            sign_link_html = '<a href="%s">signout</a>' % (
                users.create_logout_url('/logInPage'))
        #if the user has previously been to our site
            if Simple_Budget_User:
                self.response.write('''Welccome %s %s (%s)! <br> %s <br>''' % (SimpleBudgetUser.first_name, SimpleBudgetUser.last_name, email_address, signout_link_html))
            #if the user hasnt bee to our site
            else:
                self.response.write('''Welcome to our site, %s! Please sign up! <br>
                <form method ="post"action="/">
                <input type="text" name="first_name">
                <input type="text" name="last_name">
                <input type="submit">
                <form<br> %s <br>
                ''' % (email_address, signout_link_html))
        #otherwise the user isnt logged in
        else:
            self.response.write('''
                please log in to use our site! <br>
                <a> href="%s">Sign in/a>''' % (user.create_login_url('/logInPage')))

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
            enterInfoTemplate = the_jinja_env.get_template("templates/EnterInfo.html")
            self.response.write(enterInfoTemplate.render())

class SendInfoHandler (webapp2.RequestHandler):
        def get(self):
            retrieveInfoTemplate = the_jinja_env.get_template("templates/EnterInfoResult.html")
            self.response.write(retrieveInfoTemplate.render())


def post(self):
    user = user.get_current_user()
    if not user:
        self.error(500)
        return
    Simple_Budget_User = SimpleBudgetUser(
        first_name=self.request.get('first_name'),
        last_name=self.request.get('last_name'),
        id=user.user_id())
    Simple_Budget_User.put()
    self.response.write('Thanks for signing up, %s!' %
        Simple_Budget_User.first_name)

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/logInPage', LogInPageHandler),
    ('/signUpPage', SignUpPageHandler),
    ('/info', EnterInfoHandler),
    ('/budget', SendInfoHandler)
], debug = True)
