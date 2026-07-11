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

_Last updated: 2026-07-11 02:13 UTC_

**Total inmates (latest scrape):** 26,734 across 72 parishes/jails

### Acadia Parish
**Total:** 175

| Race | Count | % |
|------|-------|---|
| White | 104 | 59.4% |
| Black | 69 | 39.4% |
| Asian/PacificIslander | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 115

| Race | Count | % |
|------|-------|---|
| White | 73 | 63.5% |
| Black | 39 | 33.9% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 521

| Race | Count | % |
|------|-------|---|
| Black | 274 | 52.6% |
| White | 211 | 40.5% |
| Unknown | 32 | 6.1% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 158

| Race | Count | % |
|------|-------|---|
| Unknown | 89 | 56.3% |
| White | 69 | 43.7% |

### Avoyelles Parish
**Total:** 352

| Race | Count | % |
|------|-------|---|
| Black | 194 | 55.1% |
| White | 154 | 43.8% |
| Unknown | 3 | 0.9% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 159

| Race | Count | % |
|------|-------|---|
| White | 112 | 70.4% |
| Black | 47 | 29.6% |

### Bienville Parish
**Total:** 36

| Race | Count | % |
|------|-------|---|
| White | 20 | 55.6% |
| Unknown | 16 | 44.4% |

### Bogalusa Police Department
**Total:** 22

| Race | Count | % |
|------|-------|---|
| White | 14 | 63.6% |
| Black | 8 | 36.4% |

### Bossier City Police Department
**Total:** 51

| Race | Count | % |
|------|-------|---|
| Black | 30 | 58.8% |
| White | 21 | 41.2% |

### Bossier Parish
**Total:** 1,122

| Race | Count | % |
|------|-------|---|
| Black | 623 | 55.5% |
| White | 498 | 44.4% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,684

| Race | Count | % |
|------|-------|---|
| Black | 1,277 | 75.8% |
| White | 380 | 22.6% |
| Unknown | 26 | 1.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Calcasieu Parish
**Total:** 1,101

| Race | Count | % |
|------|-------|---|
| Black | 611 | 55.5% |
| White | 449 | 40.8% |
| Unknown | 38 | 3.5% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 614

| Race | Count | % |
|------|-------|---|
| Black | 386 | 62.9% |
| White | 210 | 34.2% |
| American Indian/Alaska Native | 17 | 2.8% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 20

| Race | Count | % |
|------|-------|---|
| White | 18 | 90.0% |
| Black | 2 | 10.0% |

### Catahoula Parish
**Total:** 133

| Race | Count | % |
|------|-------|---|
| Black | 92 | 69.2% |
| White | 40 | 30.1% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 657

| Race | Count | % |
|------|-------|---|
| Black | 406 | 61.8% |
| White | 251 | 38.2% |

### Concordia Parish
**Total:** 818

| Race | Count | % |
|------|-------|---|
| White | 463 | 56.6% |
| Black | 355 | 43.4% |

### DeSoto Parish
**Total:** 125

| Race | Count | % |
|------|-------|---|
| Black | 75 | 60.0% |
| White | 49 | 39.2% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,329

| Race | Count | % |
|------|-------|---|
| Black | 1,048 | 78.9% |
| White | 214 | 16.1% |
| Unknown | 64 | 4.8% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### East Feliciana Parish
**Total:** 275

| Race | Count | % |
|------|-------|---|
| Black | 179 | 65.1% |
| White | 94 | 34.2% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 168

| Race | Count | % |
|------|-------|---|
| Black | 94 | 56.0% |
| White | 73 | 43.5% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 841

| Race | Count | % |
|------|-------|---|
| Black | 554 | 65.9% |
| White | 277 | 32.9% |
| Unknown | 10 | 1.2% |

### Hammond Police Department
**Total:** 14

| Race | Count | % |
|------|-------|---|
| Black | 9 | 64.3% |
| White | 5 | 35.7% |

### Iberia Parish
**Total:** 459

| Race | Count | % |
|------|-------|---|
| Black | 270 | 58.8% |
| White | 178 | 38.8% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 35

| Race | Count | % |
|------|-------|---|
| Black | 18 | 51.4% |
| White | 17 | 48.6% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 158

| Race | Count | % |
|------|-------|---|
| White | 85 | 53.8% |
| Black | 70 | 44.3% |
| American Indian/Alaska Native | 2 | 1.3% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,141

| Race | Count | % |
|------|-------|---|
| Black | 731 | 64.1% |
| White | 405 | 35.5% |
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
**Total:** 804

| Race | Count | % |
|------|-------|---|
| Black | 533 | 66.3% |
| White | 255 | 31.7% |
| Unknown | 16 | 2.0% |

### Lafourche Parish
**Total:** 760

| Race | Count | % |
|------|-------|---|
| Black | 393 | 51.7% |
| White | 363 | 47.8% |
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
**Total:** 827

| Race | Count | % |
|------|-------|---|
| White | 583 | 70.5% |
| Black | 233 | 28.2% |
| Unknown | 9 | 1.1% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 141

| Race | Count | % |
|------|-------|---|
| Black | 114 | 80.9% |
| White | 26 | 18.4% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 213

| Race | Count | % |
|------|-------|---|
| Black | 154 | 72.3% |
| White | 59 | 27.7% |

### Natchitoches Parish
**Total:** 184

| Race | Count | % |
|------|-------|---|
| Black | 136 | 73.9% |
| White | 44 | 23.9% |
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
**Total:** 1,353

| Race | Count | % |
|------|-------|---|
| Black | 898 | 66.4% |
| White | 439 | 32.4% |
| Unknown | 16 | 1.2% |

### Plaquemines Parish
**Total:** 677

| Race | Count | % |
|------|-------|---|
| Black | 441 | 65.1% |
| White | 215 | 31.8% |
| Unknown | 13 | 1.9% |
| Asian/PacificIslander | 7 | 1.0% |
| American Indian/Alaska Native | 1 | 0.1% |

### Pointe Coupee Parish
**Total:** 117

| Race | Count | % |
|------|-------|---|
| Black | 69 | 59.0% |
| White | 44 | 37.6% |
| Unknown | 3 | 2.6% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,046

| Race | Count | % |
|------|-------|---|
| Black | 659 | 63.0% |
| White | 370 | 35.4% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| Black | 21 | 48.8% |
| White | 21 | 48.8% |
| Asian/PacificIslander | 1 | 2.3% |

### Richland Parish
**Total:** 676

| Race | Count | % |
|------|-------|---|
| Black | 466 | 68.9% |
| White | 201 | 29.7% |
| Unknown | 6 | 0.9% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 197

| Race | Count | % |
|------|-------|---|
| White | 111 | 56.3% |
| Black | 83 | 42.1% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 46

| Race | Count | % |
|------|-------|---|
| Black | 35 | 76.1% |
| White | 11 | 23.9% |

### St. Bernard Parish
**Total:** 220

| Race | Count | % |
|------|-------|---|
| Black | 132 | 60.0% |
| White | 84 | 38.2% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 185

| Race | Count | % |
|------|-------|---|
| Unknown | 111 | 60.0% |
| White | 74 | 40.0% |

### St. Helena Parish
**Total:** 49

| Race | Count | % |
|------|-------|---|
| Black | 34 | 69.4% |
| White | 13 | 26.5% |
| Unknown | 2 | 4.1% |

### St. James Parish
**Total:** 73

| Race | Count | % |
|------|-------|---|
| Black | 60 | 82.2% |
| White | 13 | 17.8% |

### St. John the Baptist Parish
**Total:** 206

| Race | Count | % |
|------|-------|---|
| Unknown | 136 | 66.0% |
| White | 70 | 34.0% |

### St. Landry Parish
**Total:** 127

| Race | Count | % |
|------|-------|---|
| Black | 84 | 66.1% |
| White | 41 | 32.3% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 213

| Race | Count | % |
|------|-------|---|
| Black | 109 | 51.2% |
| White | 95 | 44.6% |
| Unknown | 8 | 3.8% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 296

| Race | Count | % |
|------|-------|---|
| Black | 154 | 52.0% |
| White | 141 | 47.6% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 875

| Race | Count | % |
|------|-------|---|
| White | 458 | 52.3% |
| Black | 376 | 43.0% |
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
**Total:** 682

| Race | Count | % |
|------|-------|---|
| Black | 442 | 64.8% |
| White | 238 | 34.9% |
| Unknown | 2 | 0.3% |

### Tensas Parish
**Total:** 562

| Race | Count | % |
|------|-------|---|
| Black | 376 | 66.9% |
| White | 174 | 31.0% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 559

| Race | Count | % |
|------|-------|---|
| Black | 304 | 54.4% |
| White | 244 | 43.6% |
| American Indian/Alaska Native | 10 | 1.8% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 136

| Race | Count | % |
|------|-------|---|
| White | 68 | 50.0% |
| Black | 65 | 47.8% |
| Unknown | 2 | 1.5% |
| Asian/PacificIslander | 1 | 0.7% |

### Vernon Parish
**Total:** 165

| Race | Count | % |
|------|-------|---|
| White | 113 | 68.5% |
| Black | 50 | 30.3% |
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
**Total:** 200

| Race | Count | % |
|------|-------|---|
| Black | 103 | 51.5% |
| White | 96 | 48.0% |
| Asian/PacificIslander | 1 | 0.5% |

### Webster Parish
**Total:** 441

| Race | Count | % |
|------|-------|---|
| Black | 237 | 53.7% |
| White | 198 | 44.9% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.5% |

### West Baton Rouge Parish
**Total:** 121

| Race | Count | % |
|------|-------|---|
| Black | 80 | 66.1% |
| White | 37 | 30.6% |
| Unknown | 2 | 1.7% |
| Asian/PacificIslander | 2 | 1.7% |

### West Carroll Parish
**Total:** 31

| Race | Count | % |
|------|-------|---|
| White | 25 | 80.6% |
| Black | 6 | 19.4% |

### West Felician Parish
**Total:** 200

| Race | Count | % |
|------|-------|---|
| Black | 127 | 63.5% |
| White | 73 | 36.5% |

### Winn Parish
**Total:** 155

| Race | Count | % |
|------|-------|---|
| White | 79 | 51.0% |
| Black | 76 | 49.0% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
