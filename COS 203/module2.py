def cal_gradescore():
    resp=True
    while resp==True:
        try:
            score=float(input("Enter you score: "))
            resp=False
        except:
            print("Invalid")
    

    if score >50 and score < 101:
        grade="Pass"
    elif score<50:
        grade ="Fail"
        
    
    return grade,score