
class WayTooLongWords:
    def solve(self,strInputs):
        strOutputs = list()
        for line in strInputs:
            if(len(line)>10):
                line = line[0]+str(len(line)-2)+line[-1]
            strOutputs.append(line)
        return strOutputs 
            
                
        
        
        
        
if __name__ == "__main__":
    
    i = 0
    strInputs = list()
    n = int(raw_input())
    while(i<n):
        strInputs.append(raw_input()) 
        i+=1
    
    wtlw = WayTooLongWords()
    for line_output in wtlw.solve(strInputs):
        print line_output
    
    