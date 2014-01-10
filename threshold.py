def threshold(h):
    pixels = 0
    for value in h:
        pixels += value
    
    Wb = 0
    for value in h[:128]:
       Wb += value 
        
    
