import streamlit as st
from clusters import cluster_2, cluster_1
from setters import *

# Title of the app
st.title("KCSE Cluster Points Calculator")

# Grade points mapping
value_points = set_value_points()

# Subject list
subjects = set_subjects()

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
        
    grades_1 = grades.copy()
   
    # get groups
    groups = set_groups()
    # Grand total
    cluster_groups_list = [cluster_1(grades, groups), cluster_2(grades_1, groups)]
    for i in cluster_groups_list : 
        # total_points_all = i(grades, groups)
        total_points_all = i


        # Calculate the cluster points
        result_r = total_points_all / 48
        result_t = GRADE_POINTS / 84
        part_1 = result_r * result_t
        cluster = (part_1 ** 0.5) * 48

        # Display the calculated cluster points
        st.subheader("Cluster Points are:")
        st.write(f"Cluster values for cluster {i}: {cluster:.2f}")
        st.write(f"Total points for cluster {i}: {total_points_all:.2f}")

