# Louisiana Jail Data
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

---

## Parish Breakdown

_Last updated: 2026-05-15 02:47 UTC_

**Total inmates (latest scrape):** 25,893 across 72 parishes/jails

### Acadia Parish
**Total:** 176

| Race | Count | % |
|------|-------|---|
| White | 92 | 52.3% |
| Black | 82 | 46.6% |
| Asian/PacificIslander | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 126

| Race | Count | % |
|------|-------|---|
| White | 78 | 61.9% |
| Black | 45 | 35.7% |
| American Indian/Alaska Native | 2 | 1.6% |
| Unknown | 1 | 0.8% |

### Ascension Parish
**Total:** 496

| Race | Count | % |
|------|-------|---|
| Black | 264 | 53.2% |
| White | 201 | 40.5% |
| Unknown | 27 | 5.4% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 145

| Race | Count | % |
|------|-------|---|
| Unknown | 78 | 53.8% |
| White | 67 | 46.2% |

### Avoyelles Parish
**Total:** 385

| Race | Count | % |
|------|-------|---|
| Black | 203 | 52.7% |
| White | 178 | 46.2% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 167

| Race | Count | % |
|------|-------|---|
| White | 114 | 68.3% |
| Black | 53 | 31.7% |

### Bienville Parish
**Total:** 37

| Race | Count | % |
|------|-------|---|
| White | 23 | 62.2% |
| Unknown | 14 | 37.8% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 47

| Race | Count | % |
|------|-------|---|
| Black | 30 | 63.8% |
| White | 17 | 36.2% |

### Bossier Parish
**Total:** 1,124

| Race | Count | % |
|------|-------|---|
| Black | 621 | 55.2% |
| White | 501 | 44.6% |
| American Indian/Alaska Native | 1 | 0.1% |
| Unknown | 1 | 0.1% |

### Caddo Parish
**Total:** 1,619

| Race | Count | % |
|------|-------|---|
| Black | 1,199 | 74.1% |
| White | 388 | 24.0% |
| Unknown | 30 | 1.9% |
| Asian/PacificIslander | 2 | 0.1% |

### Calcasieu Parish
**Total:** 1,042

| Race | Count | % |
|------|-------|---|
| Black | 571 | 54.8% |
| White | 430 | 41.3% |
| Unknown | 40 | 3.8% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 604

| Race | Count | % |
|------|-------|---|
| Black | 390 | 64.6% |
| White | 195 | 32.3% |
| American Indian/Alaska Native | 19 | 3.1% |

### Cameron Parish
**Total:** 19

| Race | Count | % |
|------|-------|---|
| White | 17 | 89.5% |
| Black | 2 | 10.5% |

### Catahoula Parish
**Total:** 134

| Race | Count | % |
|------|-------|---|
| Black | 92 | 68.7% |
| White | 41 | 30.6% |
| Unknown | 1 | 0.7% |

### Claiborne Parish
**Total:** 651

| Race | Count | % |
|------|-------|---|
| Black | 396 | 60.8% |
| White | 255 | 39.2% |

### Concordia Parish
**Total:** 797

| Race | Count | % |
|------|-------|---|
| White | 449 | 56.3% |
| Black | 344 | 43.2% |
| Unknown | 4 | 0.5% |

### DeSoto Parish
**Total:** 119

| Race | Count | % |
|------|-------|---|
| Black | 72 | 60.5% |
| White | 46 | 38.7% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,046

| Race | Count | % |
|------|-------|---|
| Black | 798 | 76.3% |
| White | 196 | 18.7% |
| Unknown | 51 | 4.9% |
| Asian/PacificIslander | 1 | 0.1% |

### East Feliciana Parish
**Total:** 264

| Race | Count | % |
|------|-------|---|
| Black | 163 | 61.7% |
| White | 100 | 37.9% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 98

| Race | Count | % |
|------|-------|---|
| Black | 50 | 51.0% |
| White | 47 | 48.0% |
| Unknown | 1 | 1.0% |

### Franklin Parish
**Total:** 828

| Race | Count | % |
|------|-------|---|
| Black | 533 | 64.4% |
| White | 284 | 34.3% |
| Unknown | 10 | 1.2% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 9

| Race | Count | % |
|------|-------|---|
| Black | 8 | 88.9% |
| White | 1 | 11.1% |

### Iberia Parish
**Total:** 445

| Race | Count | % |
|------|-------|---|
| Black | 271 | 60.9% |
| White | 165 | 37.1% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 4 | 0.9% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| Black | 71 | 63.4% |
| White | 39 | 34.8% |
| Unknown | 2 | 1.8% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 149

| Race | Count | % |
|------|-------|---|
| White | 74 | 49.7% |
| Black | 70 | 47.0% |
| American Indian/Alaska Native | 3 | 2.0% |
| Asian/PacificIslander | 1 | 0.7% |
| Unknown | 1 | 0.7% |

### Jefferson Parish
**Total:** 1,193

| Race | Count | % |
|------|-------|---|
| Black | 787 | 66.0% |
| White | 394 | 33.0% |
| Unknown | 9 | 0.8% |
| Asian/PacificIslander | 3 | 0.3% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Black | 1 | 100.0% |

### LaSalle Parish
**Total:** 75

| Race | Count | % |
|------|-------|---|
| White | 54 | 72.0% |
| Black | 20 | 26.7% |
| Unknown | 1 | 1.3% |

### Lafayette Parish
**Total:** 855

| Race | Count | % |
|------|-------|---|
| Black | 548 | 64.1% |
| White | 295 | 34.5% |
| Unknown | 12 | 1.4% |

### Lafourche Parish
**Total:** 743

| Race | Count | % |
|------|-------|---|
| Black | 387 | 52.1% |
| White | 349 | 47.0% |
| American Indian/Alaska Native | 5 | 0.7% |
| Unknown | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 365

| Race | Count | % |
|------|-------|---|
| Black | 271 | 74.2% |
| White | 91 | 24.9% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 785

| Race | Count | % |
|------|-------|---|
| White | 558 | 71.1% |
| Black | 218 | 27.8% |
| Unknown | 7 | 0.9% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| Black | 103 | 78.0% |
| White | 28 | 21.2% |
| Unknown | 1 | 0.8% |

### Morehouse Parish
**Total:** 205

| Race | Count | % |
|------|-------|---|
| Black | 141 | 68.8% |
| White | 64 | 31.2% |

### Natchitoches Parish
**Total:** 196

| Race | Count | % |
|------|-------|---|
| Black | 148 | 75.5% |
| White | 44 | 22.4% |
| Unknown | 3 | 1.5% |
| Asian/PacificIslander | 1 | 0.5% |

### Oakdale Police Department
**Total:** 5

| Race | Count | % |
|------|-------|---|
| White | 3 | 60.0% |
| Black | 1 | 20.0% |
| Unknown | 1 | 20.0% |

### Opelousas Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| African American | 1 | 100.0% |

### Orleans Parish
**Total:** 1,380

| Race | Count | % |
|------|-------|---|
| Black | 1,182 | 85.7% |
| White | 174 | 12.6% |
| Unknown | 21 | 1.5% |
| Asian/PacificIslander | 3 | 0.2% |

### Ouachita Parish
**Total:** 1,295

| Race | Count | % |
|------|-------|---|
| Black | 876 | 67.6% |
| White | 402 | 31.0% |
| Unknown | 17 | 1.3% |

### Plaquemines Parish
**Total:** 639

| Race | Count | % |
|------|-------|---|
| Black | 419 | 65.6% |
| White | 200 | 31.3% |
| Unknown | 13 | 2.0% |
| Asian/PacificIslander | 6 | 0.9% |
| American Indian/Alaska Native | 1 | 0.2% |

### Pointe Coupee Parish
**Total:** 103

| Race | Count | % |
|------|-------|---|
| Black | 68 | 66.0% |
| White | 34 | 33.0% |
| Unknown | 1 | 1.0% |

### Rapides Parish
**Total:** 995

| Race | Count | % |
|------|-------|---|
| Black | 618 | 62.1% |
| White | 359 | 36.1% |
| Unknown | 16 | 1.6% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 42

| Race | Count | % |
|------|-------|---|
| Black | 23 | 54.8% |
| White | 18 | 42.9% |
| Asian/PacificIslander | 1 | 2.4% |

### Richland Parish
**Total:** 712

| Race | Count | % |
|------|-------|---|
| Black | 484 | 68.0% |
| White | 217 | 30.5% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sabine Parish
**Total:** 182

| Race | Count | % |
|------|-------|---|
| White | 102 | 56.0% |
| Black | 80 | 44.0% |

### Shreveport Police Department
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 35 | 79.5% |
| White | 9 | 20.5% |

### St. Bernard Parish
**Total:** 228

| Race | Count | % |
|------|-------|---|
| Black | 127 | 55.7% |
| White | 98 | 43.0% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.4% |

### St. Charles Parish
**Total:** 177

| Race | Count | % |
|------|-------|---|
| Unknown | 100 | 56.5% |
| White | 77 | 43.5% |

### St. Helena Parish
**Total:** 76

| Race | Count | % |
|------|-------|---|
| Black | 54 | 71.1% |
| White | 17 | 22.4% |
| Unknown | 4 | 5.3% |
| American Indian/Alaska Native | 1 | 1.3% |

### St. James Parish
**Total:** 77

| Race | Count | % |
|------|-------|---|
| Black | 60 | 77.9% |
| White | 17 | 22.1% |

### St. John the Baptist Parish
**Total:** 205

| Race | Count | % |
|------|-------|---|
| Unknown | 130 | 63.4% |
| White | 75 | 36.6% |

### St. Landry Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| Black | 70 | 62.5% |
| White | 40 | 35.7% |
| Unknown | 2 | 1.8% |

### St. Martin Parish
**Total:** 193

| Race | Count | % |
|------|-------|---|
| White | 95 | 49.2% |
| Black | 90 | 46.6% |
| Unknown | 7 | 3.6% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 258

| Race | Count | % |
|------|-------|---|
| Black | 133 | 51.6% |
| White | 123 | 47.7% |
| American Indian/Alaska Native | 1 | 0.4% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 826

| Race | Count | % |
|------|-------|---|
| White | 431 | 52.2% |
| Black | 354 | 42.9% |
| Unknown | 36 | 4.4% |
| Asian/PacificIslander | 3 | 0.4% |
| American Indian/Alaska Native | 2 | 0.2% |

### Sulphur Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| White | 13 | 86.7% |
| Black | 2 | 13.3% |

### Tangipahoa Parish
**Total:** 649

| Race | Count | % |
|------|-------|---|
| Black | 399 | 61.5% |
| White | 249 | 38.4% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 556

| Race | Count | % |
|------|-------|---|
| Black | 368 | 66.2% |
| White | 173 | 31.1% |
| Unknown | 15 | 2.7% |

### Terrebonne Parish
**Total:** 477

| Race | Count | % |
|------|-------|---|
| Black | 247 | 51.8% |
| White | 223 | 46.8% |
| American Indian/Alaska Native | 6 | 1.3% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| White | 73 | 55.7% |
| Black | 56 | 42.7% |
| Unknown | 2 | 1.5% |

### Vernon Parish
**Total:** 157

| Race | Count | % |
|------|-------|---|
| White | 104 | 66.2% |
| Black | 50 | 31.8% |
| Unknown | 2 | 1.3% |
| Asian/PacificIslander | 1 | 0.6% |

### Ville Platte Police Department
**Total:** 31

| Race | Count | % |
|------|-------|---|
| Black | 18 | 58.1% |
| White | 12 | 38.7% |
| Unknown | 1 | 3.2% |

### Washington Parish
**Total:** 168

| Race | Count | % |
|------|-------|---|
| Black | 90 | 53.6% |
| White | 78 | 46.4% |

### Webster Parish
**Total:** 447

| Race | Count | % |
|------|-------|---|
| White | 220 | 49.2% |
| Black | 220 | 49.2% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 3 | 0.7% |

### West Baton Rouge Parish
**Total:** 141

| Race | Count | % |
|------|-------|---|
| Black | 91 | 64.5% |
| White | 44 | 31.2% |
| Unknown | 5 | 3.5% |
| Asian/PacificIslander | 1 | 0.7% |

### West Carroll Parish
**Total:** 26

| Race | Count | % |
|------|-------|---|
| White | 23 | 88.5% |
| Black | 3 | 11.5% |

### West Felician Parish
**Total:** 182

| Race | Count | % |
|------|-------|---|
| Black | 116 | 63.7% |
| White | 66 | 36.3% |

### Winn Parish
**Total:** 145

| Race | Count | % |
|------|-------|---|
| Black | 73 | 50.3% |
| White | 72 | 49.7% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
