def set_groups():
    group_I = ["MATH","ENG", "KIS"]
    group_II = ["BIO", "PHY", "CHEM"]
    group_III = ["HIST", "GEO", "CRE", "IRE", "HRE"]
    group_IV = ["HSC", "ART", "AGRI", "WDWRK", "METLWK", "COMP ST", "POWER", "ELEC", "D&D"]
    group_V = ["BUS", "FRE", "MUSIC", "GER", "ARB", "SIGN LANG"]

    groups = [group_I, group_II, group_III, group_IV, group_V]

    return groups

def set_subjects():
    subjects = ["MATH", "ENG", "KIS", "BIO", "PHY", "CHEM","GEO", "BUS", "HIST", "CRE", 
            "AGRI", "HSC", "COMPST",  "FRE", "MUS"]
    
    return subjects


def set_value_points():
    value_points = {
    "A": 12, "A-": 11, "B+": 10, "B": 9, "B-": 8,
    "C+": 7, "C": 6, "C-": 5, "D+": 4, "D": 3, "D-": 2, "E": 1
}
    return value_points