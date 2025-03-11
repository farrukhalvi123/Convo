Feature: Dynamic Tables Handling Test Cases
  @Regression
  Scenario Outline:
    Given User is on Tables Page
    Then Extract all the table data
    Then Verify <lastname> and <firstname> is present in the table
    Examples:
    |lastname|firstname|
    | Doe       |  Jason       |
