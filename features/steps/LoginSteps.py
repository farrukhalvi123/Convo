from behave import *

from Utilities.URLs import login


@given("User is on HeroUk App login Page")
def step_impl(context):
    base_url = context.config.userdata.get('base_url', '')
    context.browser.get(f"{base_url}" + login)



@when("User Logs in with {username} and {password}")
def step_impl(context, username, password):
    context.hero.loginpage.user_login(username, password)



@then("User should navigate to dashboard")
def step_impl(context):
    context.hero.loginpage.postlogin()
