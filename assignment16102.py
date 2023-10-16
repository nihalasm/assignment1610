
unique_hosts = []

try:

    with open("mbox.txt", "r") as file:
        for line in file:
            if line.startswith("From:"):
                parts = line.split()
                if len(parts) > 1:
                    email = parts[1]
                    host = email.split("@")[1]
                    print(host)
                    if host not in unique_hosts:
                        unique_hosts.append(host)

    print(f"Number of unique hosts: {len(unique_hosts)}")

except FileNotFoundError:
    print("Error: The 'mbox.txt' file does not exist.")