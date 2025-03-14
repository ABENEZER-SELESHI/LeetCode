class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        row = [1]

        def pascal(row, k):
            if len(row) == k+1:
                return row
            temp = [1]
            for i in range(1, len(row)):
                temp.append(row[i]+row[i-1])
            temp.append(1)
            return pascal(temp, k)
        
        return pascal(row, rowIndex)