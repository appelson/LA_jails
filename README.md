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

_Last updated: 2026-08-07 02:31 UTC_

**Total inmates (latest scrape):** 27,002 across 72 parishes/jails

### Acadia Parish
**Total:** 162

| Race | Count | % |
|------|-------|---|
| White | 88 | 54.3% |
| Black | 72 | 44.4% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 121

| Race | Count | % |
|------|-------|---|
| White | 74 | 61.2% |
| Black | 43 | 35.5% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 2 | 1.7% |

### Ascension Parish
**Total:** 514

| Race | Count | % |
|------|-------|---|
| Black | 271 | 52.7% |
| White | 206 | 40.1% |
| Unknown | 32 | 6.2% |
| Asian/PacificIslander | 5 | 1.0% |

### Assumption Parish
**Total:** 162

| Race | Count | % |
|------|-------|---|
| Unknown | 92 | 56.8% |
| White | 70 | 43.2% |

### Avoyelles Parish
**Total:** 339

| Race | Count | % |
|------|-------|---|
| Black | 190 | 56.0% |
| White | 146 | 43.1% |
| Unknown | 3 | 0.9% |

### Beauregard Parish
**Total:** 170

| Race | Count | % |
|------|-------|---|
| White | 107 | 62.9% |
| Black | 63 | 37.1% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 19

| Race | Count | % |
|------|-------|---|
| White | 12 | 63.2% |
| Black | 7 | 36.8% |

### Bossier City Police Department
**Total:** 59

| Race | Count | % |
|------|-------|---|
| Black | 40 | 67.8% |
| White | 19 | 32.2% |

### Bossier Parish
**Total:** 1,126

| Race | Count | % |
|------|-------|---|
| Black | 630 | 56.0% |
| White | 494 | 43.9% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Caddo Parish
**Total:** 1,732

| Race | Count | % |
|------|-------|---|
| Black | 1,307 | 75.5% |
| White | 397 | 22.9% |
| Unknown | 28 | 1.6% |

### Calcasieu Parish
**Total:** 1,087

| Race | Count | % |
|------|-------|---|
| Black | 594 | 54.6% |
| White | 450 | 41.4% |
| Unknown | 42 | 3.9% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 604

| Race | Count | % |
|------|-------|---|
| Black | 388 | 64.2% |
| White | 200 | 33.1% |
| American Indian/Alaska Native | 15 | 2.5% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 23

| Race | Count | % |
|------|-------|---|
| White | 22 | 95.7% |
| Black | 1 | 4.3% |

### Catahoula Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 91 | 69.5% |
| White | 38 | 29.0% |
| Unknown | 2 | 1.5% |

### Claiborne Parish
**Total:** 649

| Race | Count | % |
|------|-------|---|
| Black | 399 | 61.5% |
| White | 250 | 38.5% |

### Concordia Parish
**Total:** 817

| Race | Count | % |
|------|-------|---|
| White | 463 | 56.7% |
| Black | 354 | 43.3% |

### DeSoto Parish
**Total:** 124

| Race | Count | % |
|------|-------|---|
| Black | 72 | 58.1% |
| White | 52 | 41.9% |

### East Baton Rouge Parish
**Total:** 1,311

| Race | Count | % |
|------|-------|---|
| Black | 1,023 | 78.0% |
| White | 230 | 17.5% |
| Unknown | 54 | 4.1% |
| Asian/PacificIslander | 3 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### East Feliciana Parish
**Total:** 270

| Race | Count | % |
|------|-------|---|
| Black | 174 | 64.4% |
| White | 94 | 34.8% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 159

| Race | Count | % |
|------|-------|---|
| Black | 96 | 60.4% |
| White | 62 | 39.0% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 846

| Race | Count | % |
|------|-------|---|
| Black | 560 | 66.2% |
| White | 281 | 33.2% |
| Unknown | 4 | 0.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 24

| Race | Count | % |
|------|-------|---|
| White | 11 | 45.8% |
| Black | 9 | 37.5% |
| Unknown | 4 | 16.7% |

### Iberia Parish
**Total:** 470

| Race | Count | % |
|------|-------|---|
| Black | 282 | 60.0% |
| White | 176 | 37.4% |
| Unknown | 6 | 1.3% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 57

| Race | Count | % |
|------|-------|---|
| Black | 35 | 61.4% |
| White | 22 | 38.6% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 163

| Race | Count | % |
|------|-------|---|
| White | 83 | 50.9% |
| Black | 78 | 47.9% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,197

| Race | Count | % |
|------|-------|---|
| Black | 784 | 65.5% |
| White | 406 | 33.9% |
| Unknown | 7 | 0.6% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 78

| Race | Count | % |
|------|-------|---|
| White | 49 | 62.8% |
| Black | 27 | 34.6% |
| Unknown | 2 | 2.6% |

### Lafayette Parish
**Total:** 837

| Race | Count | % |
|------|-------|---|
| Black | 554 | 66.2% |
| White | 272 | 32.5% |
| Unknown | 10 | 1.2% |
| Asian/PacificIslander | 1 | 0.1% |

### Lafourche Parish
**Total:** 779

| Race | Count | % |
|------|-------|---|
| Black | 396 | 50.8% |
| White | 379 | 48.7% |
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
| Black | 270 | 74.2% |
| White | 91 | 25.0% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 823

| Race | Count | % |
|------|-------|---|
| White | 584 | 71.0% |
| Black | 230 | 27.9% |
| Unknown | 6 | 0.7% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 147

| Race | Count | % |
|------|-------|---|
| Black | 120 | 81.6% |
| White | 26 | 17.7% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 202

| Race | Count | % |
|------|-------|---|
| Black | 149 | 73.8% |
| White | 52 | 25.7% |
| Unknown | 1 | 0.5% |

### Natchitoches Parish
**Total:** 185

| Race | Count | % |
|------|-------|---|
| Black | 142 | 76.8% |
| White | 39 | 21.1% |
| Unknown | 4 | 2.2% |

### Oakdale Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### Opelousas Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| African American | 1 | 100.0% |

### Orleans Parish
**Total:** 1,447

| Race | Count | % |
|------|-------|---|
| Black | 1,241 | 85.8% |
| White | 186 | 12.9% |
| Unknown | 15 | 1.0% |
| Asian/PacificIslander | 5 | 0.3% |

### Ouachita Parish
**Total:** 1,329

| Race | Count | % |
|------|-------|---|
| Black | 894 | 67.3% |
| White | 424 | 31.9% |
| Unknown | 11 | 0.8% |

### Plaquemines Parish
**Total:** 661

| Race | Count | % |
|------|-------|---|
| Black | 429 | 64.9% |
| White | 209 | 31.6% |
| Unknown | 12 | 1.8% |
| Asian/PacificIslander | 9 | 1.4% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 122

| Race | Count | % |
|------|-------|---|
| Black | 76 | 62.3% |
| White | 43 | 35.2% |
| Unknown | 2 | 1.6% |
| American Indian/Alaska Native | 1 | 0.8% |

### Rapides Parish
**Total:** 1,063

| Race | Count | % |
|------|-------|---|
| Black | 678 | 63.8% |
| White | 369 | 34.7% |
| Unknown | 14 | 1.3% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 41

| Race | Count | % |
|------|-------|---|
| Black | 22 | 53.7% |
| White | 18 | 43.9% |
| Asian/PacificIslander | 1 | 2.4% |

### Richland Parish
**Total:** 705

| Race | Count | % |
|------|-------|---|
| Black | 488 | 69.2% |
| White | 209 | 29.6% |
| Unknown | 5 | 0.7% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 190

| Race | Count | % |
|------|-------|---|
| White | 110 | 57.9% |
| Black | 78 | 41.1% |
| Unknown | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 35

| Race | Count | % |
|------|-------|---|
| Black | 25 | 71.4% |
| White | 10 | 28.6% |

### St. Bernard Parish
**Total:** 234

| Race | Count | % |
|------|-------|---|
| Black | 133 | 56.8% |
| White | 96 | 41.0% |
| Asian/PacificIslander | 3 | 1.3% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 179

| Race | Count | % |
|------|-------|---|
| Unknown | 99 | 55.3% |
| White | 80 | 44.7% |

### St. Helena Parish
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 30 | 68.2% |
| White | 14 | 31.8% |

### St. James Parish
**Total:** 79

| Race | Count | % |
|------|-------|---|
| Black | 68 | 86.1% |
| White | 11 | 13.9% |

### St. John the Baptist Parish
**Total:** 225

| Race | Count | % |
|------|-------|---|
| Unknown | 148 | 65.8% |
| White | 77 | 34.2% |

### St. Landry Parish
**Total:** 138

| Race | Count | % |
|------|-------|---|
| Black | 93 | 67.4% |
| White | 43 | 31.2% |
| Unknown | 2 | 1.4% |

### St. Martin Parish
**Total:** 214

| Race | Count | % |
|------|-------|---|
| Black | 108 | 50.5% |
| White | 98 | 45.8% |
| Unknown | 8 | 3.7% |

### St. Mary Parish
**Total:** 282

| Race | Count | % |
|------|-------|---|
| Black | 142 | 50.4% |
| White | 139 | 49.3% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 876

| Race | Count | % |
|------|-------|---|
| White | 446 | 50.9% |
| Black | 389 | 44.4% |
| Unknown | 39 | 4.5% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 14

| Race | Count | % |
|------|-------|---|
| White | 12 | 85.7% |
| Black | 2 | 14.3% |

### Tangipahoa Parish
**Total:** 704

| Race | Count | % |
|------|-------|---|
| Black | 463 | 65.8% |
| White | 238 | 33.8% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 566

| Race | Count | % |
|------|-------|---|
| Black | 382 | 67.5% |
| White | 172 | 30.4% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 585

| Race | Count | % |
|------|-------|---|
| Black | 328 | 56.1% |
| White | 243 | 41.5% |
| American Indian/Alaska Native | 12 | 2.1% |
| Unknown | 1 | 0.2% |
| Asian/PacificIslander | 1 | 0.2% |

### Vermillion Parish
**Total:** 116

| Race | Count | % |
|------|-------|---|
| White | 57 | 49.1% |
| Black | 56 | 48.3% |
| Unknown | 2 | 1.7% |
| Asian/PacificIslander | 1 | 0.9% |

### Vernon Parish
**Total:** 173

| Race | Count | % |
|------|-------|---|
| White | 121 | 69.9% |
| Black | 50 | 28.9% |
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
**Total:** 191

| Race | Count | % |
|------|-------|---|
| Black | 99 | 51.8% |
| White | 91 | 47.6% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 443

| Race | Count | % |
|------|-------|---|
| Black | 230 | 51.9% |
| White | 206 | 46.5% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 2 | 0.5% |

### West Baton Rouge Parish
**Total:** 134

| Race | Count | % |
|------|-------|---|
| Black | 88 | 65.7% |
| White | 42 | 31.3% |
| Unknown | 3 | 2.2% |
| Asian/PacificIslander | 1 | 0.7% |

### West Carroll Parish
**Total:** 29

| Race | Count | % |
|------|-------|---|
| White | 23 | 79.3% |
| Black | 6 | 20.7% |

### West Felician Parish
**Total:** 202

| Race | Count | % |
|------|-------|---|
| Black | 129 | 63.9% |
| White | 73 | 36.1% |

### Winn Parish
**Total:** 147

| Race | Count | % |
|------|-------|---|
| Black | 75 | 51.0% |
| White | 72 | 49.0% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
