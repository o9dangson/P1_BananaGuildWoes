from behave.runner import Context
from selenium import webdriver
from POM.BG_Home import BG_Home
from POM.BG_Account import BG_Account
from POM.BG_Manage import BG_Manage

def before_all(context: Context):
    # We need to add a driver to the context
    context.driver = webdriver.Chrome("utils/Driver/chromedriver.exe")
    # We need to add all POMS to the context
    context.BG_Home = BG_Home(context.driver)
    context.BG_Account = BG_Account(context.driver)
    context.BG_Manage = BG_Manage(context.driver)
    # We add an implicit wait to work with latency issues
    context.driver.implicitly_wait(2)

def after_all(context: Context):
    # This will make sure at the end of a behave test all the drivers are closed
    context.driver.quit()