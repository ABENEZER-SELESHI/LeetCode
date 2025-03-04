class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        n = len(answers)
        store = 0
        redandunt = set()
        redandunt.add(0)
        store += answers.count(0)
        for i in range(n):
            if answers[i] not in redandunt and answers.count(answers[i]) <= answers[i]+1:
                store += answers[i] + 1
                redandunt.add(answers[i])
            elif answers[i] not in redandunt and answers.count(answers[i]) > answers[i]+1:
                div = answers.count(answers[i])//(answers[i]+1)
                rem = 0
                if answers.count(answers[i]) % (answers[i]+1) != 0:
                    rem = 1
                store += (answers[i] + 1) * (div + rem)
                redandunt.add(answers[i])
        return store