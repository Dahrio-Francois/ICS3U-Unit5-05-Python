#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: June 2022
# This program prints out your full address card


def code(
    full_name,
    street_number,
    street_name,
    city,
    province,
    postal_code,
    apartment_number=None,
):
    # return code

    code = full_name
    if apartment_number != None:
        code = code + "\n" + apartment_number + " - "
    code = (
        "\n"
        + code
        + "\n"
        + street_number
        + " "
        + street_name
        + "\n"
        + city
        + " "
        + province
        + "  "
        + postal_code
    )

    return code


def main():
    # gets a users address info and prints out an address card
    apartment_number = None

    full_name = input("Enter your full name: ")
    question = input("Do you live in an apartment? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        apartment_number = input("Enter your apartment number: ")
    street_number = input("Enter your street number: ")
    street_name = input("Enter your street name and type: ")
    city = input("Enter your city: ")
    province = input("Enter your province (As an abbreviation Ex. ON, BC): ")
    postal_code = input("Enter your postal_code: ")

    if apartment_number != None:
        address = code(
            full_name,
            street_number,
            street_name,
            city,
            province,
            postal_code,
            apartment_number,
        )
    else:
        address = code(
            full_name, street_number, street_name, city, province, postal_code
        )

    print(address.upper())


if __name__ == "__main__":
    main()
