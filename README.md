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

_Last updated: 2026-05-09 02:35 UTC_

**Total inmates (latest scrape):** 25,743 across 72 parishes/jails

### Acadia Parish
**Total:** 177

| Race | Count | % |
|------|-------|---|
| White | 97 | 54.8% |
| Black | 78 | 44.1% |
| Asian/PacificIslander | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| White | 73 | 60.8% |
| Black | 44 | 36.7% |
| American Indian/Alaska Native | 2 | 1.7% |
| Unknown | 1 | 0.8% |

### Ascension Parish
**Total:** 497

| Race | Count | % |
|------|-------|---|
| Black | 265 | 53.3% |
| White | 199 | 40.0% |
| Unknown | 29 | 5.8% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 142

| Race | Count | % |
|------|-------|---|
| Unknown | 74 | 52.1% |
| White | 68 | 47.9% |

### Avoyelles Parish
**Total:** 378

| Race | Count | % |
|------|-------|---|
| Black | 198 | 52.4% |
| White | 175 | 46.3% |
| Unknown | 4 | 1.1% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 169

| Race | Count | % |
|------|-------|---|
| White | 119 | 70.4% |
| Black | 50 | 29.6% |

### Bienville Parish
**Total:** 38

| Race | Count | % |
|------|-------|---|
| White | 23 | 60.5% |
| Unknown | 15 | 39.5% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 49

| Race | Count | % |
|------|-------|---|
| Black | 31 | 63.3% |
| White | 18 | 36.7% |

### Bossier Parish
**Total:** 1,113

| Race | Count | % |
|------|-------|---|
| Black | 617 | 55.4% |
| White | 493 | 44.3% |
| Unknown | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,604

| Race | Count | % |
|------|-------|---|
| Black | 1,186 | 73.9% |
| White | 382 | 23.8% |
| Unknown | 33 | 2.1% |
| Asian/PacificIslander | 3 | 0.2% |

### Calcasieu Parish
**Total:** 1,024

| Race | Count | % |
|------|-------|---|
| Black | 563 | 55.0% |
| White | 420 | 41.0% |
| Unknown | 40 | 3.9% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 611

| Race | Count | % |
|------|-------|---|
| Black | 398 | 65.1% |
| White | 193 | 31.6% |
| American Indian/Alaska Native | 20 | 3.3% |

### Cameron Parish
**Total:** 18

| Race | Count | % |
|------|-------|---|
| White | 17 | 94.4% |
| Black | 1 | 5.6% |

### Catahoula Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| Black | 92 | 69.7% |
| White | 39 | 29.5% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 662

| Race | Count | % |
|------|-------|---|
| Black | 402 | 60.7% |
| White | 260 | 39.3% |

### Concordia Parish
**Total:** 814

| Race | Count | % |
|------|-------|---|
| White | 455 | 55.9% |
| Black | 355 | 43.6% |
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
**Total:** 265

| Race | Count | % |
|------|-------|---|
| Black | 163 | 61.5% |
| White | 101 | 38.1% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 92

| Race | Count | % |
|------|-------|---|
| White | 46 | 50.0% |
| Black | 44 | 47.8% |
| Unknown | 2 | 2.2% |

### Franklin Parish
**Total:** 837

| Race | Count | % |
|------|-------|---|
| Black | 543 | 64.9% |
| White | 283 | 33.8% |
| Unknown | 10 | 1.2% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 10

| Race | Count | % |
|------|-------|---|
| Black | 8 | 80.0% |
| White | 2 | 20.0% |

### Iberia Parish
**Total:** 445

| Race | Count | % |
|------|-------|---|
| Black | 275 | 61.8% |
| White | 162 | 36.4% |
| Asian/PacificIslander | 4 | 0.9% |
| Unknown | 3 | 0.7% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 110

| Race | Count | % |
|------|-------|---|
| Black | 67 | 60.9% |
| White | 41 | 37.3% |
| Unknown | 2 | 1.8% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 146

| Race | Count | % |
|------|-------|---|
| White | 72 | 49.3% |
| Black | 68 | 46.6% |
| American Indian/Alaska Native | 3 | 2.1% |
| Unknown | 2 | 1.4% |
| Asian/PacificIslander | 1 | 0.7% |

### Jefferson Parish
**Total:** 1,179

| Race | Count | % |
|------|-------|---|
| Black | 774 | 65.6% |
| White | 392 | 33.2% |
| Unknown | 9 | 0.8% |
| Asian/PacificIslander | 4 | 0.3% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 70

| Race | Count | % |
|------|-------|---|
| White | 49 | 70.0% |
| Black | 20 | 28.6% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 859

| Race | Count | % |
|------|-------|---|
| Black | 548 | 63.8% |
| White | 300 | 34.9% |
| Unknown | 11 | 1.3% |

### Lafourche Parish
**Total:** 738

| Race | Count | % |
|------|-------|---|
| Black | 380 | 51.5% |
| White | 351 | 47.6% |
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
**Total:** 368

| Race | Count | % |
|------|-------|---|
| Black | 277 | 75.3% |
| White | 89 | 24.2% |
| Unknown | 2 | 0.5% |

### Livingston Parish
**Total:** 785

| Race | Count | % |
|------|-------|---|
| White | 559 | 71.2% |
| Black | 217 | 27.6% |
| Unknown | 7 | 0.9% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 134

| Race | Count | % |
|------|-------|---|
| Black | 104 | 77.6% |
| White | 29 | 21.6% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 203

| Race | Count | % |
|------|-------|---|
| Black | 138 | 68.0% |
| White | 65 | 32.0% |

### Natchitoches Parish
**Total:** 196

| Race | Count | % |
|------|-------|---|
| Black | 146 | 74.5% |
| White | 46 | 23.5% |
| Unknown | 3 | 1.5% |
| Asian/PacificIslander | 1 | 0.5% |

### Oakdale Police Department
**Total:** 4

| Race | Count | % |
|------|-------|---|
| White | 3 | 75.0% |
| Black | 1 | 25.0% |

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
**Total:** 1,268

| Race | Count | % |
|------|-------|---|
| Black | 840 | 66.2% |
| White | 413 | 32.6% |
| Unknown | 15 | 1.2% |

### Plaquemines Parish
**Total:** 636

| Race | Count | % |
|------|-------|---|
| Black | 414 | 65.1% |
| White | 202 | 31.8% |
| Unknown | 12 | 1.9% |
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
**Total:** 990

| Race | Count | % |
|------|-------|---|
| Black | 612 | 61.8% |
| White | 358 | 36.2% |
| Unknown | 18 | 1.8% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 39

| Race | Count | % |
|------|-------|---|
| Black | 24 | 61.5% |
| White | 14 | 35.9% |
| Asian/PacificIslander | 1 | 2.6% |

### Richland Parish
**Total:** 714

| Race | Count | % |
|------|-------|---|
| Black | 487 | 68.2% |
| White | 217 | 30.4% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 181

| Race | Count | % |
|------|-------|---|
| White | 106 | 58.6% |
| Black | 75 | 41.4% |

### Shreveport Police Department
**Total:** 48

| Race | Count | % |
|------|-------|---|
| Black | 39 | 81.2% |
| White | 9 | 18.8% |

### St. Bernard Parish
**Total:** 222

| Race | Count | % |
|------|-------|---|
| Black | 128 | 57.7% |
| White | 91 | 41.0% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.5% |

### St. Charles Parish
**Total:** 168

| Race | Count | % |
|------|-------|---|
| Unknown | 101 | 60.1% |
| White | 67 | 39.9% |

### St. Helena Parish
**Total:** 78

| Race | Count | % |
|------|-------|---|
| Black | 56 | 71.8% |
| White | 17 | 21.8% |
| Unknown | 4 | 5.1% |
| American Indian/Alaska Native | 1 | 1.3% |

### St. James Parish
**Total:** 80

| Race | Count | % |
|------|-------|---|
| Black | 64 | 80.0% |
| White | 16 | 20.0% |

### St. John the Baptist Parish
**Total:** 203

| Race | Count | % |
|------|-------|---|
| Unknown | 129 | 63.5% |
| White | 74 | 36.5% |

### St. Landry Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| Black | 70 | 62.5% |
| White | 40 | 35.7% |
| Unknown | 2 | 1.8% |

### St. Martin Parish
**Total:** 188

| Race | Count | % |
|------|-------|---|
| White | 91 | 48.4% |
| Black | 89 | 47.3% |
| Unknown | 7 | 3.7% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 245

| Race | Count | % |
|------|-------|---|
| Black | 126 | 51.4% |
| White | 118 | 48.2% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 818

| Race | Count | % |
|------|-------|---|
| White | 415 | 50.7% |
| Black | 362 | 44.3% |
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
**Total:** 639

| Race | Count | % |
|------|-------|---|
| Black | 388 | 60.7% |
| White | 250 | 39.1% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 553

| Race | Count | % |
|------|-------|---|
| Black | 366 | 66.2% |
| White | 172 | 31.1% |
| Unknown | 15 | 2.7% |

### Terrebonne Parish
**Total:** 479

| Race | Count | % |
|------|-------|---|
| Black | 249 | 52.0% |
| White | 224 | 46.8% |
| American Indian/Alaska Native | 6 | 1.3% |

### Vermillion Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| White | 69 | 53.5% |
| Black | 58 | 45.0% |
| Unknown | 2 | 1.6% |

### Vernon Parish
**Total:** 152

| Race | Count | % |
|------|-------|---|
| White | 101 | 66.4% |
| Black | 48 | 31.6% |
| Unknown | 2 | 1.3% |
| Asian/PacificIslander | 1 | 0.7% |

### Ville Platte Police Department
**Total:** 31

| Race | Count | % |
|------|-------|---|
| Black | 18 | 58.1% |
| White | 12 | 38.7% |
| Unknown | 1 | 3.2% |

### Washington Parish
**Total:** 160

| Race | Count | % |
|------|-------|---|
| Black | 87 | 54.4% |
| White | 73 | 45.6% |

### Webster Parish
**Total:** 438

| Race | Count | % |
|------|-------|---|
| Black | 218 | 49.8% |
| White | 213 | 48.6% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 3 | 0.7% |

### West Baton Rouge Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| Black | 83 | 62.9% |
| White | 43 | 32.6% |
| Unknown | 5 | 3.8% |
| Asian/PacificIslander | 1 | 0.8% |

### West Carroll Parish
**Total:** 30

| Race | Count | % |
|------|-------|---|
| White | 26 | 86.7% |
| Black | 3 | 10.0% |
| Unknown | 1 | 3.3% |

### West Felician Parish
**Total:** 176

| Race | Count | % |
|------|-------|---|
| Black | 109 | 61.9% |
| White | 67 | 38.1% |

### Winn Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| White | 76 | 50.3% |
| Black | 75 | 49.7% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
