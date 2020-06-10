def bubbleSort(numbers): 
    n = len(numbers) 
    for i in range(len(numbers)-1):
        
        for j in range(0, len(numbers)-i-1):
            
            if numbers[j] > numbers[j+1] :
                
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

def selectionSort(numbers):
    for i in range(len(numbers)):
        
        s = i 
        for j in range(i+1, len(numbers)): 
            if numbers[s] > numbers[j]: 
                s = j 
         
        numbers[i], numbers[s] = numbers[s], numbers[i]
    return numbers

print(bubbleSort([3,4,6,1,2,8,7]))
print(selectionSort([3,4,6,1,2,8,7]))
