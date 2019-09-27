"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
"""

def defangIPaddr(address):
    l_address = list(address)
    for i in range(len(l_address)):
        if l_address[i] == ".":
            l_address[i] = "[.]"
    return "".join(l_address)
