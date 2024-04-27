import os

# Define the range of years
years = range(1999, 2025)

# Define the months
months = ["May", "November"]

# Iterate over each year
for year in years:
    # Create a directory for the year if it does not exist
    os.makedirs(str(year), exist_ok=True)
    
    # Iterate over each month
    for month in months:
        # Create a directory for the month inside the year directory if it does not exist
        os.makedirs(os.path.join(str(year), month), exist_ok=True)
    
    # Create a markdown file named with the year inside the year directory
    with open(os.path.join(str(year), f"{year}.md"), "w") as f:
        f.write(f"# Year {year}\\n")
