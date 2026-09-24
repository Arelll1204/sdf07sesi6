def validate_name(name):
    if not name or name.strip() == "":
        return False, "Nama tidak boleh kosong"
    return True, "Nama valid"
