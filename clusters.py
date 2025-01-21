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


# Subject 1: ENG/KIS, Subject 2: MAT/A/MAT/B, Subject 3: any GROUP II or any GROUP III, Subject 4: a GROUP II or a GROUP III or any GROUP IV or any GROUP V.
def cluster_5(grades, groups):
        # Calculate the total points for each group
        #weight 1
        weight_1_sub = max(["ENG", "KIS"], key=lambda sub: grades[sub])  # Corrected line
        weight_1 = grades[weight_1_sub] 
        #Drop the lowest subject in group I
        del grades[weight_1_sub]
        # weigh 2
        # weight_2_sub = max(["MATH"] + groups[1], key=lambda sub: grades[sub])  
        weight_2_sub = max([subj for subj in ['BIO','GSC'] if subj in grades], key=grades.get)
        weight_2 = grades[weight_2_sub] 
        #Drop weight_2_sub
        del grades[weight_2_sub]
        #Weight 3
        weight_3_sub = max([subj for subj in groups[2] if subj in grades], key=grades.get)
        weight_3 = grades[weight_3_sub]
        #drop weight_3_sub
        del grades[weight_3_sub]
        #Weight 4
        # Find the subject with the highest grade from the eligible subjects
        weight_4_sub = max([subj for subj in groups[2] + groups[1] + groups[3] + groups[4] if subj in grades], key=grades.get)
        weight_4 = grades[weight_4_sub]

        # Calculate the total points for each group
        total_points_i = weight_1 + weight_2 + weight_3 + weight_4

        response = {'total_points': total_points_i, 'cluster_name': 'Education and Related'}

        return response


def cluster_6(grades, groups):
        # Calculate the total points for each group
        #weight 1
        weight_1_sub = 'MATH'
        weight_1 = grades[weight_1_sub] 
        #Drop the lowest subject in group I
        del grades[weight_1_sub]
        # weigh 2
        # weight_2_sub = max(["MATH"] + groups[1], key=lambda sub: grades[sub])  
        weight_2_sub = max([subj for subj in ['ENG','MATH']+ grades[1] if subj in grades], key=grades.get)
        weight_2 = grades[weight_2_sub] 
        #Drop weight_2_sub
        del grades[weight_2_sub]
        #Weight 3
        weight_3_sub = max([subj for subj in groups[2] if subj in grades], key=grades.get)
        weight_3 = grades[weight_3_sub]
        #drop weight_3_sub
        del grades[weight_3_sub]
        #Weight 4
        # Find the subject with the highest grade from the eligible subjects
        weight_4_sub = max([subj for subj in groups[2] + groups[1] + groups[3] + groups[4] if subj in grades], key=grades.get)
        weight_4 = grades[weight_4_sub]

        # Calculate the total points for each group
        total_points_i = weight_1 + weight_2 + weight_3 + weight_4

        response = {'total_points': total_points_i, 'cluster_name': 'Arts(Kiswahili)& Related'}

        return response

def cluster_7(grades, groups):
        # Calculate the total points for each group
        #weight 1
        if 'PHY' not in grades or 'CHEM' not in grades:
                return {'message': 'Do not qualify'}
        weight_1 = grades["MATH"] 
        #Drop weight_2_sub
        del grades["MATH"]
        #Drop the lowest subject in group I

        # weigh 2
        if 'PHY' in grades.keys():
            weight_2 = grades["PHY"] 
            #Drop weight_2_sub
            del grades["PHY"]
        else:
              print('Do not qualify')
        #Drop weight_2_sub
        
        #Weight 3
        if 'CHEM' in grades.keys():
            weight_3 = grades["CHEM"] 
            #Drop weight_2_sub
            del grades["CHEM"]
        else:
              print('Do not qualify')

        #Weight 4
        # Find the subject with the highest grade from the eligible subjects
        BIO=['BIO']
        weight_4_sub = max([subj for subj in groups[2] + BIO + groups[3] + groups[4] if subj in grades], key=grades.get)
        weight_4 = grades[weight_4_sub]

        # Calculate the total points for each group
        total_points_i = weight_1 + weight_2 + weight_3 + weight_4

        response = {'total_points': total_points_i, 'cluster_name': 'Engineering, Engineering Technology & Related'}

        return response

def cluster_8(grades, groups):
        # Calculate the total points for each group
        #weight 1
        if 'PHY' not in grades:
                return {'message': 'Do not qualify'}
        weight_1 = grades["MATH"] 
        #Drop weight_2_sub
        del grades["MATH"]
        #Drop the lowest subject in group I

        # weigh 2
        if 'PHY' in grades.keys():
            weight_2 = grades["PHY"] 
            #Drop weight_2_sub
            del grades["PHY"]
        else:
              print('Do not qualify')
        #Drop weight_2_sub
        
        #Weight 3
        weight_3_sub = max([subj for subj in groups[2] if subj in grades], key=grades.get)
        weight_3= grades[weight_3_sub]
        del grades[weight_3_sub]

        #Weight 4
        # Find the subject with the highest grade from the eligible subjects

        weight_4_sub = max([subj for subj in groups[2] + groups[1] + groups[3] + groups[4] if subj in grades], key=grades.get)
        weight_4 = grades[weight_4_sub]

        # Calculate the total points for each group
        total_points_i = weight_1 + weight_2 + weight_3 + weight_4

        response = {'total_points': total_points_i, 'cluster_name': 'Architecture, Building Construction & Related'}

        return response

def cluster_10(grades, groups):
        if 'BIO' not in grades:
                return {'message': 'Do not qualify'}
        # Calculate the total points for each group
        #weight 1
        weight_1 = grades["MATH"] 
        #Drop weight_2_sub
        del grades["MATH"]
        #Drop the lowest subject in group I

        # weigh 2
        if 'BIO' in grades.keys():
            weight_2 = grades["BIO"] 
            #Drop weight_2_sub
            del grades["BIO"]
        else:
              print('Do not qualify')
        #Drop weight_2_sub
        weight_3_sub = max([subj for subj in ['PHY','CHEM'] if subj in grades], key=grades.get)
        #Weight 3
        weight_3 = grades[weight_3_sub]
            #Drop weight_2_sub
        del grades[weight_3_sub]


        #Weight 4
        # Find the subject with the highest grade from the eligible subjects
        weight_4_sub = max([subj for subj in groups[2] + groups[1] + groups[3] + groups[4] if subj in grades], key=grades.get)
        weight_4 = grades[weight_4_sub]

        # Calculate the total points for each group
        total_points_i = weight_1 + weight_2 + weight_3 + weight_4

        response = {'total_points': total_points_i, 'cluster_name': 'Agribusiness & Related'}

        return response


#MAT ,any	GROUP	II ,GROUP	II,GROUP	II	or	any	GROUP	III	or	anyGROUP	IV	or	any	GROUP	V
def cluster_11(grades, groups):
        # Calculate the total points for each group
        #weight 1
        weight_1 = grades["MATH"]  
        #Drop the lowest subject in group I
        del grades['MATH']
        # weigh 2
        # weight_2_sub = max(["MATH"] + groups[1], key=lambda sub: grades[sub])  
        weight_2_sub = max([subj for subj in groups[1] if subj in grades], key=grades.get) 
        weight_2 = grades[weight_2_sub]
        #Drop weight_2_sub
        del grades[weight_2_sub]
        #Weight 3
        weight_3_sub = max([subj for subj in groups[1] if subj in grades], key=grades.get)
        weight_3 = grades[weight_3_sub]
        #drop weight_3_sub
        del grades[weight_3_sub]
        #Weight 4
        # Find the subject with the highest grade from the eligible subjects
        weight_4_sub = max([subj for subj in groups[2] + groups[1] + groups[3] + groups[4] if subj in grades], key=grades.get)
        weight_4 = grades[weight_4_sub]

        # Calculate the total points for each group
        total_points_i = weight_1 + weight_2 + weight_3 + weight_4

        response = {'total_points': total_points_i, 'cluster_name': 'General Science , Biological Sciences, Physics, Chemistry & Related'}

        return response

#MAT ,any	GROUP	II ,GROUP	II,GROUP	III	or	any	GROUP	III	or	anyGROUP	IV	or	any	GROUP	V
def cluster_12(grades, groups):
        # Calculate the total points for each group
        #weight 1
        weight_1 = grades["MATH"]  
        #Drop the lowest subject in group I
        del grades['MATH']
        # weigh 2
        # weight_2_sub = max(["MATH"] + groups[1], key=lambda sub: grades[sub])  
        weight_2_sub = max([subj for subj in groups[1] if subj in grades], key=grades.get) 
        weight_2 = grades[weight_2_sub]
        #Drop weight_2_sub
        del grades[weight_2_sub]
        #Weight 3
        weight_3_sub = max([subj for subj in groups[2] if subj in grades], key=grades.get)
        weight_3 = grades[weight_3_sub]
        #drop weight_3_sub
        del grades[weight_3_sub]
        #Weight 4
        # Find the subject with the highest grade from the eligible subjects
        weight_4_sub = max([subj for subj in groups[2] + groups[1] + groups[3] + groups[4] if subj in grades], key=grades.get)
        weight_4 = grades[weight_4_sub]

        # Calculate the total points for each group
        total_points_i = weight_1 + weight_2 + weight_3 + weight_4

        response = {'total_points': total_points_i, 'cluster_name': 'Actuarial Science, Accountancy, Mathematics, Economics, Statistics & Related'}

        return response
#CHEM ,MAT	A,BIO	or	HSC,ENG/KIS	or	any	GROUP	III	or	a GROUP	IV	or	any	GROUP	V
def cluster_13(grades, groups):
        subjects_needed = ['CHEM']

        #weight 1
        weight_1 = grades["CHEM"]  
        #Drop the lowest subject in group I
        del grades['CHEM']
        # weigh 2
        # weight_2_sub = max(["MATH"] + groups[1], key=lambda sub: grades[sub])  
        weight_2 = grades["MATH"]  
        #Drop the lowest subjecHt in group I
        
        #Drop weight_2_sub
        del grades['MATH']
        #Weight 3
        weight_3_sub = max([subj for subj in ['BIO','HSC'] if subj in grades], key=grades.get) 
        weight_3 = grades[weight_3_sub]
        #Drop weight_2_sub
        del grades[weight_3_sub]
        #Weight 4
        # Find the subject with the highest grade from the eligible subjects
        LAN=['ENG','KIS']
        weight_4_sub = max([subj for subj in groups[2] + LAN + groups[3] + groups[4] if subj in grades], key=grades.get)
        weight_4 = grades[weight_4_sub]

        # Calculate the total points for each group
        total_points_i = weight_1 + weight_2 + weight_3 + weight_4

        response = {'total_points': total_points_i, 'cluster_name': 'Interior Design, Fashion Design, Textiles & Related'}

        return response

def cluster_14(grades, groups):
    subjects_needed = ['BIO']


    weight_1_sub = max([subj for subj in ['BIO', 'GSC'] if subj in grades], key=grades.get, default=None)
    weight_1 = grades.get(weight_1_sub, 0)
    # Remove the selected subject for Weight 1
    if weight_1_sub:
        del grades[weight_1_sub]
    # Weight 2: Always 'MATH'
    weight_2 = grades.get('MATH', 0)
    # Remove 'MATH' from `grades` if it exists
    if 'MATH' in grades:
        del grades['MATH']
    # Weight 3: Max grade from `groups[1] + groups[2]` (if subjects exist in `grades`)
    weight_3_sub = max([subj for subj in groups[1] + groups[2] if subj in grades], key=grades.get, default=None)
    weight_3 = grades.get(weight_3_sub, 0)
    # Remove the selected subject for Weight 3
    if weight_3_sub:
        del grades[weight_3_sub]
    
    # Weight 4: Max grade from `groups[2] + groups[1] + LAN + groups[3] + groups[4]`
    LAN = ['ENG', 'KIS']
    weight_4_sub = max([subj for subj in groups[2] + groups[1] + LAN + groups[3] + groups[4] if subj in grades],key=grades.get,default=None)
    weight_4 = grades.get(weight_4_sub, 0)
    # Calculate the total points
    total_points_i = weight_1 + weight_2 + weight_3 + weight_4
    # Construct the response
    response = {
        'total_points': total_points_i,
        'cluster_name': 'Sports Education, Sports Science, Sports Management & Related'
    }
    
    return response



def cluster_15(grades, groups):
    subjects_needed = ['BIO', 'CHEM']

    # Weight 1: Always "BIO"
    weight_1 = grades.get("BIO", 0)
    
    # Remove "BIO" from grades if it exists
    if "BIO" in grades:
        del grades["BIO"]
    
    # Weight 2: Always "CHEM"
    weight_2 = grades.get("CHEM", 0)
    
    # Remove "CHEM" from grades if it exists
    if "CHEM" in grades:
        del grades["CHEM"]
    
    # Weight 3: Max grade from ["MATH", "PHY"]
    weight_3_sub = max([subj for subj in ["MATH", "PHY"] if subj in grades], key=grades.get, default=None)
    weight_3 = grades.get(weight_3_sub, 0)
    
    # Remove the selected subject for Weight 3
    if weight_3_sub:
        del grades[weight_3_sub]
    
    # Weight 4: Max grade from eligible subjects in groups[2], LAN, groups[3], and groups[4]
    LAN = ["ENG", "KIS"]
    weight_4_sub = max(
        [subj for subj in groups[2] + LAN + groups[3] + groups[4] if subj in grades],
        key=grades.get,
        default=None
    )
    weight_4 = grades.get(weight_4_sub, 0)
    
    # Calculate the total points
    total_points_i = weight_1 + weight_2 + weight_3 + weight_4
    
    # Construct the response
    response = {
        'total_points': total_points_i,
        'cluster_name': 'Medicine, Nursing, Pharmacy & Related'
    }
    
    return response

def cluster_16(grades, groups):
    subjects_needed = ['HAG']

    
    # Weight 1: Always "HAG"
    weight_1 = grades.get("HAG", 0)
    
    # Remove "HAG" from grades if it exists
    if "HAG" in grades:
        del grades["HAG"]
    
    # Weight 2: Max grade from ['ENG', 'KIS']
    weight_2_sub = max([subj for subj in ['ENG', 'KIS'] if subj in grades], key=grades.get, default=None)
    weight_2 = grades.get(weight_2_sub, 0)
    
    # Remove the selected subject for Weight 2
    if weight_2_sub:
        del grades[weight_2_sub]
    
    # Weight 3: Max grade from ['MATH'] + groups[1]
    weight_3_sub = max([subj for subj in ['MATH'] + groups[1] if subj in grades], key=grades.get, default=None)
    weight_3 = grades.get(weight_3_sub, 0)
    
    # Remove the selected subject for Weight 3
    if weight_3_sub:
        del grades[weight_3_sub]
    
    # Weight 4: Max grade from groups[2] + groups[1] + groups[3] + groups[4]
    weight_4_sub = max(
        [subj for subj in groups[2] + groups[1] + groups[3] + groups[4] if subj in grades],
        key=grades.get,
        default=None
    )
    weight_4 = grades.get(weight_4_sub, 0)
    
    # Calculate the total points
    total_points_i = weight_1 + weight_2 + weight_3 + weight_4
    
    # Construct the response
    response = {
        'total_points': total_points_i,
        'cluster_name': 'Archeology'
    }
    
    return response



def cluster_17(grades, groups):
    subjects_needed = ['BIO', 'CHEM']

    
    # Weight 1: Always "BIO"
    weight_1 = grades.get("BIO", 0)
    
    # Remove "BIO" from grades if it exists
    if "BIO" in grades:
        del grades["BIO"]
    
    # Weight 2: Always "CHEM"
    weight_2 = grades.get("CHEM", 0)
    
    # Remove "CHEM" from grades if it exists
    if "CHEM" in grades:
        del grades["CHEM"]
    
    # Weight 3: Max grade from ["MATH", "PHY", "GEO"]
    weight_3_sub = max([subj for subj in ["MATH", "PHY", "GEO"] if subj in grades], key=grades.get, default=None)
    weight_3 = grades.get(weight_3_sub, 0)
    
    # Remove the selected subject for Weight 3
    if weight_3_sub:
        del grades[weight_3_sub]
    
    # Weight 4: Max grade from LAN + groups[2] + groups[1] + groups[3] + groups[4]
    LAN = ["ENG", "KIS"]
    weight_4_sub = max(
        [subj for subj in LAN + groups[2] + groups[1] + groups[3] + groups[4] if subj in grades],
        key=grades.get,
        default=None
    )
    weight_4 = grades.get(weight_4_sub, 0)
    
    # Calculate the total points
    total_points_i = weight_1 + weight_2 + weight_3 + weight_4
    
    # Construct the response
    response = {
        'total_points': total_points_i,
        'cluster_name': 'Animal Health, Nutrition, Agriculture and Production'
    }
    
    return response


def cluster_18(grades, groups):
    subjects_needed = ['GEO']

    
    # Weight 1: Always "GEO"
    weight_1 = grades.get("GEO", 0)
    
    # Remove "GEO" from grades if it exists
    if "GEO" in grades:
        del grades["GEO"]
    
    # Weight 2: Always "MATH"
    weight_2 = grades.get("MATH", 0)
    
    # Remove "MATH" from grades if it exists
    if "MATH" in grades:
        del grades["MATH"]
    
    # Weight 3: Max grade from subjects in groups[1]
    weight_3_sub = max([subj for subj in groups[1] if subj in grades], key=grades.get, default=None)
    weight_3 = grades.get(weight_3_sub, 0)
    
    # Remove the selected subject for Weight 3
    if weight_3_sub:
        del grades[weight_3_sub]
    
    # Weight 4: Max grade from subjects in groups[2] + groups[1] + groups[3] + groups[4]
    weight_4_sub = max(
        [subj for subj in groups[2] + groups[1] + groups[3] + groups[4] if subj in grades],
        key=grades.get,
        default=None
    )
    weight_4 = grades.get(weight_4_sub, 0)
    
    # Calculate the total points
    total_points_i = weight_1 + weight_2 + weight_3 + weight_4
    
    # Construct the response
    response = {
        'total_points': total_points_i,
        'cluster_name': 'Geography, Environmental Science, Natural Resources & Related'
    }
    
    return response


def cluster_19(grades, groups):
    # Calculate the total points for each group

    # Weight 1: Always "ENG"
    weight_1 = grades["ENG"]  
    # Drop the "ENG" subject from grades
    del grades['ENG']
    
    # Weight 2: Always "MATH"
    weight_2 = grades["MATH"]  
    # Drop the "MATH" subject from grades
    del grades['MATH']
    
    # Weight 3: Max grade from subjects in groups[1] + groups[2]
    weight_3_sub = max([subj for subj in groups[1] + groups[2] if subj in grades], key=grades.get) 
    weight_3 = grades[weight_3_sub]
    # Drop the selected subject for Weight 3
    del grades[weight_3_sub]
    
    # Weight 4: Max grade from subjects in groups[2] + groups[1] + groups[3] + groups[4]
    weight_4_sub = max([subj for subj in groups[2] + groups[1] + groups[3] + groups[4] if subj in grades], key=grades.get)
    weight_4 = grades[weight_4_sub]
    
    # Calculate the total points for each group
    total_points_i = weight_1 + weight_2 + weight_3 + weight_4

    # Prepare the response
    response = {'total_points': total_points_i, 'cluster_name': 'Early Childhood Development, Primary Education & Related'}

    return response


