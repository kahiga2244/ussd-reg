# integrations/nrb_api.py

NRB_DATABASE = {

    "027191514": {
        "successful": True,
        "id_number": "027191514",
        "id_type": "NATIONAL ID",
        "serial_no": "705976861",
        "full_names": {
            "first_name": "ALFRED",
            "other_names": "KIPLAGAT",
            "surname": "KETTER"
            },
        "gender": "M",
        "mother_full_name": "THERESA JEPTUM MOSBEI",
        "nationality": "KENYAN"
        },

    "12345678": {
        "successful": True,
        "id_number": "12345678",
        "id_type": "NATIONAL ID",
        "status": "ACTIVE",
        "serial_no": "123456789",
        "full_names": {
                       "first_name": "JOHN",
                       "other_names": "KAMAU",
                       "surname": "MWANGI"
                   },
        "gender": "M",
        "mother_full_name": "MARY WANJIKU",
        "nationality": "KENYAN"
    },
  "024452061":  {
    "successful": True,
    "id_number": "024452061",
    "id_type": "NATIONAL ID",
    "status": "ACTIVE",
    "serial_no": "242239903",
     "full_names": {
                        "first_name": "NOOR",
                        "other_names": "JAMA",
                        "surname": "YUSUF"
                       },
    "gender": "M",
    "mother_full_name": "ZAINAB JAMA YUSUF",
    "date_end_validity": "",
    "nationality": "KENYAN"
},
"7457673":{
    "successful": True, 
    "id_number": "7457673",
    "id_type": "NATIONAL ID",
    "status": "ACTIVE",
    "serial_no": "705525980",
    "full_names": {
                        "first_name":"FABIAN",
                        "other_names": "",
                        "surname": "KABURU"
             },
         "gender": "M",
         "mother_full_name": "DORITHI WANJIRU",
         "nationality": "KENYAN"
  },
    "13640446":{
        "successful": True, 
        "id_number": "7457673",
        "id_type": "NATIONAL ID",
        "status": "ACTIVE",
        "serial_no": "228077470",
        "full_names": 
             {
                        "first_name":"JOSEPH",
                        "other_names": "NGAO",
                        "surname": "NGUKU"
             },
        "gender": "M",
        "mother_full_name": "DORITHI WANJIRU",
        "nationality": "KENYAN"
},
 "021357124": {
    "successful": True,
    "id_number": "021357124",
    "id_type": "NATIONAL ID",
    "status": "ACTIVE",
    "serial_no": "240572915",
    "full_names": {
        "full_names": "MARY",
        "other_names": "MUTHONI",
        "surname": "KIMARI" 
    },
    "gender": "F",
    "mother_full_name": "DORIS WANJIRU",
    "date_end_validity": "",
    "nationality": "KENYAN"
},
}

def normalize(value):
    """
    Normalize text before comparison.
    """

    if value is None:
        return ""

    return " ".join(str(value).strip().upper().split())


def verify_identity(
    id_number,
    serial_no,
    first_name,
    other_names,
    surname,
    gender,
    mother_full_name,
    nationality
):

    record = NRB_DATABASE.get(id_number)

    # ID number does not exist
    if not record:

        return {
            "successful": False,
            "error": "ID_NUMBER_NOT_FOUND",
            "message": "Kindly provide ID number as it appears on the ID."
        }

    # -----------------------------------------
    # VERIFY SERIAL NUMBER
    # -----------------------------------------

    if normalize(serial_no) != normalize(record["serial_no"]):

        return {
            "successful": False,
            "error": "SERIAL_NUMBER_MISMATCH",
            "message": "Kindly provide ID serial number as it appears on the ID."
        }

    # -----------------------------------------
    # VERIFY FIRST NAME
    # -----------------------------------------

    if normalize(first_name) != normalize(
        record["full_names"]["first_name"]
    ):

        return {
            "successful": False,
            "error": "FIRST_NAME_MISMATCH",
            "message": "Kindly provide first name as it appears on the ID."
        }

    # -----------------------------------------
    # VERIFY OTHER NAMES
    # -----------------------------------------

    if normalize(other_names) != normalize(
        record["full_names"]["other_names"]
    ):

        return {
            "successful": False,
            "error": "OTHER_NAMES_MISMATCH",
            "message": "Kindly provide other names as they appear on the ID."
        }

    # -----------------------------------------
    # VERIFY SURNAME
    # -----------------------------------------

    if normalize(surname) != normalize(
        record["full_names"]["surname"]
    ):

        return {
            "successful": False,
            "error": "SURNAME_MISMATCH",
            "message": "Kindly provide surname as it appears on the ID."
        }

    # -----------------------------------------
    # VERIFY GENDER
    # -----------------------------------------

    if normalize(gender) != normalize(record["gender"]):

        return {
            "successful": False,
            "error": "GENDER_MISMATCH",
            "message": "Kindly provide gender as it appears on the ID."
        }

    # -----------------------------------------
    # VERIFY MOTHER'S NAME
    # -----------------------------------------

    if normalize(mother_full_name) != normalize(
        record["mother_full_name"]
    ):

        return {
            "successful": False,
            "error": "MOTHER_NAME_MISMATCH",
            "message": "Kindly provide mother's full name as it appears on the ID."
        }

    # -----------------------------------------
    # VERIFY NATIONALITY
    # -----------------------------------------

    if normalize(nationality) != normalize(
        record["nationality"]
    ):

        return {
            "successful": False,
            "error": "NATIONALITY_MISMATCH",
            "message": "Kindly provide nationality as it appears on the ID."
        }

    # -----------------------------------------
    # ALL DETAILS MATCH
    # -----------------------------------------

    return {
        "successful": True,
        "message": "Identity successfully verified.",
        "id_number": record["id_number"],
        "id_type": record["id_type"],
        "serial_no": record["serial_no"],
        "full_names": record["full_names"],
        "gender": record["gender"],
        "mother_full_name": record["mother_full_name"],
        "nationality": record["nationality"]
    }
    
def lookup_identity(id_number, serial_no):

    record = NRB_DATABASE.get(id_number)

    if not record:

        return {
            "successful": False,
            "error": "ID_NUMBER_NOT_FOUND",
            "message": "Kindly provide ID number as it appears on the ID."
        }

    if normalize(serial_no) != normalize(record["serial_no"]):

        return {
            "successful": False,
            "error": "SERIAL_NUMBER_MISMATCH",
            "message": (
                "Kindly provide ID serial number "
                "as it appears on the ID."
            )
        }

    return {
        "successful": True,
        "message": "Identity successfully verified.",
        "id_number": record["id_number"],
        "id_type": record["id_type"],
        "serial_no": record["serial_no"],
        "full_names": record["full_names"],
        "gender": record["gender"],
        "mother_full_name": record["mother_full_name"],
        "nationality": record["nationality"]
    }