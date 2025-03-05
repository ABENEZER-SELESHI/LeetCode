class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        n = len(command)
        result = ""
        while i < n:
            if command[i] == "G":
                result += command[i]
                i += 1
            elif command[i:i+2] == "()":
                result += "o"
                i += 2
            elif command[i:i+4] == "(al)":
                result += "al"
                i += 4
        return result