def get(time, distance):
    start = 0
    end = time
    while start <= end:
        mid1 = int(start + (end- start) // 3)
        mid2 = int(end - (end - start) // 3)
        d1 = (time - mid1) * mid1
        d2 = (time - mid2) * mid2
        
