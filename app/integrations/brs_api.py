# integrations/brs_api.py

BRS_DATABASE = {

    "CPR/2012/79231": {
        "successful": True,
        "status": "registered",
        "registration_number": "CPR/2012/79231",
        "registration_date": "17 July 2012",
        "postal_address": "48076 - 00100",
        "phone_number": None,

        "company_name": "EXECUTIVE CONCEPTS LIMITED",

        "partners": [
            {
                "type": "director_shareholder",
                "shares": [
                    {
                        "number_of_shares": 1,
                        "name": "ORDINARY"
                    }
                ],
                "name": "MANSUKHLAL HARIDAS JAMNADAS CHOTAI",
                "id_type": "citizen",
                "id_number": "1329276",
                "gender": "M"
            }
        ]
    }
}


def verify_company(registration_number):

    result = BRS_DATABASE.get(registration_number)

    if result:
        return result

    return {
        "successful": False,
        "registration_number": registration_number,
        "status": "NOT_FOUND",
        "message": "Company registration details not found"
    }