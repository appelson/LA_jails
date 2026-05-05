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

_Last updated: 2026-05-05 02:22 UTC_

**Total inmates (latest scrape):** 25,824 across 72 parishes/jails

### Acadia Parish
**Total:** 172

| Race | Count | % |
|------|-------|---|
| White | 92 | 53.5% |
| Black | 78 | 45.3% |
| Asian/PacificIslander | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 136

| Race | Count | % |
|------|-------|---|
| White | 87 | 64.0% |
| Black | 47 | 34.6% |
| Unknown | 1 | 0.7% |
| American Indian/Alaska Native | 1 | 0.7% |

### Ascension Parish
**Total:** 509

| Race | Count | % |
|------|-------|---|
| Black | 269 | 52.8% |
| White | 203 | 39.9% |
| Unknown | 33 | 6.5% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 147

| Race | Count | % |
|------|-------|---|
| Unknown | 76 | 51.7% |
| White | 71 | 48.3% |

### Avoyelles Parish
**Total:** 397

| Race | Count | % |
|------|-------|---|
| Black | 211 | 53.1% |
| White | 179 | 45.1% |
| Unknown | 6 | 1.5% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 185

| Race | Count | % |
|------|-------|---|
| White | 131 | 70.8% |
| Black | 54 | 29.2% |

### Bienville Parish
**Total:** 37

| Race | Count | % |
|------|-------|---|
| White | 22 | 59.5% |
| Unknown | 15 | 40.5% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 29 | 65.9% |
| White | 15 | 34.1% |

### Bossier Parish
**Total:** 1,121

| Race | Count | % |
|------|-------|---|
| Black | 617 | 55.0% |
| White | 501 | 44.7% |
| Unknown | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,599

| Race | Count | % |
|------|-------|---|
| Black | 1,182 | 73.9% |
| White | 380 | 23.8% |
| Unknown | 34 | 2.1% |
| Asian/PacificIslander | 3 | 0.2% |

### Calcasieu Parish
**Total:** 1,023

| Race | Count | % |
|------|-------|---|
| Black | 553 | 54.1% |
| White | 425 | 41.5% |
| Unknown | 43 | 4.2% |
| Asian/PacificIslander | 2 | 0.2% |

### Caldwell Parish
**Total:** 601

| Race | Count | % |
|------|-------|---|
| Black | 388 | 64.6% |
| White | 193 | 32.1% |
| American Indian/Alaska Native | 20 | 3.3% |

### Cameron Parish
**Total:** 20

| Race | Count | % |
|------|-------|---|
| White | 19 | 95.0% |
| Black | 1 | 5.0% |

### Catahoula Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 93 | 71.0% |
| White | 37 | 28.2% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 658

| Race | Count | % |
|------|-------|---|
| Black | 397 | 60.3% |
| White | 261 | 39.7% |

### Concordia Parish
**Total:** 831

| Race | Count | % |
|------|-------|---|
| White | 464 | 55.8% |
| Black | 363 | 43.7% |
| Unknown | 4 | 0.5% |

### DeSoto Parish
**Total:** 119

| Race | Count | % |
|------|-------|---|
| Black | 76 | 63.9% |
| White | 42 | 35.3% |
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
**Total:** 266

| Race | Count | % |
|------|-------|---|
| Black | 164 | 61.7% |
| White | 101 | 38.0% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 84

| Race | Count | % |
|------|-------|---|
| White | 45 | 53.6% |
| Black | 38 | 45.2% |
| Unknown | 1 | 1.2% |

### Franklin Parish
**Total:** 849

| Race | Count | % |
|------|-------|---|
| Black | 552 | 65.0% |
| White | 286 | 33.7% |
| Unknown | 10 | 1.2% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 8

| Race | Count | % |
|------|-------|---|
| Black | 5 | 62.5% |
| White | 3 | 37.5% |

### Iberia Parish
**Total:** 439

| Race | Count | % |
|------|-------|---|
| Black | 273 | 62.2% |
| White | 159 | 36.2% |
| Unknown | 3 | 0.7% |
| Asian/PacificIslander | 3 | 0.7% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 104

| Race | Count | % |
|------|-------|---|
| Black | 64 | 61.5% |
| White | 38 | 36.5% |
| Unknown | 2 | 1.9% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 149

| Race | Count | % |
|------|-------|---|
| White | 73 | 49.0% |
| Black | 71 | 47.7% |
| American Indian/Alaska Native | 3 | 2.0% |
| Asian/PacificIslander | 1 | 0.7% |
| Unknown | 1 | 0.7% |

### Jefferson Parish
**Total:** 1,174

| Race | Count | % |
|------|-------|---|
| Black | 770 | 65.6% |
| White | 391 | 33.3% |
| Unknown | 9 | 0.8% |
| Asian/PacificIslander | 4 | 0.3% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 75

| Race | Count | % |
|------|-------|---|
| White | 52 | 69.3% |
| Black | 22 | 29.3% |
| Unknown | 1 | 1.3% |

### Lafayette Parish
**Total:** 842

| Race | Count | % |
|------|-------|---|
| Black | 530 | 62.9% |
| White | 298 | 35.4% |
| Unknown | 14 | 1.7% |

### Lafourche Parish
**Total:** 747

| Race | Count | % |
|------|-------|---|
| Black | 383 | 51.3% |
| White | 357 | 47.8% |
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
**Total:** 374

| Race | Count | % |
|------|-------|---|
| Black | 275 | 73.5% |
| White | 95 | 25.4% |
| Unknown | 4 | 1.1% |

### Livingston Parish
**Total:** 804

| Race | Count | % |
|------|-------|---|
| White | 581 | 72.3% |
| Black | 214 | 26.6% |
| Unknown | 7 | 0.9% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 143

| Race | Count | % |
|------|-------|---|
| Black | 110 | 76.9% |
| White | 32 | 22.4% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 205

| Race | Count | % |
|------|-------|---|
| Black | 139 | 67.8% |
| White | 66 | 32.2% |

### Natchitoches Parish
**Total:** 193

| Race | Count | % |
|------|-------|---|
| Black | 147 | 76.2% |
| White | 42 | 21.8% |
| Unknown | 3 | 1.6% |
| Asian/PacificIslander | 1 | 0.5% |

### Oakdale Police Department
**Total:** 4

| Race | Count | % |
|------|-------|---|
| Black | 2 | 50.0% |
| White | 2 | 50.0% |

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
**Total:** 1,275

| Race | Count | % |
|------|-------|---|
| Black | 846 | 66.4% |
| White | 414 | 32.5% |
| Unknown | 15 | 1.2% |

### Plaquemines Parish
**Total:** 652

| Race | Count | % |
|------|-------|---|
| Black | 425 | 65.2% |
| White | 207 | 31.7% |
| Unknown | 12 | 1.8% |
| Asian/PacificIslander | 7 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Pointe Coupee Parish
**Total:** 103

| Race | Count | % |
|------|-------|---|
| Black | 68 | 66.0% |
| White | 34 | 33.0% |
| Unknown | 1 | 1.0% |

### Rapides Parish
**Total:** 982

| Race | Count | % |
|------|-------|---|
| Black | 617 | 62.8% |
| White | 347 | 35.3% |
| Unknown | 16 | 1.6% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 39

| Race | Count | % |
|------|-------|---|
| Black | 25 | 64.1% |
| White | 13 | 33.3% |
| Asian/PacificIslander | 1 | 2.6% |

### Richland Parish
**Total:** 719

| Race | Count | % |
|------|-------|---|
| Black | 495 | 68.8% |
| White | 214 | 29.8% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 181

| Race | Count | % |
|------|-------|---|
| White | 102 | 56.4% |
| Black | 79 | 43.6% |

### Shreveport Police Department
**Total:** 42

| Race | Count | % |
|------|-------|---|
| Black | 37 | 88.1% |
| White | 5 | 11.9% |

### St. Bernard Parish
**Total:** 222

| Race | Count | % |
|------|-------|---|
| Black | 129 | 58.1% |
| White | 90 | 40.5% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.5% |

### St. Charles Parish
**Total:** 169

| Race | Count | % |
|------|-------|---|
| Unknown | 96 | 56.8% |
| White | 73 | 43.2% |

### St. Helena Parish
**Total:** 77

| Race | Count | % |
|------|-------|---|
| Black | 56 | 72.7% |
| White | 16 | 20.8% |
| Unknown | 4 | 5.2% |
| American Indian/Alaska Native | 1 | 1.3% |

### St. James Parish
**Total:** 75

| Race | Count | % |
|------|-------|---|
| Black | 59 | 78.7% |
| White | 16 | 21.3% |

### St. John the Baptist Parish
**Total:** 197

| Race | Count | % |
|------|-------|---|
| Unknown | 123 | 62.4% |
| White | 74 | 37.6% |

### St. Landry Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| Black | 70 | 62.5% |
| White | 40 | 35.7% |
| Unknown | 2 | 1.8% |

### St. Martin Parish
**Total:** 192

| Race | Count | % |
|------|-------|---|
| Black | 97 | 50.5% |
| White | 88 | 45.8% |
| Unknown | 6 | 3.1% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 240

| Race | Count | % |
|------|-------|---|
| Black | 123 | 51.2% |
| White | 116 | 48.3% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 808

| Race | Count | % |
|------|-------|---|
| White | 408 | 50.5% |
| Black | 357 | 44.2% |
| Unknown | 38 | 4.7% |
| Asian/PacificIslander | 3 | 0.4% |
| American Indian/Alaska Native | 2 | 0.2% |

### Sulphur Police Department
**Total:** 14

| Race | Count | % |
|------|-------|---|
| White | 12 | 85.7% |
| Black | 2 | 14.3% |

### Tangipahoa Parish
**Total:** 630

| Race | Count | % |
|------|-------|---|
| Black | 385 | 61.1% |
| White | 244 | 38.7% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 557

| Race | Count | % |
|------|-------|---|
| Black | 366 | 65.7% |
| White | 175 | 31.4% |
| Unknown | 16 | 2.9% |

### Terrebonne Parish
**Total:** 471

| Race | Count | % |
|------|-------|---|
| Black | 247 | 52.4% |
| White | 217 | 46.1% |
| American Indian/Alaska Native | 7 | 1.5% |

### Vermillion Parish
**Total:** 125

| Race | Count | % |
|------|-------|---|
| White | 66 | 52.8% |
| Black | 57 | 45.6% |
| Unknown | 2 | 1.6% |

### Vernon Parish
**Total:** 161

| Race | Count | % |
|------|-------|---|
| White | 111 | 68.9% |
| Black | 47 | 29.2% |
| Unknown | 2 | 1.2% |
| Asian/PacificIslander | 1 | 0.6% |

### Ville Platte Police Department
**Total:** 31

| Race | Count | % |
|------|-------|---|
| Black | 18 | 58.1% |
| White | 12 | 38.7% |
| Unknown | 1 | 3.2% |

### Washington Parish
**Total:** 157

| Race | Count | % |
|------|-------|---|
| Black | 85 | 54.1% |
| White | 72 | 45.9% |

### Webster Parish
**Total:** 437

| Race | Count | % |
|------|-------|---|
| Black | 217 | 49.7% |
| White | 213 | 48.7% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 3 | 0.7% |

### West Baton Rouge Parish
**Total:** 144

| Race | Count | % |
|------|-------|---|
| Black | 89 | 61.8% |
| White | 50 | 34.7% |
| Unknown | 4 | 2.8% |
| Asian/PacificIslander | 1 | 0.7% |

### West Carroll Parish
**Total:** 30

| Race | Count | % |
|------|-------|---|
| White | 27 | 90.0% |
| Black | 3 | 10.0% |

### West Felician Parish
**Total:** 183

| Race | Count | % |
|------|-------|---|
| Black | 111 | 60.7% |
| White | 72 | 39.3% |

### Winn Parish
**Total:** 152

| Race | Count | % |
|------|-------|---|
| White | 77 | 50.7% |
| Black | 75 | 49.3% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
