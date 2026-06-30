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

_Last updated: 2026-06-30 02:56 UTC_

**Total inmates (latest scrape):** 26,732 across 72 parishes/jails

### Acadia Parish
**Total:** 185

| Race | Count | % |
|------|-------|---|
| White | 100 | 54.1% |
| Black | 83 | 44.9% |
| Asian/PacificIslander | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Allen Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| White | 70 | 62.5% |
| Black | 39 | 34.8% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 523

| Race | Count | % |
|------|-------|---|
| Black | 279 | 53.3% |
| White | 211 | 40.3% |
| Unknown | 29 | 5.5% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| Unknown | 83 | 55.0% |
| White | 68 | 45.0% |

### Avoyelles Parish
**Total:** 353

| Race | Count | % |
|------|-------|---|
| Black | 193 | 54.7% |
| White | 156 | 44.2% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 153

| Race | Count | % |
|------|-------|---|
| White | 107 | 69.9% |
| Black | 46 | 30.1% |

### Bienville Parish
**Total:** 44

| Race | Count | % |
|------|-------|---|
| White | 25 | 56.8% |
| Unknown | 19 | 43.2% |

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
| Black | 32 | 66.7% |
| White | 16 | 33.3% |

### Bossier Parish
**Total:** 1,121

| Race | Count | % |
|------|-------|---|
| Black | 623 | 55.6% |
| White | 497 | 44.3% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,700

| Race | Count | % |
|------|-------|---|
| Black | 1,278 | 75.2% |
| White | 391 | 23.0% |
| Unknown | 29 | 1.7% |
| Asian/PacificIslander | 2 | 0.1% |

### Calcasieu Parish
**Total:** 1,097

| Race | Count | % |
|------|-------|---|
| Black | 613 | 55.9% |
| White | 443 | 40.4% |
| Unknown | 38 | 3.5% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 623

| Race | Count | % |
|------|-------|---|
| Black | 392 | 62.9% |
| White | 210 | 33.7% |
| American Indian/Alaska Native | 20 | 3.2% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 19

| Race | Count | % |
|------|-------|---|
| White | 18 | 94.7% |
| Black | 1 | 5.3% |

### Catahoula Parish
**Total:** 135

| Race | Count | % |
|------|-------|---|
| Black | 94 | 69.6% |
| White | 40 | 29.6% |
| Unknown | 1 | 0.7% |

### Claiborne Parish
**Total:** 684

| Race | Count | % |
|------|-------|---|
| Black | 423 | 61.8% |
| White | 261 | 38.2% |

### Concordia Parish
**Total:** 801

| Race | Count | % |
|------|-------|---|
| White | 452 | 56.4% |
| Black | 348 | 43.4% |
| Unknown | 1 | 0.1% |

### DeSoto Parish
**Total:** 122

| Race | Count | % |
|------|-------|---|
| Black | 71 | 58.2% |
| White | 50 | 41.0% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,340

| Race | Count | % |
|------|-------|---|
| Black | 1,060 | 79.1% |
| White | 210 | 15.7% |
| Unknown | 68 | 5.1% |
| Asian/PacificIslander | 2 | 0.1% |

### East Feliciana Parish
**Total:** 274

| Race | Count | % |
|------|-------|---|
| Black | 176 | 64.2% |
| White | 97 | 35.4% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 165

| Race | Count | % |
|------|-------|---|
| Black | 95 | 57.6% |
| White | 69 | 41.8% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 839

| Race | Count | % |
|------|-------|---|
| Black | 552 | 65.8% |
| White | 277 | 33.0% |
| Unknown | 10 | 1.2% |

### Hammond Police Department
**Total:** 13

| Race | Count | % |
|------|-------|---|
| Black | 9 | 69.2% |
| White | 3 | 23.1% |
| Unknown | 1 | 7.7% |

### Iberia Parish
**Total:** 456

| Race | Count | % |
|------|-------|---|
| Black | 269 | 59.0% |
| White | 176 | 38.6% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 36

| Race | Count | % |
|------|-------|---|
| Black | 21 | 58.3% |
| White | 15 | 41.7% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 160

| Race | Count | % |
|------|-------|---|
| White | 85 | 53.1% |
| Black | 71 | 44.4% |
| American Indian/Alaska Native | 3 | 1.9% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,129

| Race | Count | % |
|------|-------|---|
| Black | 726 | 64.3% |
| White | 397 | 35.2% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 71

| Race | Count | % |
|------|-------|---|
| White | 47 | 66.2% |
| Black | 23 | 32.4% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 845

| Race | Count | % |
|------|-------|---|
| Black | 540 | 63.9% |
| White | 289 | 34.2% |
| Unknown | 15 | 1.8% |
| Asian/PacificIslander | 1 | 0.1% |

### Lafourche Parish
**Total:** 753

| Race | Count | % |
|------|-------|---|
| Black | 387 | 51.4% |
| White | 362 | 48.1% |
| American Indian/Alaska Native | 3 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 372

| Race | Count | % |
|------|-------|---|
| Black | 277 | 74.5% |
| White | 92 | 24.7% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 829

| Race | Count | % |
|------|-------|---|
| White | 595 | 71.8% |
| Black | 222 | 26.8% |
| Unknown | 10 | 1.2% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 141

| Race | Count | % |
|------|-------|---|
| Black | 112 | 79.4% |
| White | 28 | 19.9% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 213

| Race | Count | % |
|------|-------|---|
| Black | 150 | 70.4% |
| White | 63 | 29.6% |

### Natchitoches Parish
**Total:** 186

| Race | Count | % |
|------|-------|---|
| Black | 137 | 73.7% |
| White | 46 | 24.7% |
| Unknown | 3 | 1.6% |

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
**Total:** 1,294

| Race | Count | % |
|------|-------|---|
| Black | 865 | 66.8% |
| White | 416 | 32.1% |
| Unknown | 13 | 1.0% |

### Plaquemines Parish
**Total:** 672

| Race | Count | % |
|------|-------|---|
| Black | 435 | 64.7% |
| White | 211 | 31.4% |
| Unknown | 16 | 2.4% |
| Asian/PacificIslander | 7 | 1.0% |
| American Indian/Alaska Native | 3 | 0.4% |

### Pointe Coupee Parish
**Total:** 110

| Race | Count | % |
|------|-------|---|
| Black | 67 | 60.9% |
| White | 40 | 36.4% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,042

| Race | Count | % |
|------|-------|---|
| Black | 661 | 63.4% |
| White | 364 | 34.9% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 46

| Race | Count | % |
|------|-------|---|
| Black | 25 | 54.3% |
| White | 20 | 43.5% |
| Asian/PacificIslander | 1 | 2.2% |

### Richland Parish
**Total:** 714

| Race | Count | % |
|------|-------|---|
| Black | 495 | 69.3% |
| White | 209 | 29.3% |
| Unknown | 6 | 0.8% |
| Asian/PacificIslander | 4 | 0.6% |

### Sabine Parish
**Total:** 190

| Race | Count | % |
|------|-------|---|
| White | 105 | 55.3% |
| Black | 82 | 43.2% |
| Unknown | 2 | 1.1% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 80

| Race | Count | % |
|------|-------|---|
| Black | 62 | 77.5% |
| White | 18 | 22.5% |

### St. Bernard Parish
**Total:** 220

| Race | Count | % |
|------|-------|---|
| Black | 129 | 58.6% |
| White | 88 | 40.0% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.5% |

### St. Charles Parish
**Total:** 196

| Race | Count | % |
|------|-------|---|
| Unknown | 118 | 60.2% |
| White | 78 | 39.8% |

### St. Helena Parish
**Total:** 51

| Race | Count | % |
|------|-------|---|
| Black | 36 | 70.6% |
| White | 14 | 27.5% |
| Unknown | 1 | 2.0% |

### St. James Parish
**Total:** 66

| Race | Count | % |
|------|-------|---|
| Black | 56 | 84.8% |
| White | 10 | 15.2% |

### St. John the Baptist Parish
**Total:** 200

| Race | Count | % |
|------|-------|---|
| Unknown | 132 | 66.0% |
| White | 68 | 34.0% |

### St. Landry Parish
**Total:** 126

| Race | Count | % |
|------|-------|---|
| Black | 80 | 63.5% |
| White | 43 | 34.1% |
| Unknown | 3 | 2.4% |

### St. Martin Parish
**Total:** 219

| Race | Count | % |
|------|-------|---|
| Black | 112 | 51.1% |
| White | 97 | 44.3% |
| Unknown | 9 | 4.1% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 294

| Race | Count | % |
|------|-------|---|
| Black | 152 | 51.7% |
| White | 141 | 48.0% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 876

| Race | Count | % |
|------|-------|---|
| White | 462 | 52.7% |
| Black | 373 | 42.6% |
| Unknown | 38 | 4.3% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sulphur Police Department
**Total:** 16

| Race | Count | % |
|------|-------|---|
| White | 14 | 87.5% |
| Black | 2 | 12.5% |

### Tangipahoa Parish
**Total:** 667

| Race | Count | % |
|------|-------|---|
| Black | 425 | 63.7% |
| White | 241 | 36.1% |
| Unknown | 1 | 0.1% |

### Tensas Parish
**Total:** 567

| Race | Count | % |
|------|-------|---|
| Black | 378 | 66.7% |
| White | 177 | 31.2% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 506

| Race | Count | % |
|------|-------|---|
| Black | 271 | 53.6% |
| White | 225 | 44.5% |
| American Indian/Alaska Native | 9 | 1.8% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 134

| Race | Count | % |
|------|-------|---|
| White | 69 | 51.5% |
| Black | 62 | 46.3% |
| Unknown | 2 | 1.5% |
| Asian/PacificIslander | 1 | 0.7% |

### Vernon Parish
**Total:** 171

| Race | Count | % |
|------|-------|---|
| White | 119 | 69.6% |
| Black | 49 | 28.7% |
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
**Total:** 193

| Race | Count | % |
|------|-------|---|
| White | 100 | 51.8% |
| Black | 93 | 48.2% |

### Webster Parish
**Total:** 446

| Race | Count | % |
|------|-------|---|
| Black | 237 | 53.1% |
| White | 203 | 45.5% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 126

| Race | Count | % |
|------|-------|---|
| Black | 86 | 68.3% |
| White | 34 | 27.0% |
| Unknown | 4 | 3.2% |
| Asian/PacificIslander | 2 | 1.6% |

### West Carroll Parish
**Total:** 33

| Race | Count | % |
|------|-------|---|
| White | 26 | 78.8% |
| Black | 7 | 21.2% |

### West Felician Parish
**Total:** 195

| Race | Count | % |
|------|-------|---|
| Black | 126 | 64.6% |
| White | 69 | 35.4% |

### Winn Parish
**Total:** 145

| Race | Count | % |
|------|-------|---|
| Black | 76 | 52.4% |
| White | 69 | 47.6% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
