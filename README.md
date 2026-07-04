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

_Last updated: 2026-07-04 02:33 UTC_

**Total inmates (latest scrape):** 26,661 across 72 parishes/jails

### Acadia Parish
**Total:** 165

| Race | Count | % |
|------|-------|---|
| White | 94 | 57.0% |
| Black | 69 | 41.8% |
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
| White | 209 | 40.0% |
| Unknown | 31 | 5.9% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 155

| Race | Count | % |
|------|-------|---|
| Unknown | 86 | 55.5% |
| White | 69 | 44.5% |

### Avoyelles Parish
**Total:** 362

| Race | Count | % |
|------|-------|---|
| Black | 197 | 54.4% |
| White | 161 | 44.5% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 149

| Race | Count | % |
|------|-------|---|
| White | 105 | 70.5% |
| Black | 44 | 29.5% |

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
**Total:** 53

| Race | Count | % |
|------|-------|---|
| Black | 32 | 60.4% |
| White | 21 | 39.6% |

### Bossier Parish
**Total:** 1,129

| Race | Count | % |
|------|-------|---|
| Black | 626 | 55.4% |
| White | 501 | 44.4% |
| American Indian/Alaska Native | 1 | 0.1% |
| Unknown | 1 | 0.1% |

### Caddo Parish
**Total:** 1,684

| Race | Count | % |
|------|-------|---|
| Black | 1,270 | 75.4% |
| White | 386 | 22.9% |
| Unknown | 27 | 1.6% |
| Asian/PacificIslander | 1 | 0.1% |

### Calcasieu Parish
**Total:** 1,103

| Race | Count | % |
|------|-------|---|
| Black | 613 | 55.6% |
| White | 446 | 40.4% |
| Unknown | 41 | 3.7% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 620

| Race | Count | % |
|------|-------|---|
| Black | 391 | 63.1% |
| White | 208 | 33.5% |
| American Indian/Alaska Native | 20 | 3.2% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 18

| Race | Count | % |
|------|-------|---|
| White | 17 | 94.4% |
| Unknown | 1 | 5.6% |

### Catahoula Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 91 | 69.5% |
| White | 39 | 29.8% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 676

| Race | Count | % |
|------|-------|---|
| Black | 421 | 62.3% |
| White | 255 | 37.7% |

### Concordia Parish
**Total:** 798

| Race | Count | % |
|------|-------|---|
| White | 450 | 56.4% |
| Black | 347 | 43.5% |
| Unknown | 1 | 0.1% |

### DeSoto Parish
**Total:** 121

| Race | Count | % |
|------|-------|---|
| Black | 70 | 57.9% |
| White | 50 | 41.3% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,306

| Race | Count | % |
|------|-------|---|
| Black | 1,037 | 79.4% |
| White | 204 | 15.6% |
| Unknown | 64 | 4.9% |
| Asian/PacificIslander | 1 | 0.1% |

### East Feliciana Parish
**Total:** 271

| Race | Count | % |
|------|-------|---|
| Black | 174 | 64.2% |
| White | 96 | 35.4% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 168

| Race | Count | % |
|------|-------|---|
| Black | 92 | 54.8% |
| White | 75 | 44.6% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 845

| Race | Count | % |
|------|-------|---|
| Black | 553 | 65.4% |
| White | 281 | 33.3% |
| Unknown | 11 | 1.3% |

### Hammond Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| Black | 11 | 73.3% |
| White | 3 | 20.0% |
| Unknown | 1 | 6.7% |

### Iberia Parish
**Total:** 462

| Race | Count | % |
|------|-------|---|
| Black | 268 | 58.0% |
| White | 183 | 39.6% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 31

| Race | Count | % |
|------|-------|---|
| White | 18 | 58.1% |
| Black | 13 | 41.9% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 158

| Race | Count | % |
|------|-------|---|
| White | 84 | 53.2% |
| Black | 70 | 44.3% |
| American Indian/Alaska Native | 3 | 1.9% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,125

| Race | Count | % |
|------|-------|---|
| Black | 726 | 64.5% |
| White | 393 | 34.9% |
| Unknown | 5 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 78

| Race | Count | % |
|------|-------|---|
| White | 50 | 64.1% |
| Black | 27 | 34.6% |
| Unknown | 1 | 1.3% |

### Lafayette Parish
**Total:** 839

| Race | Count | % |
|------|-------|---|
| Black | 547 | 65.2% |
| White | 278 | 33.1% |
| Unknown | 13 | 1.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Lafourche Parish
**Total:** 758

| Race | Count | % |
|------|-------|---|
| Black | 389 | 51.3% |
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
**Total:** 374

| Race | Count | % |
|------|-------|---|
| Black | 279 | 74.6% |
| White | 92 | 24.6% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 830

| Race | Count | % |
|------|-------|---|
| White | 583 | 70.2% |
| Black | 235 | 28.3% |
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
| Black | 155 | 71.1% |
| White | 63 | 28.9% |

### Natchitoches Parish
**Total:** 183

| Race | Count | % |
|------|-------|---|
| Black | 135 | 73.8% |
| White | 45 | 24.6% |
| Unknown | 3 | 1.6% |

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
**Total:** 1,287

| Race | Count | % |
|------|-------|---|
| Black | 856 | 66.5% |
| White | 417 | 32.4% |
| Unknown | 14 | 1.1% |

### Plaquemines Parish
**Total:** 686

| Race | Count | % |
|------|-------|---|
| Black | 443 | 64.6% |
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
| Black | 658 | 64.2% |
| White | 351 | 34.2% |
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
**Total:** 691

| Race | Count | % |
|------|-------|---|
| Black | 475 | 68.7% |
| White | 206 | 29.8% |
| Unknown | 6 | 0.9% |
| Asian/PacificIslander | 4 | 0.6% |

### Sabine Parish
**Total:** 197

| Race | Count | % |
|------|-------|---|
| White | 110 | 55.8% |
| Black | 84 | 42.6% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 48

| Race | Count | % |
|------|-------|---|
| Black | 35 | 72.9% |
| White | 13 | 27.1% |

### St. Bernard Parish
**Total:** 217

| Race | Count | % |
|------|-------|---|
| Black | 130 | 59.9% |
| White | 84 | 38.7% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.5% |

### St. Charles Parish
**Total:** 189

| Race | Count | % |
|------|-------|---|
| Unknown | 117 | 61.9% |
| White | 72 | 38.1% |

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
| Black | 54 | 81.8% |
| White | 12 | 18.2% |

### St. John the Baptist Parish
**Total:** 207

| Race | Count | % |
|------|-------|---|
| Unknown | 134 | 64.7% |
| White | 73 | 35.3% |

### St. Landry Parish
**Total:** 128

| Race | Count | % |
|------|-------|---|
| Black | 84 | 65.6% |
| White | 42 | 32.8% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 214

| Race | Count | % |
|------|-------|---|
| Black | 111 | 51.9% |
| White | 93 | 43.5% |
| Unknown | 9 | 4.2% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 292

| Race | Count | % |
|------|-------|---|
| Black | 155 | 53.1% |
| White | 136 | 46.6% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 871

| Race | Count | % |
|------|-------|---|
| White | 461 | 52.9% |
| Black | 369 | 42.4% |
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
**Total:** 665

| Race | Count | % |
|------|-------|---|
| Black | 432 | 65.0% |
| White | 232 | 34.9% |
| Unknown | 1 | 0.2% |

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
**Total:** 133

| Race | Count | % |
|------|-------|---|
| White | 66 | 49.6% |
| Black | 64 | 48.1% |
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
**Total:** 195

| Race | Count | % |
|------|-------|---|
| White | 98 | 50.3% |
| Black | 97 | 49.7% |

### Webster Parish
**Total:** 446

| Race | Count | % |
|------|-------|---|
| Black | 238 | 53.4% |
| White | 202 | 45.3% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| Black | 87 | 67.4% |
| White | 36 | 27.9% |
| Unknown | 4 | 3.1% |
| Asian/PacificIslander | 2 | 1.6% |

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
**Total:** 151

| Race | Count | % |
|------|-------|---|
| Black | 78 | 51.7% |
| White | 73 | 48.3% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
