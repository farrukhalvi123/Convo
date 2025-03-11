Feature: Handling Java Script Pop Ups
  @Regression
  Scenario Outline: Handle all 3 JS Alerts
    Given User is on Pop Up Alerts Page
    When User Clicks on pop up <type>
    Then Pop JS alert Pop up appears and User Handles it
    Examples:
    |type|
    |alert|
    |confirm     |
    |prompt      |
