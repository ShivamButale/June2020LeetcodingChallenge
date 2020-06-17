class Solution:
    def validIPAddress(self, IP: str) -> str:
        if "." in IP:
            elem = IP.split(".")
            
            if len(elem)!=4:
                return "Neither"
            
            for i in elem:
                if len(i)==0:
                    return "Neither"
                if  len(i)>1 and i[0]=="0":
                    return "Neither"
                if not i.isnumeric() or int(i)>255:
                    return "Neither"
            return "IPv4"
        
        elif ":" in IP:
            valid = "01234567890abcdefABCDEF"
            elem = IP.split(":")
            
            if len(elem)!=8:
                return "Neither"
            
            for i in elem:
                if len(i)==0:
                    return "Neither"
                if len(i) > 4:
                    return "Neither"
                for j in i:
                    if j not in valid:
                        return "Neither"
            return "IPv6"
        return "Neither"
