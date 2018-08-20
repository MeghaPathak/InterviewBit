class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        
        indent = ""
        o =[]
        curr = ""
        
        for index, c in enumerate(A):
            if(c == "[" or c == "{"):
                #if the case is :
                    #{
                    #   A:"B",
                    #   C:
                    #       {
                    # Then curr mein C: tha, jo aapko push karna padega
                if(curr):
                    o.append(indent+curr)
                o.append(indent + c)
                curr =""
                indent+='\t'
            
            elif(c == "]" or c == "}"):
                #if the case is :
                    #   {
                    #       G:"H",
                    #       I:"J" <-- save this first, then move to next
                    #   }
                    #}
                if(curr):
                    o.append(indent + curr)
                indent = indent[:-1]
                o.append(indent+c)
                curr = ""
            
            elif(c == ","):
                if(A[index-1] == "]" or A[index-1] == "}"):
                #D:
                #   {
                #    E:"M"
                #   },
                #   F: "G"
                #Then here you need to go back to } and add a , to it
                    o[-1] = o[-1] + c
                else:
                    o.append(indent + curr + c)
                    curr=""
            
            elif c == " ":
                curr = ""
                
            else :
                curr = curr + c

        return o