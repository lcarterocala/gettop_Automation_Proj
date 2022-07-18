# Created by carte at 7/17/2022
Feature: Tests adding and modifying cart items


  Scenario: Adding to cart and manipulating item number
    Given Open home page
    When ipad is selected from menu bar
    And Product is selected
    And Plus and minus used to manipulate cart item quantity
    And Cart number of items are manually entered
    And Add to cart button is clicked
    Then Use arrows to browse through other products
    And Verify product stock status

