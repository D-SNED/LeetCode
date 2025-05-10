class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        s = queryIP.split(".")
        ip_type = "IPv4"

        if len(s) != 4:
            s = queryIP.split(":")
            
            if len(s) != 8:
                ip_type = "Neither"
            else:
                ip_type = "IPv6"

        if ip_type == "IPv4":
            for num in s:
                if len(num) > 1 and num[0] == "0":
                    ip_type = "Neither"
                    break 
                
                try:
                    val = int(num)
                except:
                    ip_type = "Neither"
                    break

                if val < 0 or val > 255:
                    ip_type = "Neither"
                    break

        elif ip_type == "IPv6":
            for num in s:
                if len(num) > 4 or len(num) < 1:
                    ip_type = "Neither"
                    break
                try:
                    num_val = int("0x" + num.lower(), 16)
                except:
                    ip_type = "Neither"
                    break

        return ip_type
                
                    

        