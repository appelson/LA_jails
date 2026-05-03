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

_Last updated: 2026-05-03 02:34 UTC_

**Total inmates (latest scrape):** 25,729 across 72 parishes/jails

### Acadia Parish
**Total:** 173

| Race | Count | % |
|------|-------|---|
| White | 90 | 52.0% |
| Black | 81 | 46.8% |
| Asian/PacificIslander | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| White | 82 | 62.1% |
| Black | 48 | 36.4% |
| Unknown | 1 | 0.8% |
| American Indian/Alaska Native | 1 | 0.8% |

### Ascension Parish
**Total:** 509

| Race | Count | % |
|------|-------|---|
| Black | 271 | 53.2% |
| White | 201 | 39.5% |
| Unknown | 33 | 6.5% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 144

| Race | Count | % |
|------|-------|---|
| Unknown | 73 | 50.7% |
| White | 71 | 49.3% |

### Avoyelles Parish
**Total:** 396

| Race | Count | % |
|------|-------|---|
| Black | 211 | 53.3% |
| White | 178 | 44.9% |
| Unknown | 6 | 1.5% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 179

| Race | Count | % |
|------|-------|---|
| White | 125 | 69.8% |
| Black | 54 | 30.2% |

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
**Total:** 50

| Race | Count | % |
|------|-------|---|
| Black | 32 | 64.0% |
| White | 18 | 36.0% |

### Bossier Parish
**Total:** 1,132

| Race | Count | % |
|------|-------|---|
| Black | 619 | 54.7% |
| White | 510 | 45.1% |
| Unknown | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,587

| Race | Count | % |
|------|-------|---|
| Black | 1,172 | 73.9% |
| White | 378 | 23.8% |
| Unknown | 34 | 2.1% |
| Asian/PacificIslander | 3 | 0.2% |

### Calcasieu Parish
**Total:** 1,021

| Race | Count | % |
|------|-------|---|
| Black | 549 | 53.8% |
| White | 429 | 42.0% |
| Unknown | 41 | 4.0% |
| Asian/PacificIslander | 2 | 0.2% |

### Caldwell Parish
**Total:** 605

| Race | Count | % |
|------|-------|---|
| Black | 393 | 65.0% |
| White | 192 | 31.7% |
| American Indian/Alaska Native | 20 | 3.3% |

### Cameron Parish
**Total:** 24

| Race | Count | % |
|------|-------|---|
| White | 23 | 95.8% |
| Black | 1 | 4.2% |

### Catahoula Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| Black | 93 | 70.5% |
| White | 38 | 28.8% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 651

| Race | Count | % |
|------|-------|---|
| Black | 389 | 59.8% |
| White | 262 | 40.2% |

### Concordia Parish
**Total:** 825

| Race | Count | % |
|------|-------|---|
| White | 459 | 55.6% |
| Black | 362 | 43.9% |
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
**Total:** 267

| Race | Count | % |
|------|-------|---|
| Black | 164 | 61.4% |
| White | 102 | 38.2% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 82

| Race | Count | % |
|------|-------|---|
| White | 43 | 52.4% |
| Black | 38 | 46.3% |
| Unknown | 1 | 1.2% |

### Franklin Parish
**Total:** 843

| Race | Count | % |
|------|-------|---|
| Black | 549 | 65.1% |
| White | 283 | 33.6% |
| Unknown | 10 | 1.2% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 8

| Race | Count | % |
|------|-------|---|
| Black | 6 | 75.0% |
| White | 2 | 25.0% |

### Iberia Parish
**Total:** 445

| Race | Count | % |
|------|-------|---|
| Black | 274 | 61.6% |
| White | 164 | 36.9% |
| Unknown | 3 | 0.7% |
| Asian/PacificIslander | 3 | 0.7% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 103

| Race | Count | % |
|------|-------|---|
| Black | 66 | 64.1% |
| White | 35 | 34.0% |
| Unknown | 2 | 1.9% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 153

| Race | Count | % |
|------|-------|---|
| White | 76 | 49.7% |
| Black | 72 | 47.1% |
| American Indian/Alaska Native | 3 | 2.0% |
| Asian/PacificIslander | 1 | 0.7% |
| Unknown | 1 | 0.7% |

### Jefferson Parish
**Total:** 1,158

| Race | Count | % |
|------|-------|---|
| Black | 759 | 65.5% |
| White | 387 | 33.4% |
| Unknown | 8 | 0.7% |
| Asian/PacificIslander | 4 | 0.3% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Black | 1 | 100.0% |

### LaSalle Parish
**Total:** 77

| Race | Count | % |
|------|-------|---|
| White | 54 | 70.1% |
| Black | 22 | 28.6% |
| Unknown | 1 | 1.3% |

### Lafayette Parish
**Total:** 840

| Race | Count | % |
|------|-------|---|
| Black | 529 | 63.0% |
| White | 299 | 35.6% |
| Unknown | 12 | 1.4% |

### Lafourche Parish
**Total:** 734

| Race | Count | % |
|------|-------|---|
| Black | 376 | 51.2% |
| White | 351 | 47.8% |
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
| Black | 272 | 73.9% |
| White | 94 | 25.5% |
| Unknown | 2 | 0.5% |

### Livingston Parish
**Total:** 797

| Race | Count | % |
|------|-------|---|
| White | 576 | 72.3% |
| Black | 211 | 26.5% |
| Unknown | 8 | 1.0% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 141

| Race | Count | % |
|------|-------|---|
| Black | 109 | 77.3% |
| White | 31 | 22.0% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 207

| Race | Count | % |
|------|-------|---|
| Black | 142 | 68.6% |
| White | 65 | 31.4% |

### Natchitoches Parish
**Total:** 193

| Race | Count | % |
|------|-------|---|
| Black | 147 | 76.2% |
| White | 42 | 21.8% |
| Unknown | 3 | 1.6% |
| Asian/PacificIslander | 1 | 0.5% |

### Oakdale Police Department
**Total:** 6

| Race | Count | % |
|------|-------|---|
| Black | 3 | 50.0% |
| White | 3 | 50.0% |

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
**Total:** 1,260

| Race | Count | % |
|------|-------|---|
| Black | 837 | 66.4% |
| White | 409 | 32.5% |
| Unknown | 14 | 1.1% |

### Plaquemines Parish
**Total:** 637

| Race | Count | % |
|------|-------|---|
| Black | 419 | 65.8% |
| White | 198 | 31.1% |
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
**Total:** 977

| Race | Count | % |
|------|-------|---|
| Black | 610 | 62.4% |
| White | 349 | 35.7% |
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
**Total:** 717

| Race | Count | % |
|------|-------|---|
| Black | 495 | 69.0% |
| White | 212 | 29.6% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 181

| Race | Count | % |
|------|-------|---|
| White | 102 | 56.4% |
| Black | 79 | 43.6% |

### Shreveport Police Department
**Total:** 46

| Race | Count | % |
|------|-------|---|
| Black | 39 | 84.8% |
| White | 6 | 13.0% |
| Unknown | 1 | 2.2% |

### St. Bernard Parish
**Total:** 223

| Race | Count | % |
|------|-------|---|
| Black | 129 | 57.8% |
| White | 91 | 40.8% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.4% |

### St. Charles Parish
**Total:** 173

| Race | Count | % |
|------|-------|---|
| Unknown | 104 | 60.1% |
| White | 69 | 39.9% |

### St. Helena Parish
**Total:** 76

| Race | Count | % |
|------|-------|---|
| Black | 56 | 73.7% |
| White | 15 | 19.7% |
| Unknown | 4 | 5.3% |
| American Indian/Alaska Native | 1 | 1.3% |

### St. James Parish
**Total:** 73

| Race | Count | % |
|------|-------|---|
| Black | 60 | 82.2% |
| White | 13 | 17.8% |

### St. John the Baptist Parish
**Total:** 200

| Race | Count | % |
|------|-------|---|
| Unknown | 125 | 62.5% |
| White | 75 | 37.5% |

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
| Black | 96 | 49.7% |
| White | 90 | 46.6% |
| Unknown | 6 | 3.1% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 237

| Race | Count | % |
|------|-------|---|
| Black | 120 | 50.6% |
| White | 116 | 48.9% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 818

| Race | Count | % |
|------|-------|---|
| White | 412 | 50.4% |
| Black | 365 | 44.6% |
| Unknown | 36 | 4.4% |
| Asian/PacificIslander | 3 | 0.4% |
| American Indian/Alaska Native | 2 | 0.2% |

### Sulphur Police Department
**Total:** 13

| Race | Count | % |
|------|-------|---|
| White | 11 | 84.6% |
| Black | 2 | 15.4% |

### Tangipahoa Parish
**Total:** 624

| Race | Count | % |
|------|-------|---|
| Black | 378 | 60.6% |
| White | 245 | 39.3% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 565

| Race | Count | % |
|------|-------|---|
| Black | 373 | 66.0% |
| White | 176 | 31.2% |
| Unknown | 16 | 2.8% |

### Terrebonne Parish
**Total:** 468

| Race | Count | % |
|------|-------|---|
| Black | 244 | 52.1% |
| White | 217 | 46.4% |
| American Indian/Alaska Native | 7 | 1.5% |

### Vermillion Parish
**Total:** 125

| Race | Count | % |
|------|-------|---|
| White | 66 | 52.8% |
| Black | 56 | 44.8% |
| Unknown | 3 | 2.4% |

### Vernon Parish
**Total:** 158

| Race | Count | % |
|------|-------|---|
| White | 109 | 69.0% |
| Black | 46 | 29.1% |
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
**Total:** 149

| Race | Count | % |
|------|-------|---|
| Black | 79 | 53.0% |
| White | 70 | 47.0% |

### Webster Parish
**Total:** 439

| Race | Count | % |
|------|-------|---|
| Black | 216 | 49.2% |
| White | 216 | 49.2% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 3 | 0.7% |

### West Baton Rouge Parish
**Total:** 139

| Race | Count | % |
|------|-------|---|
| Black | 86 | 61.9% |
| White | 48 | 34.5% |
| Unknown | 4 | 2.9% |
| Asian/PacificIslander | 1 | 0.7% |

### West Carroll Parish
**Total:** 29

| Race | Count | % |
|------|-------|---|
| White | 26 | 89.7% |
| Black | 3 | 10.3% |

### West Felician Parish
**Total:** 183

| Race | Count | % |
|------|-------|---|
| Black | 111 | 60.7% |
| White | 72 | 39.3% |

### Winn Parish
**Total:** 146

| Race | Count | % |
|------|-------|---|
| White | 75 | 51.4% |
| Black | 71 | 48.6% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
