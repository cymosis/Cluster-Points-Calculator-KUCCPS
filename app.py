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
        selected_grade = st.selectbox(f"Choose a grade for {sub}:", list(value_points.keys()), key=sub)
        grades[sub]=value_points[selected_grade]

        # "eng": "10"
 
    group_I = ["MATH","ENG", "KIS"]
    group_II = ["BIO", "PHY", "CHEM"]
    group_III = ["HIST", "GEO", "CRE", "IRE", "HRE"]
    group_IV = ["HSC", "ART", "AGRI", "WDWRK", "METLWK", "COMP ST", "POWER", "ELEC", "D&D"]
    group_V = ["BUS", "FRE", "MUSIC", "GER", "ARB", "SIGN LANG"]

    # Calculate the total points for each group
    #weight 1
    weight_1_sub = max(["ENG", "KIS"], key=lambda sub: grades[sub])  # Corrected line
    weight_1 = grades[weight_1_sub] 
    #Drop the lowest subject in group I
    del grades[weight_1_sub]
    # weigh 2
    weight_2_sub = max(["MATH"] + group_II, key=lambda sub: grades[sub])  
    weight_2 = grades[weight_2_sub] 
    #Drop weight_2_sub
    del grades[weight_2_sub]
    #Weight 3
    weight_3_sub = max([subj for subj in group_III if subj in grades], key=grades.get)
    weight_3 = grades[weight_3_sub]
    #drop weight_3_sub
    del grades[weight_3_sub]
    #Weight 4
    # Combine eligible subjects for Weight 4
    eligible_weight_4 = list(set(group_II) & set(grades.keys())) + \
                    list(set(group_III) & set(grades.keys())) + \
                    list(set(group_IV) & set(grades.keys())) + \
                    list(set(group_V) & set(grades.keys()))
    
    # Find the subject with the highest grade from the eligible subjects
    weight_4_sub = max(eligible_weight_4, key=lambda sub: grades[sub])
    weight_4 = grades[weight_4_sub]

    # Calculate the total points for each group
    total_points_i = weight_1 + weight_2 + weight_3 + weight_4


    # Grand total
    total_points_all = total_points_i


    # Calculate the cluster points
    result_r = total_points_all / 48
    result_t = GRADE_POINTS / 84
    part_1 = result_r * result_t
    cluster = (part_1 ** 0.5) * 48

    # Display the calculated cluster points
    st.subheader("Cluster Points are:")
    st.write(f"Cluster values: {cluster:.2f}")
    st.write(f"Total points: {total_points_i:.2f}")


cluster_dictionary = {
    "cluster_1": {
        "cluster_name": "Cluster 1",
        "description": "Law and related courses",
        "rules": {
            "priority_subjects": ["English", "History", "Kiswahili"]
        },
        "limiters": {
            "minimum_points": 42,
            "maximum_points": 48
        }
    },
}

