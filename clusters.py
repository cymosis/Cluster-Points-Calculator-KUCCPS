# Subject 1: ENG/KIS, Subject 2: MAT/A/MATB/ANY GROUP II, Subject 3: ANY GROUP III, Subject 4: ANY GROUP II/2nd GROUP III/ANY GROUP IV/ANY GROUP V.
def cluster_1(grades, groups):
        # Calculate the total points for each group
        #weight 1
        weight_1_sub = max(["ENG", "KIS"], key=lambda sub: grades[sub])  # Corrected line
        weight_1 = grades[weight_1_sub] 
        #Drop the lowest subject in group I
        del grades[weight_1_sub]
        # weigh 2
        weight_2_sub = max(["MATH"] + groups[1], key=lambda sub: grades[sub])  
        weight_2 = grades[weight_2_sub] 
        #Drop weight_2_sub
        del grades[weight_2_sub]
        #Weight 3
        weight_3_sub = max([subj for subj in groups[2] if subj in grades], key=grades.get)
        weight_3 = grades[weight_3_sub]
        #drop weight_3_sub
        del grades[weight_3_sub]
        #Weight 4
        # Combine eligible subjects for Weight 4
        eligible_weight_4 = list(set(groups[1]) & set(grades.keys())) + \
                        list(set(groups[2]) & set(grades.keys())) + \
                        list(set(groups[3]) & set(grades.keys())) + \
                        list(set(groups[4]) & set(grades.keys()))
        
        # Find the subject with the highest grade from the eligible subjects
        weight_4_sub = max(eligible_weight_4, key=lambda sub: grades[sub])
        weight_4 = grades[weight_4_sub]

        # Calculate the total points for each group
        total_points_i = weight_1 + weight_2 + weight_3 + weight_4

        response = {'total_points': total_points_i, 'cluster_name': 'Law and related causes'}

        return response

# Subject 1: ENG/KIS, Subject 2: MAT/A/MAT/B, Subject 3: any GROUP II or any GROUP III, Subject 4: a GROUP II or a GROUP III or any GROUP IV or any GROUP V.
def cluster_2(grades, groups):
        # Calculate the total points for each group
        #weight 1
        weight_1_sub = max(["ENG", "KIS"], key=lambda sub: grades[sub])  # Corrected line
        weight_1 = grades[weight_1_sub] 
        #Drop the lowest subject in group I
        del grades[weight_1_sub]
        # weigh 2
        # weight_2_sub = max(["MATH"] + groups[1], key=lambda sub: grades[sub])  
        weight_2 = grades["MATH"] 
        #Drop weight_2_sub
        del grades["MATH"]
        #Weight 3
        weight_3_sub = max([subj for subj in groups[2] + groups[1] if subj in grades], key=grades.get)
        weight_3 = grades[weight_3_sub]
        #drop weight_3_sub
        del grades[weight_3_sub]
        #Weight 4
        # Find the subject with the highest grade from the eligible subjects
        weight_4_sub = max([subj for subj in groups[2] + groups[1] + groups[3] + groups[4] if subj in grades], key=grades.get)
        weight_4 = grades[weight_4_sub]

        # Calculate the total points for each group
        total_points_i = weight_1 + weight_2 + weight_3 + weight_4

        response = {'total_points': total_points_i, 'cluster_name': 'Business, Management, and Applied Sciences Cluster'}

        return response

# Subject 1: ENG/KIS, Subject 2: MAT/A/MAT/B or any GROUP II, Subject 3: any GROUP III, Subject 4: a GROUP II or 2nd GROUP III or any GROUP IV or any GROUP V
def cluster_3(grades, groups):
    # Calculate the total points for each group
    # weight 1
    weight_1_sub = max(["ENG", "KIS"], key=lambda sub: grades[sub])  # Corrected line
    weight_1 = grades[weight_1_sub] 
    # Drop the lowest subject in group I
    del grades[weight_1_sub]

    # weight 2
    weight_2_sub = max(["MATH"] + groups[1], key=lambda sub: grades[sub])  
    weight_2 = grades[weight_2_sub] 
    # Drop weight_2_sub
    del grades[weight_2_sub]

    # Weight 3
    # Filter subjects in groups[2] that are in grades
    valid_weight_3_subs = [subj for subj in groups[2] if subj in grades]
    if valid_weight_3_subs:
        weight_3_sub = max(valid_weight_3_subs, key=grades.get)
        weight_3 = grades[weight_3_sub]
        del grades[weight_3_sub]
    else:
        weight_3 = 0  # Fallback in case there are no valid subjects

    # Weight 4
    # Find the subject with the highest grade from the eligible subjects
    valid_weight_4_subs = [subj for subj in groups[1] + groups[3] + groups[4] if subj in grades]
    if valid_weight_4_subs:
        weight_4_sub = max(valid_weight_4_subs, key=grades.get)
        weight_4 = grades[weight_4_sub]
        del grades[weight_4_sub]
    else:
        weight_4 = 0  # Fallback in case there are no valid subjects

    # Calculate the total points for each group
    total_points_i = weight_1 + weight_2 + weight_3 + weight_4

    response = {'total_points': total_points_i, 'cluster_name': 'Communication, Media, and Social Sciences Cluster'}

    return response


# Subject 1: MAT/A, Subject 2: PHY, Subject 3: BIO or CHE or GEO, Subject 4: a GROUP II or any GROUP III or any GROUP IV or any GROUP V.
def cluster_4(grades, groups): 
    # Calculate the total points for each group
    # weight 1
    weight_1_sub = max(["MATH"], key=lambda sub: grades[sub])  # Corrected line
    weight_1 = grades[weight_1_sub] 
    # Drop the lowest subject in group I
    del grades[weight_1_sub]

    # weight 2
    weight_2_sub = max(["PHY"], key=lambda sub: grades[sub])  
    weight_2 = grades[weight_2_sub] 
    # Drop weight_2_sub
    del grades[weight_2_sub]

    # Weight 3
    # Combine groups 2, 3, and 4, and filter valid subjects in grades
    valid_weight_3_subs = [subj for subj in groups[2] + groups[3] + groups[4] if subj in grades]
    if valid_weight_3_subs:
        weight_3_sub = max(valid_weight_3_subs, key=grades.get)
        weight_3 = grades[weight_3_sub]
        # Drop weight_3_sub
        del grades[weight_3_sub]
    else:
        weight_3 = 0  # Fallback in case no valid subjects exist for weight 3

    # Weight 4
    # Combine eligible subjects for Weight 4 and filter valid subjects in grades
    valid_weight_4_subs = [subj for subj in groups[1] + groups[2] + groups[3] + groups[4] if subj in grades]
    if valid_weight_4_subs:
        weight_4_sub = max(valid_weight_4_subs, key=grades.get)
        weight_4 = grades[weight_4_sub]
        # Drop weight_4_sub
        del grades[weight_4_sub]
    else:
        weight_4 = 0  # Fallback in case no valid subjects exist for weight 4

    # Calculate the total points for each group
    total_points_i = weight_1 + weight_2 + weight_3 + weight_4

    response = {'total_points': total_points_i, 'cluster_name': 'Geospatial and Earth Sciences Cluster'}

    return response

# Subject 1: MAT (A), Subject 2: PHY, Subject 3: 2nd GROUP II or any GROUP III, Subject 4: GROUP II or GROUP III or any GROUP IV or any GROUP V.
def cluster_9(grades, groups):
        # Calculate the total points for each group
        # weight 1
        weight_1_sub = max(["MATH"], key=lambda sub: grades[sub])  # Corrected line
        weight_1 = grades[weight_1_sub] 
        # Drop the lowest subject in group I
        del grades[weight_1_sub]
        
        # weight 2
        weight_2_sub = max(["PHY"], key=lambda sub: grades[sub])  
        weight_2 = grades[weight_2_sub] 
        # Drop weight_2_sub
        del grades[weight_2_sub]
        
        # Weight 3
        # Combine groups 2 and 3, and filter valid subjects in grades
        valid_weight_3_subs = [subj for subj in groups[1] + groups[2] if subj in grades]
        if valid_weight_3_subs:
                weight_3_sub = max(valid_weight_3_subs, key=grades.get)
                weight_3 = grades[weight_3_sub]
                # Drop weight_3_sub
                del grades[weight_3_sub]
        else:
                weight_3 = 0  # Fallback in case no valid subjects exist for weight 3
        
        # Weight 4
        # Combine eligible subjects for Weight 4 and filter valid subjects in grades
        valid_weight_4_subs = [subj for subj in groups[1] + groups[2] + groups[3] + groups[4] if subj in grades]
        if valid_weight_4_subs:
                weight_4_sub = max(valid_weight_4_subs, key=grades.get)
                weight_4 = grades[weight_4_sub]
                # Drop weight_4_sub
                del grades[weight_4_sub]
        else:
                weight_4 = 0  # Fallback in case no valid subjects exist for weight 4
        
        # Calculate the total points for each group
        total_points_i = weight_1 + weight_2 + weight_3 + weight_4
        
        response = {'total_points': total_points_i, 'cluster_name': 'Computer Science, Technology, and Applied Mathematics Cluster'}
        
        return response
