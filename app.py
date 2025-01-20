import streamlit as st
from clusters import *
from setters import *

# Title of the app
st.title("KCSE Cluster Points Calculator")

# Grade points mapping
value_points = set_value_points()

# Subject list
subjects = set_subjects()

col1, col2 = st.columns([6, 6]) 
with col1:
    # Allow user to select subjects
    GRADE_POINTS = st.number_input('Please input your grade points:', min_value=0, max_value=84, step=1)
    selected_subjects = st.multiselect("Select subjects (choose 7 or 8):", options=subjects, default=subjects[:8])

    # Display grade selection for each selected subject
    if len(selected_subjects) not in [7, 8]:
        st.error("You must select exactly 7 or 8 subjects.")
    else:
        grades = {}
        for sub in selected_subjects:
            selected_grade = st.selectbox(f"Choose a grade for {sub}:", list(value_points.keys()), key=sub)
            grades[sub]=value_points[selected_grade]
        # Make a copy of the grades

        grades_1 = grades.copy()
        grades_2 = grades.copy()
        grades_3 = grades.copy()
        grades_4=grades.copy()
        grades_5=grades.copy()
        grades_6=grades.copy()
        grades_7=grades.copy()
        grades_8 = grades.copy()
        grades_9 = grades.copy()
        grades_10 = grades.copy()
        grades_11 = grades.copy()
        grades_12 = grades.copy()

        # get groups
        groups = set_groups()
    # Grand total
with col2:
    st.subheader("Cluster Points are:")
    
    cluster_groups_list = [cluster_1(grades, groups), cluster_2(grades_1, groups), cluster_3(grades_2, groups), cluster_4(grades_3, groups),cluster_5(grades_4, groups),
                           cluster_7(grades_6, groups),cluster_8(grades_7, groups),cluster_9(grades_8, groups),cluster_10(grades_9, groups),cluster_11(grades_10, groups),
                           cluster_12(grades_11, groups),cluster_13(grades_12, groups)]
   # Iterate through the cluster responses
    for i, total_points_all in enumerate(cluster_groups_list):
        # Extract total points and cluster name from the response
        total_points_all_value = total_points_all['total_points']
        cluster_name = total_points_all['cluster_name']

        # Calculate the cluster points
        result_r = total_points_all_value / 48
        result_t = GRADE_POINTS / 84  # Adjust this if needed
        part_1 = result_r * result_t
        cluster = (part_1 ** 0.5) * 48

        # Display the calculated cluster points and total points
        st.write(f"{cluster_name}: {cluster:.2f}")




