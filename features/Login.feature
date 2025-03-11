Feature: Create Test Scenarios for Login
  Scenario Outline: Login Test Case
    Given User is on HeroUk App login Page
    When User Logs in with <username> and <password>
    Then User should navigate to dashboard
    Examples:
    |username|password|
    |tomsmith|SuperSecretPassword!|
    |  tom      |      Super              |