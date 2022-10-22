def solution(survey, choices):
    answer = ''
    charc = [0]*26
    for i in range(len(survey)):
        if(choices[i] < 4):
            idx = ord(survey[i][0])-65
            charc[idx] += 4-choices[i]
        elif(choices[i] > 4):
            idx = ord(survey[i][1])-65
            charc[idx] += choices[i]-4
            
    if(charc[ord("R")-65] < charc[ord("T")-65]):
        answer += "T"
    else:
        answer += "R"
    
    if(charc[ord("C")-65] < charc[ord("F")-65]):
        answer += "F"
    else:
        answer += "C"
        
    if(charc[ord("J")-65] < charc[ord("M")-65]):
        answer += "M"
    else:
        answer += "J"
        
    if(charc[ord("A")-65] < charc[ord("N")-65]):
        answer += "N"
    else:
        answer += "A"
    
    return answer