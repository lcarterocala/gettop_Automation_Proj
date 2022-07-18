# Created by carte at 7/16/2022
Feature: Tests gettop site filter and sorting features


  Scenario: Verify Price Filter CTA and Reset function
    Given Open home page
    When ipad is selected from menu bar
    And Filter bar is adjusted
    And Filter button is clicked
    Then Close the applied Min filter
    And Close the applied Max filter
    And Verify price filter has been reset
