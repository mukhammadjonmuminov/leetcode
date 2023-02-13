class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_address = address.replace('.', '[.]')
        return new_address

if __name__ == "__main__":
    ip_address = Solution()
    print(ip_address.defangIPaddr('1.1.1.1'))