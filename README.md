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

_Last updated: 2026-07-09 02:34 UTC_

**Total inmates (latest scrape):** 26,824 across 72 parishes/jails

### Acadia Parish
**Total:** 168

| Race | Count | % |
|------|-------|---|
| White | 96 | 57.1% |
| Black | 70 | 41.7% |
| Asian/PacificIslander | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 115

| Race | Count | % |
|------|-------|---|
| White | 71 | 61.7% |
| Black | 41 | 35.7% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 531

| Race | Count | % |
|------|-------|---|
| Black | 283 | 53.3% |
| White | 212 | 39.9% |
| Unknown | 32 | 6.0% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 157

| Race | Count | % |
|------|-------|---|
| Unknown | 87 | 55.4% |
| White | 70 | 44.6% |

### Avoyelles Parish
**Total:** 350

| Race | Count | % |
|------|-------|---|
| Black | 192 | 54.9% |
| White | 154 | 44.0% |
| Unknown | 3 | 0.9% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 158

| Race | Count | % |
|------|-------|---|
| White | 112 | 70.9% |
| Black | 46 | 29.1% |

### Bienville Parish
**Total:** 40

| Race | Count | % |
|------|-------|---|
| White | 21 | 52.5% |
| Unknown | 19 | 47.5% |

### Bogalusa Police Department
**Total:** 19

| Race | Count | % |
|------|-------|---|
| White | 13 | 68.4% |
| Black | 6 | 31.6% |

### Bossier City Police Department
**Total:** 45

| Race | Count | % |
|------|-------|---|
| Black | 29 | 64.4% |
| White | 16 | 35.6% |

### Bossier Parish
**Total:** 1,142

| Race | Count | % |
|------|-------|---|
| Black | 640 | 56.0% |
| White | 501 | 43.9% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,692

| Race | Count | % |
|------|-------|---|
| Black | 1,274 | 75.3% |
| White | 386 | 22.8% |
| Unknown | 31 | 1.8% |
| Asian/PacificIslander | 1 | 0.1% |

### Calcasieu Parish
**Total:** 1,105

| Race | Count | % |
|------|-------|---|
| Black | 610 | 55.2% |
| White | 452 | 40.9% |
| Unknown | 40 | 3.6% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 616

| Race | Count | % |
|------|-------|---|
| Black | 386 | 62.7% |
| White | 211 | 34.3% |
| American Indian/Alaska Native | 18 | 2.9% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 15 | 88.2% |
| Black | 2 | 11.8% |

### Catahoula Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 91 | 69.5% |
| White | 39 | 29.8% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 662

| Race | Count | % |
|------|-------|---|
| Black | 412 | 62.2% |
| White | 250 | 37.8% |

### Concordia Parish
**Total:** 807

| Race | Count | % |
|------|-------|---|
| White | 458 | 56.8% |
| Black | 349 | 43.2% |

### DeSoto Parish
**Total:** 118

| Race | Count | % |
|------|-------|---|
| Black | 69 | 58.5% |
| White | 48 | 40.7% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,361

| Race | Count | % |
|------|-------|---|
| Black | 1,074 | 78.9% |
| White | 218 | 16.0% |
| Unknown | 66 | 4.8% |
| Asian/PacificIslander | 2 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### East Feliciana Parish
**Total:** 269

| Race | Count | % |
|------|-------|---|
| Black | 173 | 64.3% |
| White | 95 | 35.3% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 168

| Race | Count | % |
|------|-------|---|
| Black | 94 | 56.0% |
| White | 73 | 43.5% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 843

| Race | Count | % |
|------|-------|---|
| Black | 554 | 65.7% |
| White | 279 | 33.1% |
| Unknown | 10 | 1.2% |

### Hammond Police Department
**Total:** 21

| Race | Count | % |
|------|-------|---|
| Black | 14 | 66.7% |
| White | 6 | 28.6% |
| Unknown | 1 | 4.8% |

### Iberia Parish
**Total:** 469

| Race | Count | % |
|------|-------|---|
| Black | 273 | 58.2% |
| White | 186 | 39.7% |
| Asian/PacificIslander | 5 | 1.1% |
| Unknown | 4 | 0.9% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 36

| Race | Count | % |
|------|-------|---|
| Black | 19 | 52.8% |
| White | 17 | 47.2% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 164

| Race | Count | % |
|------|-------|---|
| White | 90 | 54.9% |
| Black | 71 | 43.3% |
| American Indian/Alaska Native | 2 | 1.2% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,159

| Race | Count | % |
|------|-------|---|
| Black | 748 | 64.5% |
| White | 406 | 35.0% |
| Unknown | 5 | 0.4% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 73

| Race | Count | % |
|------|-------|---|
| White | 49 | 67.1% |
| Black | 23 | 31.5% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 809

| Race | Count | % |
|------|-------|---|
| Black | 534 | 66.0% |
| White | 259 | 32.0% |
| Unknown | 15 | 1.9% |
| Asian/PacificIslander | 1 | 0.1% |

### Lafourche Parish
**Total:** 754

| Race | Count | % |
|------|-------|---|
| Black | 392 | 52.0% |
| White | 358 | 47.5% |
| American Indian/Alaska Native | 3 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 371

| Race | Count | % |
|------|-------|---|
| Black | 273 | 73.6% |
| White | 95 | 25.6% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 819

| Race | Count | % |
|------|-------|---|
| White | 574 | 70.1% |
| Black | 233 | 28.4% |
| Unknown | 10 | 1.2% |
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
**Total:** 218

| Race | Count | % |
|------|-------|---|
| Black | 157 | 72.0% |
| White | 61 | 28.0% |

### Natchitoches Parish
**Total:** 181

| Race | Count | % |
|------|-------|---|
| Black | 134 | 74.0% |
| White | 43 | 23.8% |
| Unknown | 4 | 2.2% |

### Oakdale Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

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
**Total:** 1,351

| Race | Count | % |
|------|-------|---|
| Black | 898 | 66.5% |
| White | 437 | 32.3% |
| Unknown | 16 | 1.2% |

### Plaquemines Parish
**Total:** 684

| Race | Count | % |
|------|-------|---|
| Black | 442 | 64.6% |
| White | 219 | 32.0% |
| Unknown | 14 | 2.0% |
| Asian/PacificIslander | 7 | 1.0% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 116

| Race | Count | % |
|------|-------|---|
| Black | 70 | 60.3% |
| White | 42 | 36.2% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 2 | 1.7% |

### Rapides Parish
**Total:** 1,040

| Race | Count | % |
|------|-------|---|
| Black | 661 | 63.6% |
| White | 362 | 34.8% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 47

| Race | Count | % |
|------|-------|---|
| White | 23 | 48.9% |
| Black | 23 | 48.9% |
| Asian/PacificIslander | 1 | 2.1% |

### Richland Parish
**Total:** 683

| Race | Count | % |
|------|-------|---|
| Black | 472 | 69.1% |
| White | 202 | 29.6% |
| Unknown | 6 | 0.9% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 198

| Race | Count | % |
|------|-------|---|
| White | 112 | 56.6% |
| Black | 83 | 41.9% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 38

| Race | Count | % |
|------|-------|---|
| Black | 27 | 71.1% |
| White | 11 | 28.9% |

### St. Bernard Parish
**Total:** 221

| Race | Count | % |
|------|-------|---|
| Black | 132 | 59.7% |
| White | 85 | 38.5% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 201

| Race | Count | % |
|------|-------|---|
| Unknown | 121 | 60.2% |
| White | 80 | 39.8% |

### St. Helena Parish
**Total:** 51

| Race | Count | % |
|------|-------|---|
| Black | 36 | 70.6% |
| White | 14 | 27.5% |
| Unknown | 1 | 2.0% |

### St. James Parish
**Total:** 70

| Race | Count | % |
|------|-------|---|
| Black | 56 | 80.0% |
| White | 14 | 20.0% |

### St. John the Baptist Parish
**Total:** 204

| Race | Count | % |
|------|-------|---|
| Unknown | 132 | 64.7% |
| White | 72 | 35.3% |

### St. Landry Parish
**Total:** 127

| Race | Count | % |
|------|-------|---|
| Black | 85 | 66.9% |
| White | 40 | 31.5% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 222

| Race | Count | % |
|------|-------|---|
| Black | 114 | 51.4% |
| White | 98 | 44.1% |
| Unknown | 9 | 4.1% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 296

| Race | Count | % |
|------|-------|---|
| Black | 153 | 51.7% |
| White | 142 | 48.0% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 878

| Race | Count | % |
|------|-------|---|
| White | 461 | 52.5% |
| Black | 376 | 42.8% |
| Unknown | 39 | 4.4% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| White | 12 | 80.0% |
| Black | 3 | 20.0% |

### Tangipahoa Parish
**Total:** 667

| Race | Count | % |
|------|-------|---|
| Black | 437 | 65.5% |
| White | 228 | 34.2% |
| Unknown | 2 | 0.3% |

### Tensas Parish
**Total:** 563

| Race | Count | % |
|------|-------|---|
| Black | 376 | 66.8% |
| White | 175 | 31.1% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 558

| Race | Count | % |
|------|-------|---|
| Black | 304 | 54.5% |
| White | 242 | 43.4% |
| American Indian/Alaska Native | 11 | 2.0% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 64 | 49.2% |
| White | 63 | 48.5% |
| Unknown | 2 | 1.5% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 166

| Race | Count | % |
|------|-------|---|
| White | 115 | 69.3% |
| Black | 49 | 29.5% |
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
**Total:** 205

| Race | Count | % |
|------|-------|---|
| Black | 104 | 50.7% |
| White | 101 | 49.3% |

### Webster Parish
**Total:** 442

| Race | Count | % |
|------|-------|---|
| Black | 234 | 52.9% |
| White | 202 | 45.7% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.5% |

### West Baton Rouge Parish
**Total:** 127

| Race | Count | % |
|------|-------|---|
| Black | 87 | 68.5% |
| White | 36 | 28.3% |
| Unknown | 2 | 1.6% |
| Asian/PacificIslander | 2 | 1.6% |

### West Carroll Parish
**Total:** 30

| Race | Count | % |
|------|-------|---|
| White | 24 | 80.0% |
| Black | 6 | 20.0% |

### West Felician Parish
**Total:** 193

| Race | Count | % |
|------|-------|---|
| Black | 125 | 64.8% |
| White | 68 | 35.2% |

### Winn Parish
**Total:** 149

| Race | Count | % |
|------|-------|---|
| Black | 75 | 50.3% |
| White | 74 | 49.7% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
