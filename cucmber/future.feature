Feature: Calculator
    Scenario: Add6
        Given we call the add function
        When we give the function an argumentof size 6
        Then we should get 12

    Scenario: Add10
        Given we call the add function
        When we give the function an argumentof size 10
        Then we should get 20

    Scenario: div_two_numbers
        Given we call the div function
        When we give arguments 90 and 10
        Then we get 9