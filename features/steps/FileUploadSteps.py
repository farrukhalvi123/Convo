from behave import *

from Utilities.URLs import upload


@given("User is on File Upload Page")
def step_impl(context):
    base_url = context.config.userdata.get('base_url', '')
    context.browser.get(f"{base_url}" + upload)


@when("User Uploads the file")
def step_impl(context):
    context.hero.upload.upload_file()


# @then("User Verifies correct file is uploaded with filename")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: Then User Verifies correct file is uploaded with filename')