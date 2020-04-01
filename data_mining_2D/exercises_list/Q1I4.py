import numpy as np
def blackBoxNormalization(arrayOfCds):
    retArray = []
    
    #choose the minimum value between the arrays lengths
    normalizedArrayLength = np.min([len(array) for array in arrayOfCds])
    
    
    for array in arrayOfCds:
        if len(array)!=normalizedArrayLength:
            arrayLen = len(array) #get the current array length
            step = arrayLen/normalizedArrayLength #find the step

            normalizedArray = []
            normalizedArray.append(array[0])
            idx,aux = 0,0.0
            
            for x in range(normalizedArrayLength-1):
                aux +=step
                a = int(aux)
                idx+=a
                aux -= a
                if idx > arrayLen-1:
                    break
                else:
                    normalizedArray.append(array[idx])
            
            retArray.append(normalizedArray)
        else:
            retArray.append(array)
    return retArray
                
        
    
    
    
arrayOfCds = [[1, 0, 3, 2, 1, 3, 2, 1, 0, 1], [0,3,2,1,2,3,1,0,3,2,1,3,2,0,1,0]]
print(blackBoxNormalization(arrayOfCds))