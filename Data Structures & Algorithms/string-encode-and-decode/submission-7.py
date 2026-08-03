class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""       

        encoded_string = ""
        for string in strs:
            encoded_string += (f"{len(string)}#{string}")
        
        return encoded_string
        

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        decoded_strings = []

        left_ptr = 0
        
        while left_ptr < len(s):
            right_ptr = left_ptr

            while s[right_ptr] != "#":
                right_ptr += 1
            
            length = int(s[left_ptr:right_ptr])
            string_start = right_ptr + 1
            string_end = string_start + length
            decoded_strings.append(s[string_start:string_end])

            left_ptr = string_end 

        
        return decoded_strings
