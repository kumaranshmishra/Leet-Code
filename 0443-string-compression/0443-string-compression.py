class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0
        i = 0
        n = len(chars)
        while i < n:
            curr = chars[i]
            count = 0
            while i < n and chars[i] == curr:
                count += 1
                i += 1
            chars[write] = curr
            write += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write
         

        