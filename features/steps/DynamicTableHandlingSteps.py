from behave import *
from Utilities.URLs import tables

@given("User is on Tables Page")
def step_impl(context):
    base_url = context.config.userdata.get('base_url', '')
    context.browser.get(f"{base_url}" + tables)



@then("Extract all the table data")
def step_impl(context):
    context.table_data = context.hero.dynamicTablePage.get_table_data()


@then("Verify {lastname} and {firstname} is present in the table")
def step_impl(context, lastname, firstname):
    assert context.hero.dynamicTablePage.verify_table_data(lastname, firstname), \
        f"{firstname} {lastname} not found in the table!"


