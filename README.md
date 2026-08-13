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

_Last updated: 2026-08-13 01:31 UTC_

**Total inmates (latest scrape):** 27,119 across 72 parishes/jails

### Acadia Parish
**Total:** 160

| Race | Count | % |
|------|-------|---|
| White | 87 | 54.4% |
| Black | 71 | 44.4% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| White | 74 | 61.7% |
| Black | 42 | 35.0% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 2 | 1.7% |

### Ascension Parish
**Total:** 517

| Race | Count | % |
|------|-------|---|
| Black | 271 | 52.4% |
| White | 209 | 40.4% |
| Unknown | 32 | 6.2% |
| Asian/PacificIslander | 5 | 1.0% |

### Assumption Parish
**Total:** 166

| Race | Count | % |
|------|-------|---|
| Unknown | 96 | 57.8% |
| White | 70 | 42.2% |

### Avoyelles Parish
**Total:** 360

| Race | Count | % |
|------|-------|---|
| Black | 202 | 56.1% |
| White | 155 | 43.1% |
| Unknown | 3 | 0.8% |

### Beauregard Parish
**Total:** 182

| Race | Count | % |
|------|-------|---|
| White | 115 | 63.2% |
| Black | 67 | 36.8% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 25

| Race | Count | % |
|------|-------|---|
| White | 18 | 72.0% |
| Black | 7 | 28.0% |

### Bossier City Police Department
**Total:** 56

| Race | Count | % |
|------|-------|---|
| Black | 38 | 67.9% |
| White | 18 | 32.1% |

### Bossier Parish
**Total:** 1,125

| Race | Count | % |
|------|-------|---|
| Black | 633 | 56.3% |
| White | 490 | 43.6% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Caddo Parish
**Total:** 1,730

| Race | Count | % |
|------|-------|---|
| Black | 1,312 | 75.8% |
| White | 387 | 22.4% |
| Unknown | 30 | 1.7% |
| Asian/PacificIslander | 1 | 0.1% |

### Calcasieu Parish
**Total:** 1,104

| Race | Count | % |
|------|-------|---|
| Black | 596 | 54.0% |
| White | 465 | 42.1% |
| Unknown | 42 | 3.8% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 610

| Race | Count | % |
|------|-------|---|
| Black | 393 | 64.4% |
| White | 200 | 32.8% |
| American Indian/Alaska Native | 15 | 2.5% |
| Unknown | 2 | 0.3% |

### Cameron Parish
**Total:** 22

| Race | Count | % |
|------|-------|---|
| White | 21 | 95.5% |
| Black | 1 | 4.5% |

### Catahoula Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 90 | 68.7% |
| White | 39 | 29.8% |
| Unknown | 2 | 1.5% |

### Claiborne Parish
**Total:** 640

| Race | Count | % |
|------|-------|---|
| Black | 396 | 61.9% |
| White | 244 | 38.1% |

### Concordia Parish
**Total:** 825

| Race | Count | % |
|------|-------|---|
| White | 471 | 57.1% |
| Black | 354 | 42.9% |

### DeSoto Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| Black | 74 | 57.4% |
| White | 55 | 42.6% |

### East Baton Rouge Parish
**Total:** 1,295

| Race | Count | % |
|------|-------|---|
| Black | 1,013 | 78.2% |
| White | 223 | 17.2% |
| Unknown | 55 | 4.2% |
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
**Total:** 168

| Race | Count | % |
|------|-------|---|
| Black | 98 | 58.3% |
| White | 69 | 41.1% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 853

| Race | Count | % |
|------|-------|---|
| Black | 566 | 66.4% |
| White | 282 | 33.1% |
| Unknown | 4 | 0.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 18

| Race | Count | % |
|------|-------|---|
| Black | 11 | 61.1% |
| White | 7 | 38.9% |

### Iberia Parish
**Total:** 463

| Race | Count | % |
|------|-------|---|
| Black | 278 | 60.0% |
| White | 173 | 37.4% |
| Unknown | 6 | 1.3% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 91

| Race | Count | % |
|------|-------|---|
| Black | 66 | 72.5% |
| White | 24 | 26.4% |
| Unknown | 1 | 1.1% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 166

| Race | Count | % |
|------|-------|---|
| White | 85 | 51.2% |
| Black | 79 | 47.6% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,233

| Race | Count | % |
|------|-------|---|
| Black | 805 | 65.3% |
| White | 422 | 34.2% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 78

| Race | Count | % |
|------|-------|---|
| White | 48 | 61.5% |
| Black | 29 | 37.2% |
| Unknown | 1 | 1.3% |

### Lafayette Parish
**Total:** 847

| Race | Count | % |
|------|-------|---|
| Black | 554 | 65.4% |
| White | 282 | 33.3% |
| Unknown | 11 | 1.3% |

### Lafourche Parish
**Total:** 776

| Race | Count | % |
|------|-------|---|
| Black | 389 | 50.1% |
| White | 383 | 49.4% |
| American Indian/Alaska Native | 3 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 370

| Race | Count | % |
|------|-------|---|
| Black | 279 | 75.4% |
| White | 87 | 23.5% |
| Unknown | 4 | 1.1% |

### Livingston Parish
**Total:** 832

| Race | Count | % |
|------|-------|---|
| White | 588 | 70.7% |
| Black | 236 | 28.4% |
| Unknown | 5 | 0.6% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 148

| Race | Count | % |
|------|-------|---|
| Black | 120 | 81.1% |
| White | 27 | 18.2% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 198

| Race | Count | % |
|------|-------|---|
| Black | 143 | 72.2% |
| White | 55 | 27.8% |

### Natchitoches Parish
**Total:** 188

| Race | Count | % |
|------|-------|---|
| Black | 145 | 77.1% |
| White | 39 | 20.7% |
| Unknown | 4 | 2.1% |

### Oakdale Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Black | 1 | 100.0% |

### Opelousas Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| African American | 1 | 100.0% |

### Orleans Parish
**Total:** 1,455

| Race | Count | % |
|------|-------|---|
| Black | 1,255 | 86.3% |
| White | 181 | 12.4% |
| Unknown | 14 | 1.0% |
| Asian/PacificIslander | 5 | 0.3% |

### Ouachita Parish
**Total:** 1,336

| Race | Count | % |
|------|-------|---|
| Black | 900 | 67.4% |
| White | 426 | 31.9% |
| Unknown | 10 | 0.7% |

### Plaquemines Parish
**Total:** 667

| Race | Count | % |
|------|-------|---|
| Black | 432 | 64.8% |
| White | 209 | 31.3% |
| Unknown | 14 | 2.1% |
| Asian/PacificIslander | 10 | 1.5% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 128

| Race | Count | % |
|------|-------|---|
| Black | 84 | 65.6% |
| White | 41 | 32.0% |
| Unknown | 2 | 1.6% |
| American Indian/Alaska Native | 1 | 0.8% |

### Rapides Parish
**Total:** 1,039

| Race | Count | % |
|------|-------|---|
| Black | 663 | 63.8% |
| White | 359 | 34.6% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 23 | 52.3% |
| White | 20 | 45.5% |
| Asian/PacificIslander | 1 | 2.3% |

### Richland Parish
**Total:** 695

| Race | Count | % |
|------|-------|---|
| Black | 479 | 68.9% |
| White | 208 | 29.9% |
| Unknown | 5 | 0.7% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 183

| Race | Count | % |
|------|-------|---|
| White | 107 | 58.5% |
| Black | 74 | 40.4% |
| Unknown | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 35

| Race | Count | % |
|------|-------|---|
| Black | 25 | 71.4% |
| White | 9 | 25.7% |
| Unknown | 1 | 2.9% |

### St. Bernard Parish
**Total:** 233

| Race | Count | % |
|------|-------|---|
| Black | 143 | 61.4% |
| White | 87 | 37.3% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.4% |

### St. Charles Parish
**Total:** 174

| Race | Count | % |
|------|-------|---|
| Unknown | 99 | 56.9% |
| White | 75 | 43.1% |

### St. Helena Parish
**Total:** 46

| Race | Count | % |
|------|-------|---|
| Black | 36 | 78.3% |
| White | 10 | 21.7% |

### St. James Parish
**Total:** 75

| Race | Count | % |
|------|-------|---|
| Black | 63 | 84.0% |
| White | 12 | 16.0% |

### St. John the Baptist Parish
**Total:** 223

| Race | Count | % |
|------|-------|---|
| Unknown | 147 | 65.9% |
| White | 76 | 34.1% |

### St. Landry Parish
**Total:** 136

| Race | Count | % |
|------|-------|---|
| Black | 90 | 66.2% |
| White | 44 | 32.4% |
| Unknown | 2 | 1.5% |

### St. Martin Parish
**Total:** 227

| Race | Count | % |
|------|-------|---|
| Black | 112 | 49.3% |
| White | 107 | 47.1% |
| Unknown | 8 | 3.5% |

### St. Mary Parish
**Total:** 282

| Race | Count | % |
|------|-------|---|
| Black | 144 | 51.1% |
| White | 136 | 48.2% |
| Unknown | 1 | 0.4% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 865

| Race | Count | % |
|------|-------|---|
| White | 441 | 51.0% |
| Black | 381 | 44.0% |
| Unknown | 41 | 4.7% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 14

| Race | Count | % |
|------|-------|---|
| White | 12 | 85.7% |
| Black | 2 | 14.3% |

### Tangipahoa Parish
**Total:** 709

| Race | Count | % |
|------|-------|---|
| Black | 465 | 65.6% |
| White | 241 | 34.0% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 564

| Race | Count | % |
|------|-------|---|
| Black | 380 | 67.4% |
| White | 170 | 30.1% |
| Unknown | 14 | 2.5% |

### Terrebonne Parish
**Total:** 585

| Race | Count | % |
|------|-------|---|
| Black | 332 | 56.8% |
| White | 239 | 40.9% |
| American Indian/Alaska Native | 13 | 2.2% |
| Asian/PacificIslander | 1 | 0.2% |

### Vermillion Parish
**Total:** 119

| Race | Count | % |
|------|-------|---|
| White | 58 | 48.7% |
| Black | 58 | 48.7% |
| Unknown | 2 | 1.7% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 171

| Race | Count | % |
|------|-------|---|
| White | 121 | 70.8% |
| Black | 48 | 28.1% |
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
**Total:** 182

| Race | Count | % |
|------|-------|---|
| Black | 93 | 51.1% |
| White | 88 | 48.4% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 445

| Race | Count | % |
|------|-------|---|
| Black | 230 | 51.7% |
| White | 209 | 47.0% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 134

| Race | Count | % |
|------|-------|---|
| Black | 88 | 65.7% |
| White | 42 | 31.3% |
| Unknown | 3 | 2.2% |
| Asian/PacificIslander | 1 | 0.7% |

### West Carroll Parish
**Total:** 27

| Race | Count | % |
|------|-------|---|
| White | 21 | 77.8% |
| Black | 6 | 22.2% |

### West Felician Parish
**Total:** 199

| Race | Count | % |
|------|-------|---|
| Black | 126 | 63.3% |
| White | 73 | 36.7% |

### Winn Parish
**Total:** 148

| Race | Count | % |
|------|-------|---|
| Black | 76 | 51.4% |
| White | 72 | 48.6% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
