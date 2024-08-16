dominoes = ".L.R....L"
dominoes = list(dominoes)
endpointL = [0, ""]
endpointR = []
for index,val in enumerate(dominoes):
    if val == "L":
        endpointR = [index, val]
        isEven = (index-endpointL[0]) % 2 == 0
        midpoint = 0
        if isEven:
            midpoint = (index-endpointL[0]) / 2 + endpointL[0] - 1
        else:
            midpoint = (index - endpointL[0]+1) / 2 + endpointL[0] - 1
        toChange = "L"
        doChange = True
        for i in range(index,endpointL[0]-1,-1):
            print(midpoint)
            if i == midpoint and endpointL[1] == "R":
                if isEven:
                    toChange = "."
                    doChange = False
                toChange = "R"
            if doChange:
                dominoes[i] = toChange
            doChange = True
        endpointL = [index, val]
    if val == "R":
        endpointL = [index, val]
print(dominoes)