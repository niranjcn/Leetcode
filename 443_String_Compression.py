class Solution:
    def compress(self, chars: list[str]) -> int:
        read = 0
        write = 0

        while read < len(chars):
            curr = chars[read]
            start = read

            while read < len(chars) and curr == chars[read]:
                read += 1
            
            count = read - start
            chars[write] = curr
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write