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

        return total_points_i



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

        return total_points_i