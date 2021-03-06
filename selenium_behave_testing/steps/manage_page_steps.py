import time
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@given(u'I am on the Account page')
def step_on_account_page(context):
    context.driver.get("http://localhost:5000/")
    context.BG_Home.get_username_form().send_keys("manager")
    context.BG_Home.get_password_form().send_keys("Password123")
    context.BG_Home.get_login_btn().click()

@when(u'I click on the Manage Pending Request Page')
def step_on_manage_request_page(context):
    context.BG_Account.get_manage_button().click()

@then(u"I should see all requests that aren't mine")
def step_all_pending_requests(context):
    userId = "2"
    if (len(context.BG_Manage.get_list_of_user_id_input())> 0):
        list_of_requests = context.BG_Manage.get_list_of_user_id_input()
        for reqs in list_of_requests:
            assert reqs.get_attribute("value") != userId
    else:
        assert True
    context.BG_Account.get_logout_button().click()

@when (u'I click the Accept Button')
def step_click_on_accept_request(context):
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'user-id-request')))
    if (len(context.BG_Manage.get_list_of_acc_rej_btn())> 0):
        context.size_of_pending_list = len(context.BG_Manage.get_list_of_acc_rej_btn())
        list_of_buttons = context.BG_Manage.get_list_of_acc_rej_btn()
        for button in list_of_buttons:
            button.click()
            break

@then (u'It should no longer be on my pending requests')
def step_check_to_see_if_pending_removed(context):
    time.sleep(3)
    curr_len_of_pending = len(context.BG_Manage.get_list_of_acc_rej_btn())
    assert curr_len_of_pending < context.size_of_pending_list
    context.BG_Account.get_logout_button().click()