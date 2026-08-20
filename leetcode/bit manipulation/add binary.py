class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        out = ''
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0

            total = x + y + carry

            out += str(total % 2)
            carry = total // 2

            i -= 1
            j -= 1

        if carry:
            out += '1'

        return out[::-1]