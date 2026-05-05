class Solution:
    def defangIPaddr(self, address: str) -> str:
        split_address = address.split(".")

        defanged = ""

        for i in range(len(split_address)):
            if i < len(split_address) - 1:
                defanged += split_address[i] + "[.]"
            else:
                defanged += split_address[i]

        return defanged