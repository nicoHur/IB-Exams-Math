import os

# Define the range of years
years = range(1999, 2025)

# Define the months
months = ["May", "November"]

# Iterate over each year
for year in years:
    # Open the markdown file for the year
    with open(os.path.join(str(year), f"{year}.md"), "w") as f:  # 'w' mode will overwrite the existing file
        # Iterate over each month
        for month in months:
            # Write the month to the markdown file
            f.write(f"\n## {month}\n")
            
            # Get the list of files in the month directory
            files = os.listdir(os.path.join(str(year), month))
            
            # Iterate over each file
            for file in files:
                # Write the file link to the markdown file using the full relative path for file links in obsidian
                f.write(f"[[/{year}/{month}/{file}]]\n")
