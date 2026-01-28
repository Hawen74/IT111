import os

# FUNCTION SearchLogs(pattern)
#     PRINT "Scanning log files..."
#     SET found TO False
def SearchLogs(pattern):
    print("Scanning log files...")
    found = False

#     FOR each file IN current directory
#         IF file is NOT a log file
#             SKIP to next file
    for filename in os.listdir("."):
        if not filename.endswith(".log"):
            continue

#         TRY
#             OPEN file
#             FOR each line IN file
#                 IF line contains pattern
#                     PRINT "FOUND in file"
#                     SET found TO True
#                     STOP checking this file
#         CATCH error
#             PRINT "SKIPPED file (cannot read)"
        try:
            f = open(filename, "r")
            for line in f:
                if pattern in line:
                    print(f"FOUND in {filename}")
                    found = True
                    break
        except: 
            print(f"SKIPPED {filename} (cannot read)")

#     IF found IS False
#         PRINT "No matching entries found."
    if not found:
        print("No matching entries found.")

# FUNCTION Main()
#     PRINT "System Log Search Tool"
#     PRINT "---------------------"
def Main():
    print("System Log Search Tool")
    print("---------------------")
    
#     INPUT pattern FROM user
#     REMOVE leading and trailing spaces from pattern
    pattern = input("Input search pattern: ").strip()

#     IF pattern IS empty
#         PRINT "Search pattern cannot be empty."
#         STOP
    if not pattern:
        print("Search pattern cannot be empty.")
        return

#     CALL SearchLogs(pattern)
    SearchLogs(pattern)

# IF program is executed directly
#     CALL Main()
if __name__ == "__main__":
    Main()