'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
'''
def convert(self, s: str, numRows: int) -> str:
    if numRows==1:
        return s
    rows = [''] * min(numRows, len(s))
    row=0
    down=False
    for i in s:
        rows[row] += i
        if row==0 or row==numRows-1:
            down= not down
        if down:
            row+=1
        else:
            row-=1
    return ''.join(rows)
