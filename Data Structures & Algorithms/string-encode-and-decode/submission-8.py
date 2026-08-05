class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        string_parts = []
        for word in strs:
            string_parts.append(f"{len(word)}#{word}")
        print(string_parts)
        
        return "".join(string_parts)

    def decode(self, s: str) -> List[str]:
        print(s)
        l_ptr = 0
        decoded_strings = []

        while l_ptr < len(s):
            r_ptr = l_ptr

            while s[r_ptr] != "#":
                r_ptr += 1
            print(r_ptr)
            length = int(s[l_ptr:r_ptr])
            string_start = r_ptr + 1
            string_end = string_start + length
            decoded_strings.append(s[string_start:string_end])

            l_ptr = string_end

        return decoded_strings

