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

_Last updated: 2026-07-10 02:36 UTC_

**Total inmates (latest scrape):** 26,724 across 72 parishes/jails

### Acadia Parish
**Total:** 172

| Race | Count | % |
|------|-------|---|
| White | 101 | 58.7% |
| Black | 69 | 40.1% |
| Asian/PacificIslander | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 114

| Race | Count | % |
|------|-------|---|
| White | 71 | 62.3% |
| Black | 40 | 35.1% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 522

| Race | Count | % |
|------|-------|---|
| Black | 278 | 53.3% |
| White | 208 | 39.8% |
| Unknown | 32 | 6.1% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 159

| Race | Count | % |
|------|-------|---|
| Unknown | 89 | 56.0% |
| White | 70 | 44.0% |

### Avoyelles Parish
**Total:** 352

| Race | Count | % |
|------|-------|---|
| Black | 192 | 54.5% |
| White | 156 | 44.3% |
| Unknown | 3 | 0.9% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 157

| Race | Count | % |
|------|-------|---|
| White | 111 | 70.7% |
| Black | 46 | 29.3% |

### Bienville Parish
**Total:** 38

| Race | Count | % |
|------|-------|---|
| White | 20 | 52.6% |
| Unknown | 18 | 47.4% |

### Bogalusa Police Department
**Total:** 20

| Race | Count | % |
|------|-------|---|
| White | 14 | 70.0% |
| Black | 6 | 30.0% |

### Bossier City Police Department
**Total:** 43

| Race | Count | % |
|------|-------|---|
| Black | 26 | 60.5% |
| White | 17 | 39.5% |

### Bossier Parish
**Total:** 1,124

| Race | Count | % |
|------|-------|---|
| Black | 626 | 55.7% |
| White | 497 | 44.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,689

| Race | Count | % |
|------|-------|---|
| Black | 1,276 | 75.5% |
| White | 384 | 22.7% |
| Unknown | 28 | 1.7% |
| Asian/PacificIslander | 1 | 0.1% |

### Calcasieu Parish
**Total:** 1,105

| Race | Count | % |
|------|-------|---|
| Black | 610 | 55.2% |
| White | 453 | 41.0% |
| Unknown | 39 | 3.5% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 613

| Race | Count | % |
|------|-------|---|
| Black | 385 | 62.8% |
| White | 210 | 34.3% |
| American Indian/Alaska Native | 17 | 2.8% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 19

| Race | Count | % |
|------|-------|---|
| White | 17 | 89.5% |
| Black | 2 | 10.5% |

### Catahoula Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| Black | 92 | 69.7% |
| White | 39 | 29.5% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 659

| Race | Count | % |
|------|-------|---|
| Black | 408 | 61.9% |
| White | 251 | 38.1% |

### Concordia Parish
**Total:** 823

| Race | Count | % |
|------|-------|---|
| White | 466 | 56.6% |
| Black | 357 | 43.4% |

### DeSoto Parish
**Total:** 122

| Race | Count | % |
|------|-------|---|
| Black | 73 | 59.8% |
| White | 48 | 39.3% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,319

| Race | Count | % |
|------|-------|---|
| Black | 1,043 | 79.1% |
| White | 209 | 15.8% |
| Unknown | 64 | 4.9% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### East Feliciana Parish
**Total:** 272

| Race | Count | % |
|------|-------|---|
| Black | 177 | 65.1% |
| White | 94 | 34.6% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 166

| Race | Count | % |
|------|-------|---|
| Black | 96 | 57.8% |
| White | 69 | 41.6% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 842

| Race | Count | % |
|------|-------|---|
| Black | 554 | 65.8% |
| White | 278 | 33.0% |
| Unknown | 10 | 1.2% |

### Hammond Police Department
**Total:** 17

| Race | Count | % |
|------|-------|---|
| Black | 11 | 64.7% |
| White | 5 | 29.4% |
| Unknown | 1 | 5.9% |

### Iberia Parish
**Total:** 462

| Race | Count | % |
|------|-------|---|
| Black | 271 | 58.7% |
| White | 180 | 39.0% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
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
**Total:** 159

| Race | Count | % |
|------|-------|---|
| White | 86 | 54.1% |
| Black | 70 | 44.0% |
| American Indian/Alaska Native | 2 | 1.3% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,140

| Race | Count | % |
|------|-------|---|
| Black | 731 | 64.1% |
| White | 404 | 35.4% |
| Unknown | 5 | 0.4% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 72

| Race | Count | % |
|------|-------|---|
| White | 49 | 68.1% |
| Black | 22 | 30.6% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 803

| Race | Count | % |
|------|-------|---|
| Black | 534 | 66.5% |
| White | 253 | 31.5% |
| Unknown | 16 | 2.0% |

### Lafourche Parish
**Total:** 758

| Race | Count | % |
|------|-------|---|
| Black | 395 | 52.1% |
| White | 359 | 47.4% |
| American Indian/Alaska Native | 3 | 0.4% |
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
| Black | 269 | 73.7% |
| White | 93 | 25.5% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 825

| Race | Count | % |
|------|-------|---|
| White | 580 | 70.3% |
| Black | 233 | 28.2% |
| Unknown | 10 | 1.2% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 139

| Race | Count | % |
|------|-------|---|
| Black | 114 | 82.0% |
| White | 24 | 17.3% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 216

| Race | Count | % |
|------|-------|---|
| Black | 156 | 72.2% |
| White | 60 | 27.8% |

### Natchitoches Parish
**Total:** 186

| Race | Count | % |
|------|-------|---|
| Black | 139 | 74.7% |
| White | 43 | 23.1% |
| Unknown | 4 | 2.2% |

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
**Total:** 1,358

| Race | Count | % |
|------|-------|---|
| Black | 901 | 66.3% |
| White | 441 | 32.5% |
| Unknown | 16 | 1.2% |

### Plaquemines Parish
**Total:** 673

| Race | Count | % |
|------|-------|---|
| Black | 438 | 65.1% |
| White | 214 | 31.8% |
| Unknown | 13 | 1.9% |
| Asian/PacificIslander | 7 | 1.0% |
| American Indian/Alaska Native | 1 | 0.1% |

### Pointe Coupee Parish
**Total:** 114

| Race | Count | % |
|------|-------|---|
| Black | 69 | 60.5% |
| White | 42 | 36.8% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,040

| Race | Count | % |
|------|-------|---|
| Black | 657 | 63.2% |
| White | 366 | 35.2% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 45

| Race | Count | % |
|------|-------|---|
| Black | 22 | 48.9% |
| White | 22 | 48.9% |
| Asian/PacificIslander | 1 | 2.2% |

### Richland Parish
**Total:** 678

| Race | Count | % |
|------|-------|---|
| Black | 468 | 69.0% |
| White | 201 | 29.6% |
| Unknown | 6 | 0.9% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 199

| Race | Count | % |
|------|-------|---|
| White | 113 | 56.8% |
| Black | 83 | 41.7% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 32

| Race | Count | % |
|------|-------|---|
| Black | 26 | 81.2% |
| White | 6 | 18.8% |

### St. Bernard Parish
**Total:** 222

| Race | Count | % |
|------|-------|---|
| Black | 133 | 59.9% |
| White | 85 | 38.3% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 194

| Race | Count | % |
|------|-------|---|
| Unknown | 115 | 59.3% |
| White | 79 | 40.7% |

### St. Helena Parish
**Total:** 49

| Race | Count | % |
|------|-------|---|
| Black | 34 | 69.4% |
| White | 14 | 28.6% |
| Unknown | 1 | 2.0% |

### St. James Parish
**Total:** 71

| Race | Count | % |
|------|-------|---|
| Black | 57 | 80.3% |
| White | 14 | 19.7% |

### St. John the Baptist Parish
**Total:** 202

| Race | Count | % |
|------|-------|---|
| Unknown | 131 | 64.9% |
| White | 71 | 35.1% |

### St. Landry Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| Black | 85 | 65.9% |
| White | 42 | 32.6% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 217

| Race | Count | % |
|------|-------|---|
| Black | 110 | 50.7% |
| White | 98 | 45.2% |
| Unknown | 8 | 3.7% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 296

| Race | Count | % |
|------|-------|---|
| Black | 153 | 51.7% |
| White | 142 | 48.0% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 877

| Race | Count | % |
|------|-------|---|
| White | 462 | 52.7% |
| Black | 374 | 42.6% |
| Unknown | 39 | 4.4% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 16

| Race | Count | % |
|------|-------|---|
| White | 13 | 81.2% |
| Black | 3 | 18.8% |

### Tangipahoa Parish
**Total:** 680

| Race | Count | % |
|------|-------|---|
| Black | 447 | 65.7% |
| White | 231 | 34.0% |
| Unknown | 2 | 0.3% |

### Tensas Parish
**Total:** 562

| Race | Count | % |
|------|-------|---|
| Black | 376 | 66.9% |
| White | 174 | 31.0% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 557

| Race | Count | % |
|------|-------|---|
| Black | 304 | 54.6% |
| White | 242 | 43.4% |
| American Indian/Alaska Native | 10 | 1.8% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 136

| Race | Count | % |
|------|-------|---|
| Black | 67 | 49.3% |
| White | 66 | 48.5% |
| Unknown | 2 | 1.5% |
| Asian/PacificIslander | 1 | 0.7% |

### Vernon Parish
**Total:** 164

| Race | Count | % |
|------|-------|---|
| White | 113 | 68.9% |
| Black | 49 | 29.9% |
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
| Black | 104 | 52.5% |
| White | 94 | 47.5% |

### Webster Parish
**Total:** 450

| Race | Count | % |
|------|-------|---|
| Black | 244 | 54.2% |
| White | 200 | 44.4% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 124

| Race | Count | % |
|------|-------|---|
| Black | 82 | 66.1% |
| White | 37 | 29.8% |
| Unknown | 3 | 2.4% |
| Asian/PacificIslander | 2 | 1.6% |

### West Carroll Parish
**Total:** 31

| Race | Count | % |
|------|-------|---|
| White | 25 | 80.6% |
| Black | 6 | 19.4% |

### West Felician Parish
**Total:** 199

| Race | Count | % |
|------|-------|---|
| Black | 127 | 63.8% |
| White | 72 | 36.2% |

### Winn Parish
**Total:** 150

| Race | Count | % |
|------|-------|---|
| Black | 75 | 50.0% |
| White | 75 | 50.0% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
