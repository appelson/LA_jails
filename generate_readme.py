import pandas as pd
import glob
import os
from datetime import datetime

STATIC_README = """# Louisiana Jail Data
An automated scraper that collects inmate roster data from Louisiana parish jails and police departments using GitHub Actions.
![Race Breakdown](race.png)
## Updates
- **`April 24th, 2026`**: Updated to fix the encryption, to instead make it a cypher. This allows us to compare encrypted names / encrypted dates of birth across time. We also condensed the past 30+ days of downloads with the previous rosters. This gives us 7,000,000+ records.
## What it does
Every day at 6:00 PM CST, the GitHub Actions workflow scrapes inmate roster tables from 72 Louisiana parish jails and police departments listed in `links.csv`. This includes 61 out of 64 parishes and 11 municipal jails. Scraped data is saved as a timestamped CSV in the `downloads/` folder and committed to the repo. Sensitive fields (`Name` and `DOB`) are encrypted using RSA public-key encryption before being committed. If you need this information, please contact me at `eappelson@laaclu.org`.
> [!NOTE] 
> This data includes both those held pretrial and post-conviction. Additionally, historical rosters were scraped from [here](https://jailrosters.org/), and the resulting dataframe is saved in `downloads` as `rosters.rds`. Sensitive data is hashed.
## Files
- `script.py`: Scrapes all jails and encrypts sensitive columns before saving
- `encrypt.py`: Encryption utility
- `decrypt.py`: Decrypts CSVs locally using the private key
- `jail_scraper.r`: Scrapes data from the past year saved [here](https://jailrosters.org/).
- `links.csv`: List of 80 jail roster URLs with associated jail names
- `.github/workflows/main.yml`: GitHub Actions workflow that runs the scraper
## Warning
This code should NEVER be replicated or repurposed to scrape and track individuals held in jail. This project exists solely for research and accountability purposes. Do not misuse this code or data to monitor, target, or surveil incarcerated individuals.
"""

def load_latest_csv():
    files = glob.glob("downloads/scraped_data_*.csv")
    if not files:
        print("No scraped data found.")
        return None
    latest = max(files, key=os.path.getmtime)
    print(f"Using: {latest}")
    return pd.read_csv(latest)

def build_parish_section(df):
    lines = []
    lines.append("---\n")
    lines.append("## Parish Breakdown\n")
    lines.append(f"_Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}_\n")

    total = len(df)
    num_parishes = df["jail"].nunique()
    lines.append(f"**Total inmates (latest scrape):** {total:,} across {num_parishes} parishes/jails\n")

    # Detect race column flexibly
    race_col = next(
        (c for c in df.columns if "race" in c.lower()),
        None
    )

    for jail, group in df.groupby("jail"):
        lines.append(f"### {jail}")
        lines.append(f"**Total:** {len(group):,}\n")

        if race_col:
            race_counts = (
                group[race_col]
                .fillna("Unknown")
                .value_counts()
                .reset_index()
            )
            race_counts.columns = ["Race", "Count"]
            race_counts["Percent"] = (
                race_counts["Count"] / len(group) * 100
            ).round(1)

            lines.append("| Race | Count | % |")
            lines.append("|------|-------|---|")
            for _, row in race_counts.iterrows():
                lines.append(f"| {row['Race']} | {row['Count']:,} | {row['Percent']}% |")
            lines.append("")
        else:
            lines.append("_Race data not available for this jail._\n")

    return "\n".join(lines)

def main():
    df = load_latest_csv()

    if df is not None:
        parish_section = build_parish_section(df)
    else:
        parish_section = "---\n\n## Parish Breakdown\n\n_No scraped data available yet._\n"

    readme = STATIC_README.rstrip() + "\n\n" + parish_section

    with open("README.md", "w") as f:
        f.write(readme)
    print("README.md updated.")

if __name__ == "__main__":
    main()
