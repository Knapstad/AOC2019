
goal=19690720

for c in range(100):
    noun=c
    
    for y in range(100):
        print("reset input")
        inp=[1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,2,9,19,23,2,13,23,27,1,6,27,31,2,6,31,35,2,13,35,39,1,39,10,43,2,43,13,47,1,9,47,51,1,51,13,55,1,55,13,59,2,59,13,63,1,63,6,67,2,6,67,71,1,5,71,75,2,6,75,79,1,5,79,83,2,83,6,87,1,5,87,91,1,6,91,95,2,95,6,99,1,5,99,103,1,6,103,107,1,107,2,111,1,111,5,0,99,2,14,0,0]
        verb=y
        print(f" {noun} {verb}")
        inp[2]=y
        inp[1]=noun

        for i in range(0,len(inp)+1,4):
            if inp[i]==99:
                break
            a=inp[i+1]
            b=inp[i+2]
            c=inp[i+3]
            if inp[i]==1:
                inp[c]=inp[a]+inp[b]
            elif inp[i]==2:
                inp[c]=inp[a]*inp[b]
            else:
                print(f"error pos{i}")
        print("checking ans")
        print(f"{inp[0]}  {goal}")
        if inp[0]==goal:
            print(f"verb {verb}, noun {noun} ans = {100*verb+noun}")
            break