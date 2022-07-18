# Created by carte at 7/9/2022
Feature: Tests for gettop searches
  # Enter feature description here

  Scenario: Verify user can search by topic in search bar
    Given Open home page
    When Mouse hover on search icon
    And Search for ipad
    Then Click on search icon
    And Verify search results for ipad

  Scenario: Verify footer features are present and functional
    Given Open home page
    Then Verify footer shows Best Selling, Latest, Top Rated categories
    And Verify products in footer have price, name, star-rating
    And Verify copyright is present in the footer
    And Verify product category links in footer are working
    And Verify presence and function of go back to top button


