file_name = input("Enter the file name: ")

try:
    with open(file_name, "r") as file:
        total = 0
        count = 0

        for line in file:
            if line.startswith("X-DSPAM-Confidence:"):
                try:
            
                    confidence = float(line.split(":")[1])
                    total += confidence
                    count += 1
                except ValueError:
                    print("Error: Unable to parse the confidence value on line:", line)

        if count > 0:
            average = total / count
            print("Average confidence:", average)
        else:
            print("No X-DSPAM-Confidence lines found in the file.")

except FileNotFoundError:
    print(" The file does not exist.")