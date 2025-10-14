def wed(q1):
    if q1 <= 0:
        print('\033[95m  DONE!!🔥🤍')
        return
    else:
        for i in range(q1):
            print('🎁', end='')
        print()
        wed(q1-1)
        
            
wed((10))

