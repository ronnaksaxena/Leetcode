class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        i = 0
        width = 0
        curLine = []
        
        while i < len(words):
            curWord = words[i]
            # Can add word to line
            if width + len(curWord) <= maxWidth:
                curLine.append(curWord)
                width += len(curWord) + 1 # add 1 for space
                i += 1
            else:
                # + len(curLine) becuase haven't actually added spaces yet
                # incremented width + 1 as a placeholder
                spaces = maxWidth - width + len(curLine)
                # Allocate equal number of spaces to all words except last
                j = 0
                added = 0
                while added < spaces:
                    if j >= len(curLine)-1:
                        j = 0
                    curLine[j] += ' '
                    added += 1
                    j += 1
                # Add processesed line to output
                output.append(''.join(curLine))
                # Reset vars
                width = 0
                curLine = []
        # Add 1 space between every word besides last
        for j in range(len(curLine)-1):
            curLine[j] += ' '
        curLine[-1] += ' ' * (maxWidth-width+1)
        output.append(''.join(curLine))
        return output
                
