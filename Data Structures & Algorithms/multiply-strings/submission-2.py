class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans_arr = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                pos = i + j + 1

                total = int(num1[i]) * int(num2[j]) + ans_arr[pos]

                ans_arr[pos] = total % 10
                ans_arr[pos - 1] += total // 10

        result = ''.join(map(str, ans_arr)).lstrip('0')

        return result or "0"