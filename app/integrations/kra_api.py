# integrations/kra_api.py

KRA_DATABASE = {

    "A123456789Z": {
        "successful": True,
        "pin": "A123456789Z",
        "taxpayer_name": "ALFRED KIPLAGAT KETTER",
        "pin_status": "ACTIVE",
        "taxpayer_type": "INDIVIDUAL",
        "tax_compliance_status": "COMPLIANT"
    },

    "P051395867U": {
        "successful": True,
        "pin": "P051395867U",
        "taxpayer_name": "EXECUTIVE CONCEPTS LIMITED",
        "pin_status": "ACTIVE",
        "taxpayer_type": "COMPANY",
        "tax_compliance_status": "COMPLIANT"
    }
}


def verify_pin(pin):

    result = KRA_DATABASE.get(pin)

    if result:
        return result

    return {
        "successful": False,
        "pin": pin,
        "pin_status": "INVALID",
        "message": "KRA PIN could not be verified"
    }