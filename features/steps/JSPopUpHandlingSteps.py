import time

from behave import *

from Utilities.URLs import jsalerts


@given("User is on Pop Up Alerts Page")
def step_impl(context):
    base_url = context.config.userdata.get('base_url', '')
    context.browser.get(f"{base_url}" + jsalerts)


@when("User Clicks on pop up {type}")
def step_impl(context, type):
    context.hero.jshandling.popup_appear(type)


@then("Pop JS alert Pop up appears and User Handles it")
def step_impl(context):
    context.hero.jshandling.handling_popup()