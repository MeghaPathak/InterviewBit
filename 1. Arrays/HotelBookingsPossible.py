class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        arr = arrive
        dep = depart
        arr.sort()
        dep.sort()
        n = len(arr)
        if(n==1):
            return True
        flag = 0
        room = 1
        temp = []
        temp.append(dep[0])
        for i in range(n-1):
                if room < K:
                    temp.append(dep[i+1])
                    room+=1
                    flag = 1
                elif room == K:
                    for j in range(len(temp)):
                        if(temp[j]<=arr[i+1]):
                            temp[j]=dep[i+1]
                            flag = 1
                            break
                    else:
                        flag= 0
                        return flag
        return flag
