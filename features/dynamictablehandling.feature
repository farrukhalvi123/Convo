Feature: Dynamic Tables Handling Test Cases
  Scenario Outline:
    Given User is on Tables Page
    Then Extract all the table data
    Then Verify <lastname> and <firstname> is present in the table
    Examples:
    |lastname|firstname|
    | Doe       |  Jason       |
    |  Alvi         |   Farrukh              |
    # failing this case deliberately 
