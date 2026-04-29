#You have a list of server names. Use a for loop to simulate checking their status and print:
#"Server <name> is UP" if index is even
#"Server <name> is DOWN" if index is odd

servers = ["web1", "web2", "db1", "cache1"]
for index, server in enumerate(servers):
    if index % 2 == 0:
        print(f"{server} is up")
    else:
        print(f"{server} is down")