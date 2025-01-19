import streamlit as st

# Title of the app
st.title("KCSE Cluster Points Calculator")

# Grade points mapping
value_points = {
    "A": 12, "A-": 11, "B+": 10, "B": 9, "B-": 8,
    "C+": 7, "C": 6, "C-": 5, "D+": 4, "D": 3, "D-": 2, "E": 1
}

# Subject list
subjects = ["MATH", "ENG", "KIS", "BIO", "PHY", "CHEM", "HIST", "CRE", "GEO", 
            "AGRI", "HSC", "COMPST", "BUS", "FRE", "MUS"]

# Allow user to select subjects
GRADE_POINTS = st.number_input('Please input your grade points:', min_value=0, max_value=84, step=1)
selected_subjects = st.multiselect("Select subjects (choose 7 or 8):", options=subjects, default=subjects[:7])

# Display grade selection for each selected subject
if len(selected_subjects) not in [7, 8]:
    st.error("You must select exactly 7 or 8 subjects.")
else:
    grades = {}
    for sub in selected_subjects:
        grades[sub] = st.selectbox(f"Choose a grade for {sub}:", list(value_points.keys()), key=sub)

    # Calculate total points for each group
    group_0= {"MATH": grades.get("MATH", "")}
    group_i = {"ENG": grades.get("ENG", ""), "KIS": grades.get("KIS", "")}
    group_ii = {"BIO": grades.get("BIO", ""), "PHY": grades.get("PHY", ""), "CHEM": grades.get("CHEM", "")}
    group_iii = {"HIST": grades.get("HIST", ""), "CRE": grades.get("CRE", ""), "GEO": grades.get("GEO", "")}
    group_iv = {"AGRI": grades.get("AGRI", ""), "HSC": grades.get("HSC", ""), "COMPST": grades.get("COMPST", "")}
    group_v = {"BUS": grades.get("BUS", ""), "FRE": grades.get("FRE", ""), "MUS": grades.get("MUS", "")}

    # Calculate the total points
    total_points_0 = max((value_points[grade] for grade in group_0.values() if grade), default=0)
    total_points_i = max((value_points[grade] for grade in group_i.values() if grade), default=0)
    total_points_ii = max((value_points[grade] for grade in group_ii.values() if grade), default=0)
    total_points_iii = max((value_points[grade] for grade in group_iii.values() if grade), default=0)
    total_points_iv = max((value_points[grade] for grade in group_iv.values() if grade), default=0)

    # Grand total
    total_points_all = total_points_i + total_points_ii + total_points_iii + total_points_0

    # Calculate the cluster points
    result_r = total_points_all / 48
    result_t = GRADE_POINTS / 84
    part_1 = result_r * result_t
    cluster = (part_1 ** 0.5) * 48

    # Display the calculated cluster points
    st.subheader("Cluster Points are:")
    st.write(f"Cluster Value: {cluster:.2f}")
