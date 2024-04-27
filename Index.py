import os

# Define the range of years
years = range(1999, 2025)

# Define the months
months = ["May", "November"]

# Define the languages
languages = ["English Papers", "Spanish Papers", "French Papers"]

# Iterate over each year
for year in years:
    # Iterate over each month
    for month in months:
        # Open the markdown file for the month in write mode to clear previous content
        with open(os.path.join(str(year), month, f"{month}.md"), "w") as f:
            # Write the year to the markdown file
            f.write(f"# {year}\n\n")
            
            # Write the month to the markdown file
            # f.write(f"## {month}\n")
            
            # Link to the year file
            f.write(f"[[/{year}/{year}.md]]\n\n")
            
            # Iterate over each language
            for language in languages:
                # Write the language section to the markdown file
                f.write(f"### {language}\n")
                
                # Get the list of files in the language folder
                language_folder = os.path.join(str(year), month, language)
                if os.path.exists(language_folder):
                    files = os.listdir(language_folder)
                    
                    # Iterate over each file
                    for file in files:
                        # Write the file link to the markdown file using the full relative path for file links in obsidian
                        f.write(f"[[/{year}/{month}/{language}/{file}]]\n")
                        
            # Get the list of files in the month directory (excluding language folders)
            month_files = [file for file in os.listdir(os.path.join(str(year), month)) if file not in languages]
            
            # Write the files that are not in language folders
            if month_files:
                f.write(f"\n### Other Files\n")
                for file in month_files:
                    f.write(f"[[/{year}/{month}/{file}]]\n")
