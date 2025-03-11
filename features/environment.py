import os
import yaml
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from features.steps.commons import herokuapp
import random


def before_all(context):
    # Get the environment variable to choose environment (default: 'dev')
    environment = os.getenv('ENVIRONMENT', 'dev')  # Default to 'dev' if not set

    # Load the YAML configuration file for the specified environment (only 1 for this project)
    config_path = f'config/config_{environment}.yaml'

    with open(config_path) as f:
        config = yaml.safe_load(f)

    # Update context.config.userdata with the loaded configuration
    context.config.userdata.update(config)

    # Store browser configurations to be used later
    context.browsers = context.config.userdata.get('browsers', [])

    # Ensure that browsers list is not empty
    if not context.browsers:
        raise ValueError("No browsers are configured in the YAML file!")

    # If running in parallel, assign a unique browser per test
    context.browser_name = None


def before_scenario(context, scenario):
    if hasattr(context, 'browser'):
        context.browser.quit()
        del context.browser

    # If running in parallel, pick a browser for this scenario
    if not context.browser_name:
        context.browser_name = context.browsers[0]['name']
        is_ci = os.getenv("CI", "false").lower() == "true"
        headless = is_ci or context.browsers[0].get('headless', False) # This makes sure CICD always runs in headless mode

    # Create WebDriver instance based on the selected browser
    if context.browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless=new')  # Use "--headless=new" for Chrome 109+
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        context.browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        context.browser.maximize_window()

    elif context.browser_name == "firefox": # change 'chrome' to 'firefox' in config_dev.yaml file to run your test on Firefox
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument('--headless')
        context.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        context.browser.maximize_window()

    context.browser.implicitly_wait(2)  # Set implicit wait if needed
    context.hero = herokuapp(context.browser)

    # Tag the scenario with the browser name, if desired
    scenario.tags.append(context.browser_name)


def after_scenario(context, scenario):
    if scenario.status == "failed":  # Check if the test failed. If test fails this takes screenshot globally
        if hasattr(context, "browser"):
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)  # Create directory if it doesn't exist

            screenshot_path = os.path.join(screenshot_dir, f"{scenario.name}.png")
            context.browser.save_screenshot(screenshot_path)
            print(f"Screenshot saved: {screenshot_path}")  # Log the screenshot path

    if hasattr(context, "browser"):
        context.browser.close()
        context.browser.quit()



