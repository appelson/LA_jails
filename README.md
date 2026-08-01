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

_Last updated: 2026-08-01 02:22 UTC_

**Total inmates (latest scrape):** 26,525 across 71 parishes/jails

### Acadia Parish
**Total:** 163

| Race | Count | % |
|------|-------|---|
| White | 90 | 55.2% |
| Black | 71 | 43.6% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 121

| Race | Count | % |
|------|-------|---|
| White | 76 | 62.8% |
| Black | 41 | 33.9% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 2 | 1.7% |

### Ascension Parish
**Total:** 505

| Race | Count | % |
|------|-------|---|
| Black | 268 | 53.1% |
| White | 200 | 39.6% |
| Unknown | 33 | 6.5% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 162

| Race | Count | % |
|------|-------|---|
| Unknown | 92 | 56.8% |
| White | 70 | 43.2% |

### Beauregard Parish
**Total:** 176

| Race | Count | % |
|------|-------|---|
| White | 120 | 68.2% |
| Black | 56 | 31.8% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 14

| Race | Count | % |
|------|-------|---|
| White | 7 | 50.0% |
| Black | 7 | 50.0% |

### Bossier City Police Department
**Total:** 69

| Race | Count | % |
|------|-------|---|
| Black | 45 | 65.2% |
| White | 24 | 34.8% |

### Bossier Parish
**Total:** 1,120

| Race | Count | % |
|------|-------|---|
| Black | 629 | 56.2% |
| White | 489 | 43.7% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Caddo Parish
**Total:** 1,703

| Race | Count | % |
|------|-------|---|
| Black | 1,285 | 75.5% |
| White | 390 | 22.9% |
| Unknown | 28 | 1.6% |

### Calcasieu Parish
**Total:** 1,095

| Race | Count | % |
|------|-------|---|
| Black | 599 | 54.7% |
| White | 453 | 41.4% |
| Unknown | 42 | 3.8% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 615

| Race | Count | % |
|------|-------|---|
| Black | 395 | 64.2% |
| White | 204 | 33.2% |
| American Indian/Alaska Native | 15 | 2.4% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 21

| Race | Count | % |
|------|-------|---|
| White | 21 | 100.0% |

### Catahoula Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 92 | 70.8% |
| White | 37 | 28.5% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 649

| Race | Count | % |
|------|-------|---|
| Black | 401 | 61.8% |
| White | 248 | 38.2% |

### Concordia Parish
**Total:** 825

| Race | Count | % |
|------|-------|---|
| White | 470 | 57.0% |
| Black | 355 | 43.0% |

### DeSoto Parish
**Total:** 124

| Race | Count | % |
|------|-------|---|
| Black | 73 | 58.9% |
| White | 50 | 40.3% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,269

| Race | Count | % |
|------|-------|---|
| Black | 974 | 76.8% |
| White | 235 | 18.5% |
| Unknown | 57 | 4.5% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### East Feliciana Parish
**Total:** 282

| Race | Count | % |
|------|-------|---|
| Black | 185 | 65.6% |
| White | 95 | 33.7% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 157

| Race | Count | % |
|------|-------|---|
| Black | 94 | 59.9% |
| White | 62 | 39.5% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 852

| Race | Count | % |
|------|-------|---|
| Black | 563 | 66.1% |
| White | 285 | 33.5% |
| Unknown | 4 | 0.5% |

### Hammond Police Department
**Total:** 25

| Race | Count | % |
|------|-------|---|
| Black | 11 | 44.0% |
| White | 11 | 44.0% |
| Unknown | 3 | 12.0% |

### Iberia Parish
**Total:** 477

| Race | Count | % |
|------|-------|---|
| Black | 287 | 60.2% |
| White | 178 | 37.3% |
| Unknown | 6 | 1.3% |
| Asian/PacificIslander | 5 | 1.0% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 45

| Race | Count | % |
|------|-------|---|
| Black | 27 | 60.0% |
| White | 18 | 40.0% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 163

| Race | Count | % |
|------|-------|---|
| White | 85 | 52.1% |
| Black | 75 | 46.0% |
| American Indian/Alaska Native | 2 | 1.2% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,189

| Race | Count | % |
|------|-------|---|
| Black | 767 | 64.5% |
| White | 415 | 34.9% |
| Unknown | 6 | 0.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 73

| Race | Count | % |
|------|-------|---|
| White | 48 | 65.8% |
| Black | 24 | 32.9% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 844

| Race | Count | % |
|------|-------|---|
| Black | 556 | 65.9% |
| White | 277 | 32.8% |
| Unknown | 11 | 1.3% |

### Lafourche Parish
**Total:** 770

| Race | Count | % |
|------|-------|---|
| Black | 395 | 51.3% |
| White | 371 | 48.2% |
| American Indian/Alaska Native | 3 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 364

| Race | Count | % |
|------|-------|---|
| Black | 268 | 73.6% |
| White | 93 | 25.5% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 822

| Race | Count | % |
|------|-------|---|
| White | 581 | 70.7% |
| Black | 230 | 28.0% |
| Unknown | 8 | 1.0% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| Black | 121 | 80.1% |
| White | 29 | 19.2% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 202

| Race | Count | % |
|------|-------|---|
| Black | 149 | 73.8% |
| White | 53 | 26.2% |

### Natchitoches Parish
**Total:** 182

| Race | Count | % |
|------|-------|---|
| Black | 138 | 75.8% |
| White | 40 | 22.0% |
| Unknown | 4 | 2.2% |

### Oakdale Police Department
**Total:** 4

| Race | Count | % |
|------|-------|---|
| White | 4 | 100.0% |

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
**Total:** 1,332

| Race | Count | % |
|------|-------|---|
| Black | 896 | 67.3% |
| White | 422 | 31.7% |
| Unknown | 14 | 1.1% |

### Plaquemines Parish
**Total:** 664

| Race | Count | % |
|------|-------|---|
| Black | 430 | 64.8% |
| White | 210 | 31.6% |
| Unknown | 12 | 1.8% |
| Asian/PacificIslander | 10 | 1.5% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 119

| Race | Count | % |
|------|-------|---|
| Black | 74 | 62.2% |
| White | 42 | 35.3% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.8% |

### Rapides Parish
**Total:** 1,041

| Race | Count | % |
|------|-------|---|
| Black | 655 | 62.9% |
| White | 370 | 35.5% |
| Unknown | 14 | 1.3% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 39

| Race | Count | % |
|------|-------|---|
| Black | 20 | 51.3% |
| White | 18 | 46.2% |
| Asian/PacificIslander | 1 | 2.6% |

### Richland Parish
**Total:** 707

| Race | Count | % |
|------|-------|---|
| Black | 488 | 69.0% |
| White | 211 | 29.8% |
| Unknown | 5 | 0.7% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 188

| Race | Count | % |
|------|-------|---|
| White | 108 | 57.4% |
| Black | 77 | 41.0% |
| Unknown | 2 | 1.1% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 40

| Race | Count | % |
|------|-------|---|
| Black | 32 | 80.0% |
| White | 8 | 20.0% |

### St. Bernard Parish
**Total:** 231

| Race | Count | % |
|------|-------|---|
| Black | 134 | 58.0% |
| White | 92 | 39.8% |
| Asian/PacificIslander | 3 | 1.3% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 167

| Race | Count | % |
|------|-------|---|
| Unknown | 97 | 58.1% |
| White | 70 | 41.9% |

### St. Helena Parish
**Total:** 41

| Race | Count | % |
|------|-------|---|
| Black | 29 | 70.7% |
| White | 12 | 29.3% |

### St. James Parish
**Total:** 78

| Race | Count | % |
|------|-------|---|
| Black | 66 | 84.6% |
| White | 12 | 15.4% |

### St. John the Baptist Parish
**Total:** 227

| Race | Count | % |
|------|-------|---|
| Unknown | 151 | 66.5% |
| White | 76 | 33.5% |

### St. Landry Parish
**Total:** 128

| Race | Count | % |
|------|-------|---|
| Black | 85 | 66.4% |
| White | 41 | 32.0% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 210

| Race | Count | % |
|------|-------|---|
| Black | 106 | 50.5% |
| White | 96 | 45.7% |
| Unknown | 8 | 3.8% |

### St. Mary Parish
**Total:** 289

| Race | Count | % |
|------|-------|---|
| Black | 153 | 52.9% |
| White | 135 | 46.7% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 903

| Race | Count | % |
|------|-------|---|
| White | 457 | 50.6% |
| Black | 404 | 44.7% |
| Unknown | 40 | 4.4% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 13

| Race | Count | % |
|------|-------|---|
| White | 10 | 76.9% |
| Black | 3 | 23.1% |

### Tangipahoa Parish
**Total:** 699

| Race | Count | % |
|------|-------|---|
| Black | 465 | 66.5% |
| White | 231 | 33.0% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 570

| Race | Count | % |
|------|-------|---|
| Black | 384 | 67.4% |
| White | 174 | 30.5% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 569

| Race | Count | % |
|------|-------|---|
| Black | 315 | 55.4% |
| White | 242 | 42.5% |
| American Indian/Alaska Native | 12 | 2.1% |

### Vermillion Parish
**Total:** 116

| Race | Count | % |
|------|-------|---|
| Black | 57 | 49.1% |
| White | 56 | 48.3% |
| Unknown | 2 | 1.7% |
| Asian/PacificIslander | 1 | 0.9% |

### Vernon Parish
**Total:** 183

| Race | Count | % |
|------|-------|---|
| White | 128 | 69.9% |
| Black | 53 | 29.0% |
| Asian/PacificIslander | 1 | 0.5% |
| Unknown | 1 | 0.5% |

### Ville Platte Police Department
**Total:** 31

| Race | Count | % |
|------|-------|---|
| Black | 18 | 58.1% |
| White | 12 | 38.7% |
| Unknown | 1 | 3.2% |

### Washington Parish
**Total:** 185

| Race | Count | % |
|------|-------|---|
| Black | 98 | 53.0% |
| White | 86 | 46.5% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 449

| Race | Count | % |
|------|-------|---|
| Black | 233 | 51.9% |
| White | 209 | 46.5% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 134

| Race | Count | % |
|------|-------|---|
| Black | 88 | 65.7% |
| White | 42 | 31.3% |
| Unknown | 3 | 2.2% |
| Asian/PacificIslander | 1 | 0.7% |

### West Carroll Parish
**Total:** 28

| Race | Count | % |
|------|-------|---|
| White | 22 | 78.6% |
| Black | 6 | 21.4% |

### West Felician Parish
**Total:** 204

| Race | Count | % |
|------|-------|---|
| Black | 131 | 64.2% |
| White | 73 | 35.8% |

### Winn Parish
**Total:** 146

| Race | Count | % |
|------|-------|---|
| White | 73 | 50.0% |
| Black | 73 | 50.0% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
