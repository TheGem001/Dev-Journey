import os
import re

def update_readme():
    # 1. Define the range where the table lives
    start_marker = ""
    end_marker = ""
    
    # 2. Scan directories that start with "Day-"
    entries = []
    for item in sorted(os.listdir(".")):
        if os.path.isdir(item) and item.startswith("Day-"):
            # Folder name format expected: Day-01-Topic-Name
            parts = item.split("-")
            day_num = f"Day {parts[1]}"
            topic = " ".join(parts[2:])
            link = f"./{item}"
            
            # Add row to table
            entries.append(f"| [{day_num}]({link}) | {topic} | See Code | ✅ |")

    # 3. Build the new table
    new_table = f"{start_marker}\n| Day | Topic | Details | Status |\n| :--- | :--- | :--- | :--- |\n"
    new_table += "\n".join(entries)
    new_table += f"\n{end_marker}"

    # 4. Read the current README
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # 5. Replace the old table with the new one
    pattern = re.compile(f"{re.escape(start_marker)}.*?{re.escape(end_marker)}", re.DOTALL)
    new_content = pattern.sub(new_table, content)

    # 6. Save back to README
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print("✅ README.md updated with latest days!")

if __name__ == "__main__":
    update_readme()
