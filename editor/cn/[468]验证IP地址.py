# leetcode submit region begin(Prohibit modification and deletion)
import string


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.count('.') == 3:
            ipv4_ls = queryIP.split('.')
            for i in ipv4_ls:
                if i.isdigit() and 0 <= int(i) <= 255 and str(int(i)) == i:
                    continue
                else:
                    return 'Neither'
            return 'IPv4'
        elif queryIP.count(':') == 7:
            ipv6_ls = queryIP.split(':')
            st = 'abcdefABCDEF'
            for i in ipv6_ls:
                if 1 <= len(i) <= 4:
                    for j in i:
                        if j.isdigit() or j in st:
                            continue
                        else:
                            return 'Neither'
                else:
                    return 'Neither'
            return 'IPv6'
        else:
            return 'Neither'


# leetcode submit region end(Prohibit modification and deletion)
addr = "1e1.4.5.6"
x = Solution().validIPAddress(addr)
print(x)
