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

_Last updated: 2026-07-06 02:46 UTC_

**Total inmates (latest scrape):** 26,888 across 72 parishes/jails

### Acadia Parish
**Total:** 167

| Race | Count | % |
|------|-------|---|
| White | 97 | 58.1% |
| Black | 68 | 40.7% |
| Asian/PacificIslander | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 117

| Race | Count | % |
|------|-------|---|
| White | 73 | 62.4% |
| Black | 41 | 35.0% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 528

| Race | Count | % |
|------|-------|---|
| Black | 281 | 53.2% |
| White | 212 | 40.2% |
| Unknown | 31 | 5.9% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 159

| Race | Count | % |
|------|-------|---|
| Unknown | 90 | 56.6% |
| White | 69 | 43.4% |

### Avoyelles Parish
**Total:** 363

| Race | Count | % |
|------|-------|---|
| Black | 199 | 54.8% |
| White | 160 | 44.1% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 149

| Race | Count | % |
|------|-------|---|
| White | 106 | 71.1% |
| Black | 43 | 28.9% |

### Bienville Parish
**Total:** 41

| Race | Count | % |
|------|-------|---|
| White | 22 | 53.7% |
| Unknown | 19 | 46.3% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 43

| Race | Count | % |
|------|-------|---|
| Black | 26 | 60.5% |
| White | 17 | 39.5% |

### Bossier Parish
**Total:** 1,135

| Race | Count | % |
|------|-------|---|
| Black | 636 | 56.0% |
| White | 497 | 43.8% |
| American Indian/Alaska Native | 1 | 0.1% |
| Unknown | 1 | 0.1% |

### Caddo Parish
**Total:** 1,700

| Race | Count | % |
|------|-------|---|
| Black | 1,280 | 75.3% |
| White | 392 | 23.1% |
| Unknown | 27 | 1.6% |
| Asian/PacificIslander | 1 | 0.1% |

### Calcasieu Parish
**Total:** 1,114

| Race | Count | % |
|------|-------|---|
| Black | 616 | 55.3% |
| White | 454 | 40.8% |
| Unknown | 41 | 3.7% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 621

| Race | Count | % |
|------|-------|---|
| Black | 391 | 63.0% |
| White | 209 | 33.7% |
| American Indian/Alaska Native | 20 | 3.2% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 16 | 94.1% |
| Black | 1 | 5.9% |

### Catahoula Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 91 | 69.5% |
| White | 39 | 29.8% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 672

| Race | Count | % |
|------|-------|---|
| Black | 417 | 62.1% |
| White | 255 | 37.9% |

### Concordia Parish
**Total:** 803

| Race | Count | % |
|------|-------|---|
| White | 448 | 55.8% |
| Black | 354 | 44.1% |
| Unknown | 1 | 0.1% |

### DeSoto Parish
**Total:** 122

| Race | Count | % |
|------|-------|---|
| Black | 71 | 58.2% |
| White | 50 | 41.0% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,330

| Race | Count | % |
|------|-------|---|
| Black | 1,054 | 79.2% |
| White | 209 | 15.7% |
| Unknown | 66 | 5.0% |
| Asian/PacificIslander | 1 | 0.1% |

### East Feliciana Parish
**Total:** 271

| Race | Count | % |
|------|-------|---|
| Black | 174 | 64.2% |
| White | 96 | 35.4% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 171

| Race | Count | % |
|------|-------|---|
| Black | 93 | 54.4% |
| White | 77 | 45.0% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 846

| Race | Count | % |
|------|-------|---|
| Black | 556 | 65.7% |
| White | 280 | 33.1% |
| Unknown | 10 | 1.2% |

### Hammond Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| Black | 11 | 73.3% |
| White | 3 | 20.0% |
| Unknown | 1 | 6.7% |

### Iberia Parish
**Total:** 471

| Race | Count | % |
|------|-------|---|
| Black | 272 | 57.7% |
| White | 188 | 39.9% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 33

| Race | Count | % |
|------|-------|---|
| White | 18 | 54.5% |
| Black | 15 | 45.5% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 164

| Race | Count | % |
|------|-------|---|
| White | 89 | 54.3% |
| Black | 71 | 43.3% |
| American Indian/Alaska Native | 3 | 1.8% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,146

| Race | Count | % |
|------|-------|---|
| Black | 734 | 64.0% |
| White | 406 | 35.4% |
| Unknown | 5 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 81

| Race | Count | % |
|------|-------|---|
| White | 53 | 65.4% |
| Black | 27 | 33.3% |
| Unknown | 1 | 1.2% |

### Lafayette Parish
**Total:** 845

| Race | Count | % |
|------|-------|---|
| Black | 553 | 65.4% |
| White | 276 | 32.7% |
| Unknown | 15 | 1.8% |
| Asian/PacificIslander | 1 | 0.1% |

### Lafourche Parish
**Total:** 759

| Race | Count | % |
|------|-------|---|
| Black | 390 | 51.4% |
| White | 365 | 48.1% |
| American Indian/Alaska Native | 3 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 375

| Race | Count | % |
|------|-------|---|
| Black | 280 | 74.7% |
| White | 92 | 24.5% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 834

| Race | Count | % |
|------|-------|---|
| White | 588 | 70.5% |
| Black | 233 | 27.9% |
| Unknown | 11 | 1.3% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 143

| Race | Count | % |
|------|-------|---|
| Black | 116 | 81.1% |
| White | 26 | 18.2% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 220

| Race | Count | % |
|------|-------|---|
| Black | 155 | 70.5% |
| White | 65 | 29.5% |

### Natchitoches Parish
**Total:** 187

| Race | Count | % |
|------|-------|---|
| Black | 139 | 74.3% |
| White | 45 | 24.1% |
| Unknown | 3 | 1.6% |

### Oakdale Police Department
**Total:** 5

| Race | Count | % |
|------|-------|---|
| White | 3 | 60.0% |
| Black | 2 | 40.0% |

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
**Total:** 1,317

| Race | Count | % |
|------|-------|---|
| Black | 874 | 66.4% |
| White | 428 | 32.5% |
| Unknown | 15 | 1.1% |

### Plaquemines Parish
**Total:** 686

| Race | Count | % |
|------|-------|---|
| Black | 442 | 64.4% |
| White | 218 | 31.8% |
| Unknown | 15 | 2.2% |
| Asian/PacificIslander | 7 | 1.0% |
| American Indian/Alaska Native | 4 | 0.6% |

### Pointe Coupee Parish
**Total:** 115

| Race | Count | % |
|------|-------|---|
| Black | 72 | 62.6% |
| White | 40 | 34.8% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,030

| Race | Count | % |
|------|-------|---|
| Black | 660 | 64.1% |
| White | 354 | 34.4% |
| Unknown | 14 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| Black | 21 | 48.8% |
| White | 21 | 48.8% |
| Asian/PacificIslander | 1 | 2.3% |

### Richland Parish
**Total:** 694

| Race | Count | % |
|------|-------|---|
| Black | 478 | 68.9% |
| White | 206 | 29.7% |
| Unknown | 6 | 0.9% |
| Asian/PacificIslander | 4 | 0.6% |

### Sabine Parish
**Total:** 201

| Race | Count | % |
|------|-------|---|
| White | 111 | 55.2% |
| Black | 85 | 42.3% |
| Unknown | 4 | 2.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 53

| Race | Count | % |
|------|-------|---|
| Black | 40 | 75.5% |
| White | 12 | 22.6% |
| Unknown | 1 | 1.9% |

### St. Bernard Parish
**Total:** 221

| Race | Count | % |
|------|-------|---|
| Black | 131 | 59.3% |
| White | 86 | 38.9% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 192

| Race | Count | % |
|------|-------|---|
| Unknown | 117 | 60.9% |
| White | 75 | 39.1% |

### St. Helena Parish
**Total:** 52

| Race | Count | % |
|------|-------|---|
| Black | 36 | 69.2% |
| White | 15 | 28.8% |
| Unknown | 1 | 1.9% |

### St. James Parish
**Total:** 70

| Race | Count | % |
|------|-------|---|
| Black | 57 | 81.4% |
| White | 13 | 18.6% |

### St. John the Baptist Parish
**Total:** 207

| Race | Count | % |
|------|-------|---|
| Unknown | 134 | 64.7% |
| White | 73 | 35.3% |

### St. Landry Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 85 | 65.4% |
| White | 42 | 32.3% |
| Unknown | 3 | 2.3% |

### St. Martin Parish
**Total:** 215

| Race | Count | % |
|------|-------|---|
| Black | 111 | 51.6% |
| White | 94 | 43.7% |
| Unknown | 9 | 4.2% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 296

| Race | Count | % |
|------|-------|---|
| Black | 154 | 52.0% |
| White | 141 | 47.6% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 873

| Race | Count | % |
|------|-------|---|
| White | 460 | 52.7% |
| Black | 372 | 42.6% |
| Unknown | 38 | 4.4% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sulphur Police Department
**Total:** 19

| Race | Count | % |
|------|-------|---|
| White | 17 | 89.5% |
| Black | 2 | 10.5% |

### Tangipahoa Parish
**Total:** 673

| Race | Count | % |
|------|-------|---|
| Black | 439 | 65.2% |
| White | 233 | 34.6% |
| Unknown | 1 | 0.1% |

### Tensas Parish
**Total:** 572

| Race | Count | % |
|------|-------|---|
| Black | 380 | 66.4% |
| White | 180 | 31.5% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 543

| Race | Count | % |
|------|-------|---|
| Black | 298 | 54.9% |
| White | 233 | 42.9% |
| American Indian/Alaska Native | 10 | 1.8% |
| Unknown | 2 | 0.4% |

### Vermillion Parish
**Total:** 136

| Race | Count | % |
|------|-------|---|
| White | 67 | 49.3% |
| Black | 66 | 48.5% |
| Unknown | 2 | 1.5% |
| Asian/PacificIslander | 1 | 0.7% |

### Vernon Parish
**Total:** 174

| Race | Count | % |
|------|-------|---|
| White | 121 | 69.5% |
| Black | 51 | 29.3% |
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
**Total:** 198

| Race | Count | % |
|------|-------|---|
| White | 100 | 50.5% |
| Black | 98 | 49.5% |

### Webster Parish
**Total:** 448

| Race | Count | % |
|------|-------|---|
| Black | 240 | 53.6% |
| White | 202 | 45.1% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 89 | 68.5% |
| White | 35 | 26.9% |
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
**Total:** 152

| Race | Count | % |
|------|-------|---|
| Black | 79 | 52.0% |
| White | 73 | 48.0% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
