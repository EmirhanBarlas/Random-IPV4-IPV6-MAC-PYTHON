import random

def generate_random_mac_address():
    mac = [random.randint(0x00, 0xff) for _ in range(6)] # Generate 6 random numbers between 0 and 255
    mac_address = ':'.join(map(lambda x: "%02x" % x, mac)) 
    return mac_address

def generate_random_ipv4_address():
    ipv4 = '.'.join(map(str, (random.randint(0, 255) for _ in range(4)))) # Generate 4 random numbers between 0 and 255
    return ipv4

def generate_random_ipv6_address():
    ipv6 = ':'.join('{:04x}'.format(random.randint(0, 0xffff)) for _ in range(8)) # Generate 8 random 4 digit hex numbers
    return ipv6

random_mac = generate_random_mac_address() # Call the function to generate a random MAC address
random_ipv4 = generate_random_ipv4_address() # Call the function to generate a random IPv4 address
random_ipv6 = generate_random_ipv6_address() # Call the function to generate a random IPv6 address

user_input = input("Enter 1 = 'ipv4' or 2 = 'ipv6' or 3 ='MAC' to generate the corresponding address: ")

if user_input == '1':
    random_ipv4 = generate_random_ipv4_address()
    print("Random IPv4 Address:", random_ipv4)
if user_input == '2':
    random_ipv6 = generate_random_ipv6_address()
    print("Random IPv6 Address:", random_ipv6)
if user_input == '3':
    random_mac = generate_random_mac_address()
    print("Random MAC Address:", random_mac)    
else:
    print("Invalid input. Please enter 1 = 'ipv4' or 2 = 'ipv6' or 3 ='MAC'")