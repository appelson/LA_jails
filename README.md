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

_Last updated: 2026-07-03 02:35 UTC_

**Total inmates (latest scrape):** 26,616 across 72 parishes/jails

### Acadia Parish
**Total:** 166

| Race | Count | % |
|------|-------|---|
| White | 94 | 56.6% |
| Black | 70 | 42.2% |
| Asian/PacificIslander | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 115

| Race | Count | % |
|------|-------|---|
| White | 72 | 62.6% |
| Black | 40 | 34.8% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 518

| Race | Count | % |
|------|-------|---|
| Black | 276 | 53.3% |
| White | 208 | 40.2% |
| Unknown | 30 | 5.8% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 154

| Race | Count | % |
|------|-------|---|
| Unknown | 87 | 56.5% |
| White | 67 | 43.5% |

### Avoyelles Parish
**Total:** 359

| Race | Count | % |
|------|-------|---|
| Black | 197 | 54.9% |
| White | 158 | 44.0% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 144

| Race | Count | % |
|------|-------|---|
| White | 102 | 70.8% |
| Black | 42 | 29.2% |

### Bienville Parish
**Total:** 40

| Race | Count | % |
|------|-------|---|
| White | 22 | 55.0% |
| Unknown | 18 | 45.0% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 48

| Race | Count | % |
|------|-------|---|
| Black | 30 | 62.5% |
| White | 18 | 37.5% |

### Bossier Parish
**Total:** 1,132

| Race | Count | % |
|------|-------|---|
| Black | 626 | 55.3% |
| White | 505 | 44.6% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,686

| Race | Count | % |
|------|-------|---|
| Black | 1,275 | 75.6% |
| White | 383 | 22.7% |
| Unknown | 27 | 1.6% |
| Asian/PacificIslander | 1 | 0.1% |

### Calcasieu Parish
**Total:** 1,100

| Race | Count | % |
|------|-------|---|
| Black | 613 | 55.7% |
| White | 443 | 40.3% |
| Unknown | 41 | 3.7% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 619

| Race | Count | % |
|------|-------|---|
| Black | 390 | 63.0% |
| White | 208 | 33.6% |
| American Indian/Alaska Native | 20 | 3.2% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 20

| Race | Count | % |
|------|-------|---|
| White | 18 | 90.0% |
| Black | 1 | 5.0% |
| Unknown | 1 | 5.0% |

### Catahoula Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 91 | 69.5% |
| White | 39 | 29.8% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 673

| Race | Count | % |
|------|-------|---|
| Black | 418 | 62.1% |
| White | 255 | 37.9% |

### Concordia Parish
**Total:** 797

| Race | Count | % |
|------|-------|---|
| White | 450 | 56.5% |
| Black | 346 | 43.4% |
| Unknown | 1 | 0.1% |

### DeSoto Parish
**Total:** 118

| Race | Count | % |
|------|-------|---|
| Black | 69 | 58.5% |
| White | 48 | 40.7% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,322

| Race | Count | % |
|------|-------|---|
| Black | 1,051 | 79.5% |
| White | 202 | 15.3% |
| Unknown | 68 | 5.1% |
| Asian/PacificIslander | 1 | 0.1% |

### East Feliciana Parish
**Total:** 271

| Race | Count | % |
|------|-------|---|
| Black | 174 | 64.2% |
| White | 96 | 35.4% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 167

| Race | Count | % |
|------|-------|---|
| Black | 93 | 55.7% |
| White | 73 | 43.7% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 843

| Race | Count | % |
|------|-------|---|
| Black | 553 | 65.6% |
| White | 280 | 33.2% |
| Unknown | 10 | 1.2% |

### Hammond Police Department
**Total:** 17

| Race | Count | % |
|------|-------|---|
| Black | 13 | 76.5% |
| White | 3 | 17.6% |
| Unknown | 1 | 5.9% |

### Iberia Parish
**Total:** 460

| Race | Count | % |
|------|-------|---|
| Black | 267 | 58.0% |
| White | 182 | 39.6% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 31

| Race | Count | % |
|------|-------|---|
| White | 17 | 54.8% |
| Black | 14 | 45.2% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 157

| Race | Count | % |
|------|-------|---|
| White | 83 | 52.9% |
| Black | 70 | 44.6% |
| American Indian/Alaska Native | 3 | 1.9% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,130

| Race | Count | % |
|------|-------|---|
| Black | 727 | 64.3% |
| White | 398 | 35.2% |
| Unknown | 5 | 0.4% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 75

| Race | Count | % |
|------|-------|---|
| White | 47 | 62.7% |
| Black | 27 | 36.0% |
| Unknown | 1 | 1.3% |

### Lafayette Parish
**Total:** 829

| Race | Count | % |
|------|-------|---|
| Black | 541 | 65.3% |
| White | 274 | 33.1% |
| Unknown | 13 | 1.6% |
| Asian/PacificIslander | 1 | 0.1% |

### Lafourche Parish
**Total:** 757

| Race | Count | % |
|------|-------|---|
| Black | 388 | 51.3% |
| White | 365 | 48.2% |
| American Indian/Alaska Native | 3 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 373

| Race | Count | % |
|------|-------|---|
| Black | 277 | 74.3% |
| White | 93 | 24.9% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 829

| Race | Count | % |
|------|-------|---|
| White | 583 | 70.3% |
| Black | 233 | 28.1% |
| Unknown | 11 | 1.3% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 142

| Race | Count | % |
|------|-------|---|
| Black | 115 | 81.0% |
| White | 26 | 18.3% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 214

| Race | Count | % |
|------|-------|---|
| Black | 151 | 70.6% |
| White | 63 | 29.4% |

### Natchitoches Parish
**Total:** 180

| Race | Count | % |
|------|-------|---|
| Black | 133 | 73.9% |
| White | 44 | 24.4% |
| Unknown | 3 | 1.7% |

### Oakdale Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| White | 2 | 100.0% |

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
**Total:** 1,273

| Race | Count | % |
|------|-------|---|
| Black | 848 | 66.6% |
| White | 411 | 32.3% |
| Unknown | 14 | 1.1% |

### Plaquemines Parish
**Total:** 687

| Race | Count | % |
|------|-------|---|
| Black | 444 | 64.6% |
| White | 217 | 31.6% |
| Unknown | 15 | 2.2% |
| Asian/PacificIslander | 7 | 1.0% |
| American Indian/Alaska Native | 4 | 0.6% |

### Pointe Coupee Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| Black | 69 | 61.6% |
| White | 40 | 35.7% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,025

| Race | Count | % |
|------|-------|---|
| Black | 660 | 64.4% |
| White | 349 | 34.0% |
| Unknown | 14 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 44

| Race | Count | % |
|------|-------|---|
| White | 22 | 50.0% |
| Black | 21 | 47.7% |
| Asian/PacificIslander | 1 | 2.3% |

### Richland Parish
**Total:** 697

| Race | Count | % |
|------|-------|---|
| Black | 480 | 68.9% |
| White | 206 | 29.6% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 4 | 0.6% |

### Sabine Parish
**Total:** 195

| Race | Count | % |
|------|-------|---|
| White | 108 | 55.4% |
| Black | 84 | 43.1% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 51

| Race | Count | % |
|------|-------|---|
| Black | 38 | 74.5% |
| White | 13 | 25.5% |

### St. Bernard Parish
**Total:** 217

| Race | Count | % |
|------|-------|---|
| Black | 130 | 59.9% |
| White | 84 | 38.7% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.5% |

### St. Charles Parish
**Total:** 193

| Race | Count | % |
|------|-------|---|
| Unknown | 116 | 60.1% |
| White | 77 | 39.9% |

### St. Helena Parish
**Total:** 52

| Race | Count | % |
|------|-------|---|
| Black | 36 | 69.2% |
| White | 15 | 28.8% |
| Unknown | 1 | 1.9% |

### St. James Parish
**Total:** 66

| Race | Count | % |
|------|-------|---|
| Black | 55 | 83.3% |
| White | 11 | 16.7% |

### St. John the Baptist Parish
**Total:** 203

| Race | Count | % |
|------|-------|---|
| Unknown | 134 | 66.0% |
| White | 69 | 34.0% |

### St. Landry Parish
**Total:** 128

| Race | Count | % |
|------|-------|---|
| Black | 83 | 64.8% |
| White | 43 | 33.6% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 213

| Race | Count | % |
|------|-------|---|
| Black | 110 | 51.6% |
| White | 93 | 43.7% |
| Unknown | 9 | 4.2% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 289

| Race | Count | % |
|------|-------|---|
| Black | 154 | 53.3% |
| White | 134 | 46.4% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 871

| Race | Count | % |
|------|-------|---|
| White | 460 | 52.8% |
| Black | 370 | 42.5% |
| Unknown | 38 | 4.4% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sulphur Police Department
**Total:** 16

| Race | Count | % |
|------|-------|---|
| White | 14 | 87.5% |
| Black | 2 | 12.5% |

### Tangipahoa Parish
**Total:** 662

| Race | Count | % |
|------|-------|---|
| Black | 430 | 65.0% |
| White | 231 | 34.9% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 572

| Race | Count | % |
|------|-------|---|
| Black | 380 | 66.4% |
| White | 180 | 31.5% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 541

| Race | Count | % |
|------|-------|---|
| Black | 295 | 54.5% |
| White | 233 | 43.1% |
| American Indian/Alaska Native | 10 | 1.8% |
| Unknown | 2 | 0.4% |
| Asian/PacificIslander | 1 | 0.2% |

### Vermillion Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| White | 66 | 50.0% |
| Black | 63 | 47.7% |
| Unknown | 2 | 1.5% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 168

| Race | Count | % |
|------|-------|---|
| White | 118 | 70.2% |
| Black | 48 | 28.6% |
| Asian/PacificIslander | 1 | 0.6% |
| Unknown | 1 | 0.6% |

### Ville Platte Police Department
**Total:** 31

| Race | Count | % |
|------|-------|---|
| Black | 18 | 58.1% |
| White | 12 | 38.7% |
| Unknown | 1 | 3.2% |

### Washington Parish
**Total:** 194

| Race | Count | % |
|------|-------|---|
| White | 98 | 50.5% |
| Black | 96 | 49.5% |

### Webster Parish
**Total:** 446

| Race | Count | % |
|------|-------|---|
| Black | 238 | 53.4% |
| White | 202 | 45.3% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 88 | 67.2% |
| White | 37 | 28.2% |
| Unknown | 4 | 3.1% |
| Asian/PacificIslander | 2 | 1.5% |

### West Carroll Parish
**Total:** 30

| Race | Count | % |
|------|-------|---|
| White | 23 | 76.7% |
| Black | 7 | 23.3% |

### West Felician Parish
**Total:** 198

| Race | Count | % |
|------|-------|---|
| Black | 129 | 65.2% |
| White | 69 | 34.8% |

### Winn Parish
**Total:** 149

| Race | Count | % |
|------|-------|---|
| Black | 78 | 52.3% |
| White | 71 | 47.7% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
