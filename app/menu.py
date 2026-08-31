# from .utils import (
#     valid_email,
#     valid_phone,
#     valid_id_number
# )

# from app.services import (
#     user_exists,
#     id_exists,
#     email_exists,
#     register_user
# )

# from .integrations.nrb_api import lookup_identity


# def menu(text, phone):

#     # Split the USSD text
#     data = text.split("*") if text else []

#     # =========================================================
#     # MAIN MENU
#     # =========================================================

#     if len(data) == 0:

#         return """CON Welcome to Ardhisasa

# 1. Register
# 2. Search
# 3. Customer Care
# 4. Exit
# """

#     # =========================================================
#     # REGISTER
#     # =========================================================

#     if data[0] == "1":

#         # -----------------------------------------------------
#         # SELECT REGISTRATION TYPE
#         # -----------------------------------------------------

#         if len(data) == 1:

#             return """CON Select Registration Type

# 1. Individual
# 2. Company
# """

#         # =====================================================
#         # INDIVIDUAL REGISTRATION
#         # =====================================================

#         if data[1] == "1":

#             # -------------------------------------------------
#             # SELECT IDENTIFICATION TYPE
#             # -------------------------------------------------

#             if len(data) == 2:

#                 return """CON Select Identification Type

# 1. National ID
# 2. Passport
# 3. Alien ID
# """

#             # -------------------------------------------------
#             # ID TYPE
#             # -------------------------------------------------

#             if len(data) == 3:

#                 if data[2] not in ["1", "2", "3"]:

#                     return """CON Invalid identification type.

# 1. National ID
# 2. Passport
# 3. Alien ID
# """

#                 return (
#                     "CON Kindly provide ID number "
#                     "as it appears on the ID:"
#                 )

#             # -------------------------------------------------
#             # ID NUMBER
#             # -------------------------------------------------

#             if len(data) == 4:

#                 id_number = data[3].strip()

#                 if not valid_id_number(id_number):

#                     return (
#                         "CON Kindly provide ID number "
#                         "as it appears on the ID:"
#                     )

#                 # Check if already registered
#                 if id_exists(id_number):

#                     return (
#                         "END This ID number is already registered."
#                     )

#                 return (
#                     "CON Kindly provide ID serial number "
#                     "as it appears on the ID:"
#                 )

#             # -------------------------------------------------
#             # SERIAL NUMBER
#             # -------------------------------------------------

#             if len(data) == 5:

#                 serial_no = data[4].strip()

#                 if not serial_no:

#                     return (
#                         "CON Kindly provide ID serial number "
#                         "as it appears on the ID:"
#                     )

#                 return (
#                     "CON Kindly provide first name "
#                     "as it appears on the ID:"
#                 )

#             # -------------------------------------------------
#             # FIRST NAME
#             # -------------------------------------------------

#             if len(data) == 6:

#                 first_name = data[5].strip()

#                 if not first_name:

#                     return (
#                         "CON Kindly provide first name "
#                         "as it appears on the ID:"
#                     )

#                 return (
#                     "CON Kindly provide other names "
#                     "as they appear on the ID:"
#                 )

#             # -------------------------------------------------
#             # OTHER NAMES
#             # -------------------------------------------------

#             if len(data) == 7:

#                 other_names = data[6].strip()

#                 # Other names can be optional.
#                 # If there are no other names, user can enter NONE.

#                 if not other_names:

#                     return (
#                         "CON Kindly provide other names "
#                         "as they appear on the ID:"
#                     )

#                 return (
#                     "CON Kindly provide surname "
#                     "as it appears on the ID:"
#                 )

#             # -------------------------------------------------
#             # SURNAME
#             # -------------------------------------------------

#             if len(data) == 8:

#                 surname = data[7].strip()

#                 if not surname:

#                     return (
#                         "CON Kindly provide surname "
#                         "as it appears on the ID:"
#                     )

#                 return """CON Select gender

# 1. Male
# 2. Female
# """

#             # -------------------------------------------------
#             # GENDER
#             # -------------------------------------------------

#             if len(data) == 9:

#                 gender_input = data[8].strip()

#                 if gender_input not in ["1", "2"]:

#                     return """CON Invalid selection.

# 1. Male
# 2. Female
# """

#                 return (
#                     "CON Kindly provide mother's full name "
#                     "as it appears on the ID:"
#                 )

#             # -------------------------------------------------
#             # MOTHER'S FULL NAME
#             # -------------------------------------------------

#             if len(data) == 10:

#                 mother_name = data[9].strip()
#                 print("MOTHER NAME RECEIVED:", repr(mother_name))
#                 if not mother_name:

#                     return (
#                         "CON Kindly provide mother's full name "
#                         "as it appears on the ID:"
#                     )

#                 return """CON Select nationality

# 1. Kenyan
# 2. Other
# """

#             # =================================================
#             # NATIONALITY + NRB VERIFICATION
#             # =================================================

#             if len(data) == 11:

#                 nationality_input = data[10].strip()

#                 if nationality_input not in ["1", "2"]:

#                     return """CON Invalid selection.

# 1. Kenyan
# 2. Other
# """

#                 # ---------------------------------------------
#                 # Convert USSD selections to NRB values
#                 # ---------------------------------------------

#                 gender = (
#                     "M"
#                     if data[8].strip() == "1"
#                     else "F"
#                 )

#                 nationality = (
#                     "KENYAN"
#                     if nationality_input == "1"
#                     else "OTHER"
#                 )

#                 # ---------------------------------------------
#                 # Collect all identity information
#                 # ---------------------------------------------

#                 id_number = data[3].strip()
#                 serial_no = data[4].strip()
#                 first_name = data[5].strip()
#                 other_names = data[6].strip()
#                 surname = data[7].strip()
#                 mother_full_name = data[9].strip()

#                 # ---------------------------------------------
#                 # NRB VERIFICATION
#                 # ---------------------------------------------

#                 try:

#                     nrb_response = verify_identity(
#                         id_number=id_number,
#                         serial_no=serial_no,
#                         first_name=first_name,
#                         other_names=other_names,
#                         surname=surname,
#                         gender=gender,
#                         mother_full_name=mother_full_name,
#                         nationality=nationality
#                     )

#                 except Exception as e:

#                     print("NRB ERROR:", repr(e))

#                     return (
#                         "END Identity verification service "
#                         "is currently unavailable. "
#                         "Please try again later."
#                     )

#                 # ---------------------------------------------
#                 # NRB VERIFICATION FAILED
#                 # ---------------------------------------------

#                 if not nrb_response.get("successful"):

#                     message = nrb_response.get(
#                         "message",
#                         "Identity verification failed."
#                     )

#                     return f"""CON {message}

# Please check your details and try again.
# """

#                 # ---------------------------------------------
#                 # NRB VERIFICATION SUCCESSFUL
#                 # ---------------------------------------------

#                 return """CON Identity verification successful.

# Kindly proceed with the registration.

# 1. Continue
# 2. Cancel
# """

#         # =====================================================
#         # COMPANY REGISTRATION
#         # =====================================================

#         if data[1] == "2":

#             # ---------------------------------------------
#             # COMPANY REGISTRATION NUMBER
#             # ---------------------------------------------

#             if len(data) == 2:

#                 return (
#                     "CON Kindly provide Company Registration Number:"
#                 )

#             # ---------------------------------------------
#             # COMPANY REGISTRATION NUMBER ENTERED
#             # ---------------------------------------------

#             if len(data) == 3:

#                 registration_number = data[2].strip()

#                 if not registration_number:

#                     return (
#                         "CON Kindly provide Company Registration Number:"
#                     )

#                 # BRS verification will be added here
#                 return (
#                     "CON Company details received. "
#                     "BRS verification will continue here."
#                 )

#     # =========================================================
#     # SEARCH
#     # =========================================================

#     if data[0] == "2":

#         # -----------------------------------------------------
#         # SEARCH MENU
#         # -----------------------------------------------------

#         if len(data) == 1:

#             return """CON Search Land

# 1. Search by Title Number
# 2. Search by Parcel Number
# """

#         # -----------------------------------------------------
#         # SEARCH BY TITLE
#         # -----------------------------------------------------

#         if len(data) == 2 and data[1] == "1":

#             return "CON Kindly provide Title Number:"

#         # -----------------------------------------------------
#         # SEARCH BY PARCEL
#         # -----------------------------------------------------

#         if len(data) == 2 and data[1] == "2":

#             return "CON Kindly provide Parcel Number:"

#     # =========================================================
#     # CUSTOMER CARE
#     # =========================================================

#     if data[0] == "3":

#         if len(data) == 1:

#             return """CON Customer Care

# 1. Account Support
# 2. Registration Support
# 3. Land Search Support
# """

#     # =========================================================
#     # EXIT
#     # =========================================================

#     if data[0] == "4":

#         return "END Thank you for using Ardhisasa."

#     # =========================================================
#     # INVALID OPTION
#     # =========================================================

#     return "END Invalid option."

from .utils import (
    valid_email,
    valid_phone,
    valid_id_number
)

from app.services import (
    user_exists,
    id_exists,
    email_exists,
    register_user
)

from .integrations.nrb_api import lookup_identity


def menu(text, phone):

    # =========================================================
    # SPLIT USSD INPUT
    # =========================================================

    data = text.split("*") if text else []

    print("USSD DATA:", data)


    # =========================================================
    # MAIN MENU
    # =========================================================

    if len(data) == 0:

        return """CON Welcome to Ardhisasa

1. Register
2. Search
3. Customer Care
4. Exit
"""


    # =========================================================
    # REGISTER
    # =========================================================

    if data[0] == "1":

        # -----------------------------------------------------
        # SELECT REGISTRATION TYPE
        # -----------------------------------------------------

        if len(data) == 1:

            return """CON Select Registration Type

1. Individual
2. Company
"""


        # =====================================================
        # INDIVIDUAL REGISTRATION
        # =====================================================

        if data[1] == "1":

            # -------------------------------------------------
            # SELECT IDENTIFICATION TYPE
            # -------------------------------------------------

            if len(data) == 2:

                return """CON Select Identification Type

1. National ID
2. Passport
3. Alien ID
"""


            # -------------------------------------------------
            # IDENTIFICATION TYPE SELECTED
            # -------------------------------------------------

            if len(data) == 3:

                if data[2] not in ["1", "2", "3"]:

                    return """CON Invalid identification type.

1. National ID
2. Passport
3. Alien ID
"""

                return (
                    "CON Kindly provide ID number "
                    "as it appears on the ID:"
                )


            # -------------------------------------------------
            # ID NUMBER
            # -------------------------------------------------

            if len(data) == 4:

                id_number = data[3].strip()

                print("ID NUMBER:", repr(id_number))

                # Validate ID format

                if not valid_id_number(id_number):

                    return (
                        "CON Kindly provide ID number "
                        "as it appears on the ID:"
                    )

                # Check whether already registered

                try:

                    if id_exists(id_number):

                        return (
                            "END This ID number is already "
                            "registered."
                        )

                except Exception as e:

                    print("ID CHECK ERROR:", repr(e))

                    return (
                        "END Unable to verify registration "
                        "status. Please try again later."
                    )

                return (
                    "CON Kindly provide ID serial number "
                    "as it appears on the ID:"
                )


            # =================================================
            # SERIAL NUMBER + NRB VERIFICATION
            # =================================================

            if len(data) == 5:

                id_number = data[3].strip()
                serial_no = data[4].strip()

                print("ID NUMBER:", repr(id_number))
                print("SERIAL NUMBER:", repr(serial_no))

                if not serial_no:

                    return (
                        "CON Kindly provide ID serial number "
                        "as it appears on the ID:"
                    )


                # ---------------------------------------------
                # CALL SIMULATED NRB API
                # ---------------------------------------------

                try:

                    nrb_response = lookup_identity(
                        id_number=id_number,
                        serial_no=serial_no
                    )

                    print("NRB RESPONSE:", nrb_response)

                except Exception as e:

                    print("NRB ERROR:", repr(e))

                    return (
                        "END Identity verification service "
                        "is currently unavailable. "
                        "Please try again later."
                    )


                # ---------------------------------------------
                # NRB VERIFICATION FAILED
                # ---------------------------------------------

                if not nrb_response.get("successful"):

                    message = nrb_response.get(
                        "message",
                        "Identity verification failed."
                    )

                    return f"""CON {message}

Please check your details and try again.
"""


                # ---------------------------------------------
                # NRB VERIFICATION SUCCESSFUL
                # ---------------------------------------------

                full_names = nrb_response.get(
                    "full_names",
                    {}
                )

                first_name = full_names.get(
                    "first_name",
                    ""
                )

                other_names = full_names.get(
                    "other_names",
                    ""
                )

                surname = full_names.get(
                    "surname",
                    ""
                )

                complete_name = " ".join(
                    part
                    for part in [
                        first_name,
                        other_names,
                        surname
                    ]
                    if part
                )

                gender = nrb_response.get(
                    "gender",
                    ""
                )

                if gender == "M":
                    gender_display = "Male"

                elif gender == "F":
                    gender_display = "Female"

                else:
                    gender_display = gender

                nationality = nrb_response.get(
                    "nationality",
                    ""
                )

                nationality = nationality.title()


                return f"""CON Identity verified

Name: {complete_name}
Gender: {gender_display}
Nationality: {nationality}

1. Confirm
2. Cancel
"""


            # =================================================
            # CONFIRM / CANCEL NRB DETAILS
            # =================================================

            if len(data) == 6:

                confirmation = data[5].strip()

                # ---------------------------------------------
                # CONFIRM
                # ---------------------------------------------

                if confirmation == "1":

                    return """CON Identity confirmed.

Kindly provide your phone number:
"""


                # ---------------------------------------------
                # CANCEL
                # ---------------------------------------------

                if confirmation == "2":

                    return (
                        "END Registration cancelled. "
                        "Thank you for using Ardhisasa."
                    )


                # ---------------------------------------------
                # INVALID OPTION
                # ---------------------------------------------

                return """CON Invalid selection.

1. Confirm
2. Cancel
"""


            # =================================================
            # PHONE NUMBER
            # =================================================

            if len(data) == 7:

                phone_number = data[6].strip()

                print(
                    "REGISTRATION PHONE:",
                    repr(phone_number)
                )

                if not valid_phone(phone_number):

                    return (
                        "CON Invalid phone number. "
                        "Kindly provide a valid phone number:"
                    )


                try:

                    if user_exists(phone_number):

                        return (
                            "END This phone number is already "
                            "registered."
                        )

                except Exception as e:

                    print("PHONE CHECK ERROR:", repr(e))

                    return (
                        "END Unable to verify phone number. "
                        "Please try again later."
                    )


                return (
                    "CON Kindly provide your email address:"
                )


            # =================================================
            # EMAIL
            # =================================================

            if len(data) == 8:

                email = data[7].strip()

                print(
                    "REGISTRATION EMAIL:",
                    repr(email)
                )

                if not valid_email(email):

                    return (
                        "CON Invalid email address. "
                        "Kindly provide a valid email:"
                    )


                try:

                    if email_exists(email):

                        return (
                            "END This email address is already "
                            "registered."
                        )

                except Exception as e:

                    print("EMAIL CHECK ERROR:", repr(e))

                    return (
                        "END Unable to verify email address. "
                        "Please try again later."
                    )


                return (
                    "CON Create your password:"
                )
        # =================================================
    # PASSWORD + CREATE ACCOUNT
    # =================================================

    if len(data) == 9:

        password = data[8]

        if len(password) < 4:

            return (
                "CON Password must contain at least "
                "4 characters:"
            )

        try:

            id_number = data[3]
            id_type = data[2]
            phone_number = data[6]
            email = data[7]

            user = register_user({

                "id_type": id_type,

                "id_number": id_number,

                "phone": phone_number,

                "email": email,

                "password": password

            })

            return f"""END Registration successful.

    Your Ardhisasa ID:
    {user.ardhisasa_id}

    Use this ID to login.

    Password:
    {password}

    Keep your login details safe.
    """

        except Exception as e:

            print(
                "REGISTRATION ERROR:",
                repr(e)
            )

            return (
                "END Registration failed. "
                "Please try again later."
            )

            
        # =====================================================
        # COMPANY REGISTRATION
        # =====================================================

        if data[1] == "2":

            # -------------------------------------------------
            # COMPANY REGISTRATION NUMBER
            # -------------------------------------------------

            if len(data) == 2:

                return (
                    "CON Kindly provide Company "
                    "Registration Number:"
                )


            # -------------------------------------------------
            # COMPANY REGISTRATION NUMBER ENTERED
            # -------------------------------------------------

            if len(data) == 3:

                registration_number = data[2].strip()

                print(
                    "COMPANY REGISTRATION NUMBER:",
                    repr(registration_number)
                )

                if not registration_number:

                    return (
                        "CON Kindly provide Company "
                        "Registration Number:"
                    )


                # ---------------------------------------------
                # BRS WILL BE CONNECTED HERE
                # ---------------------------------------------

                return """CON Company details received.

BRS verification will continue here.

Please wait...
"""


    # =========================================================
    # SEARCH
    # =========================================================

    if data[0] == "2":

        # -----------------------------------------------------
        # SEARCH MENU
        # -----------------------------------------------------

        if len(data) == 1:

            return """CON Search Land

1. Search by Title Number
2. Search by Parcel Number
"""


        # -----------------------------------------------------
        # SEARCH BY TITLE NUMBER
        # -----------------------------------------------------

        if len(data) == 2 and data[1] == "1":

            return (
                "CON Kindly provide Title Number:"
            )


        # -----------------------------------------------------
        # TITLE NUMBER ENTERED
        # -----------------------------------------------------

        if len(data) == 3 and data[1] == "1":

            title_number = data[2].strip()

            if not title_number:

                return (
                    "CON Kindly provide Title Number:"
                )

            # ---------------------------------------------
            # LAND REGISTRY SEARCH WILL BE ADDED HERE
            # ---------------------------------------------

            return f"""END Title search received.

Title Number: {title_number}

Land Registry search will continue here.
"""


        # -----------------------------------------------------
        # SEARCH BY PARCEL NUMBER
        # -----------------------------------------------------

        if len(data) == 2 and data[1] == "2":

            return (
                "CON Kindly provide Parcel Number:"
            )


        # -----------------------------------------------------
        # PARCEL NUMBER ENTERED
        # -----------------------------------------------------

        if len(data) == 3 and data[1] == "2":

            parcel_number = data[2].strip()

            if not parcel_number:

                return (
                    "CON Kindly provide Parcel Number:"
                )

            # ---------------------------------------------
            # LAND REGISTRY SEARCH WILL BE ADDED HERE
            # ---------------------------------------------

            return f"""END Parcel search received.

Parcel Number: {parcel_number}

Land Registry search will continue here.
"""


    # =========================================================
    # CUSTOMER CARE
    # =========================================================

    if data[0] == "3":

        if len(data) == 1:

            return """CON Customer Care

1. Account Support
2. Registration Support
3. Land Search Support
"""


        if len(data) == 2:

            if data[1] == "1":

                return (
                    "END Account Support: "
                    "Please contact customer care."
                )

            if data[1] == "2":

                return (
                    "END Registration Support: "
                    "Please contact customer care."
                )

            if data[1] == "3":

                return (
                    "END Land Search Support: "
                    "Please contact customer care."
                )

            return """CON Invalid option.

1. Account Support
2. Registration Support
3. Land Search Support
"""


    # =========================================================
    # EXIT
    # =========================================================

    if data[0] == "4":

        return (
            "END Thank you for using Ardhisasa."
        )


    # =========================================================
    # INVALID OPTION
    # =========================================================

    return "END Invalid option."