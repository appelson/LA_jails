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

_Last updated: 2026-06-24 02:51 UTC_

**Total inmates (latest scrape):** 26,674 across 72 parishes/jails

### Acadia Parish
**Total:** 184

| Race | Count | % |
|------|-------|---|
| White | 98 | 53.3% |
| Black | 84 | 45.7% |
| Asian/PacificIslander | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Allen Parish
**Total:** 113

| Race | Count | % |
|------|-------|---|
| White | 71 | 62.8% |
| Black | 39 | 34.5% |
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
**Total:** 153

| Race | Count | % |
|------|-------|---|
| Unknown | 84 | 54.9% |
| White | 69 | 45.1% |

### Avoyelles Parish
**Total:** 352

| Race | Count | % |
|------|-------|---|
| Black | 194 | 55.1% |
| White | 154 | 43.8% |
| Unknown | 3 | 0.9% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 140

| Race | Count | % |
|------|-------|---|
| White | 97 | 69.3% |
| Black | 43 | 30.7% |

### Bienville Parish
**Total:** 40

| Race | Count | % |
|------|-------|---|
| White | 23 | 57.5% |
| Unknown | 17 | 42.5% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 40

| Race | Count | % |
|------|-------|---|
| Black | 27 | 67.5% |
| White | 12 | 30.0% |
| Asian/PacificIslander | 1 | 2.5% |

### Bossier Parish
**Total:** 1,110

| Race | Count | % |
|------|-------|---|
| Black | 610 | 55.0% |
| White | 499 | 45.0% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,689

| Race | Count | % |
|------|-------|---|
| Black | 1,272 | 75.3% |
| White | 389 | 23.0% |
| Unknown | 26 | 1.5% |
| Asian/PacificIslander | 2 | 0.1% |

### Calcasieu Parish
**Total:** 1,092

| Race | Count | % |
|------|-------|---|
| Black | 611 | 56.0% |
| White | 441 | 40.4% |
| Unknown | 37 | 3.4% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 625

| Race | Count | % |
|------|-------|---|
| Black | 396 | 63.4% |
| White | 208 | 33.3% |
| American Indian/Alaska Native | 20 | 3.2% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 22

| Race | Count | % |
|------|-------|---|
| White | 19 | 86.4% |
| Black | 3 | 13.6% |

### Catahoula Parish
**Total:** 133

| Race | Count | % |
|------|-------|---|
| Black | 93 | 69.9% |
| White | 39 | 29.3% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 681

| Race | Count | % |
|------|-------|---|
| Black | 419 | 61.5% |
| White | 262 | 38.5% |

### Concordia Parish
**Total:** 816

| Race | Count | % |
|------|-------|---|
| White | 463 | 56.7% |
| Black | 351 | 43.0% |
| Unknown | 2 | 0.2% |

### DeSoto Parish
**Total:** 124

| Race | Count | % |
|------|-------|---|
| Black | 71 | 57.3% |
| White | 52 | 41.9% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,330

| Race | Count | % |
|------|-------|---|
| Black | 1,057 | 79.5% |
| White | 204 | 15.3% |
| Unknown | 67 | 5.0% |
| Asian/PacificIslander | 2 | 0.2% |

### East Feliciana Parish
**Total:** 266

| Race | Count | % |
|------|-------|---|
| Black | 170 | 63.9% |
| White | 95 | 35.7% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 158

| Race | Count | % |
|------|-------|---|
| Black | 88 | 55.7% |
| White | 69 | 43.7% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 841

| Race | Count | % |
|------|-------|---|
| Black | 548 | 65.2% |
| White | 282 | 33.5% |
| Unknown | 11 | 1.3% |

### Hammond Police Department
**Total:** 8

| Race | Count | % |
|------|-------|---|
| Black | 5 | 62.5% |
| White | 3 | 37.5% |

### Iberia Parish
**Total:** 451

| Race | Count | % |
|------|-------|---|
| Black | 261 | 57.9% |
| White | 180 | 39.9% |
| Asian/PacificIslander | 5 | 1.1% |
| Unknown | 4 | 0.9% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 89

| Race | Count | % |
|------|-------|---|
| Black | 58 | 65.2% |
| White | 30 | 33.7% |
| Unknown | 1 | 1.1% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 162

| Race | Count | % |
|------|-------|---|
| White | 85 | 52.5% |
| Black | 73 | 45.1% |
| American Indian/Alaska Native | 3 | 1.9% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,161

| Race | Count | % |
|------|-------|---|
| Black | 756 | 65.1% |
| White | 399 | 34.4% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 74

| Race | Count | % |
|------|-------|---|
| White | 49 | 66.2% |
| Black | 24 | 32.4% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 834

| Race | Count | % |
|------|-------|---|
| Black | 542 | 65.0% |
| White | 278 | 33.3% |
| Unknown | 13 | 1.6% |
| Asian/PacificIslander | 1 | 0.1% |

### Lafourche Parish
**Total:** 744

| Race | Count | % |
|------|-------|---|
| Black | 383 | 51.5% |
| White | 356 | 47.8% |
| American Indian/Alaska Native | 4 | 0.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 366

| Race | Count | % |
|------|-------|---|
| Black | 273 | 74.6% |
| White | 90 | 24.6% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 812

| Race | Count | % |
|------|-------|---|
| White | 578 | 71.2% |
| Black | 223 | 27.5% |
| Unknown | 9 | 1.1% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 142

| Race | Count | % |
|------|-------|---|
| Black | 113 | 79.6% |
| White | 28 | 19.7% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 215

| Race | Count | % |
|------|-------|---|
| Black | 153 | 71.2% |
| White | 62 | 28.8% |

### Natchitoches Parish
**Total:** 199

| Race | Count | % |
|------|-------|---|
| Black | 146 | 73.4% |
| White | 48 | 24.1% |
| Unknown | 5 | 2.5% |

### Oakdale Police Department
**Total:** 5

| Race | Count | % |
|------|-------|---|
| White | 5 | 100.0% |

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
**Total:** 1,336

| Race | Count | % |
|------|-------|---|
| Black | 887 | 66.4% |
| White | 433 | 32.4% |
| Unknown | 16 | 1.2% |

### Plaquemines Parish
**Total:** 676

| Race | Count | % |
|------|-------|---|
| Black | 446 | 66.0% |
| White | 206 | 30.5% |
| Unknown | 12 | 1.8% |
| Asian/PacificIslander | 8 | 1.2% |
| American Indian/Alaska Native | 4 | 0.6% |

### Pointe Coupee Parish
**Total:** 105

| Race | Count | % |
|------|-------|---|
| Black | 64 | 61.0% |
| White | 38 | 36.2% |
| Unknown | 2 | 1.9% |
| American Indian/Alaska Native | 1 | 1.0% |

### Rapides Parish
**Total:** 1,042

| Race | Count | % |
|------|-------|---|
| Black | 665 | 63.8% |
| White | 359 | 34.5% |
| Unknown | 16 | 1.5% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 24 | 54.5% |
| White | 19 | 43.2% |
| Asian/PacificIslander | 1 | 2.3% |

### Richland Parish
**Total:** 723

| Race | Count | % |
|------|-------|---|
| Black | 499 | 69.0% |
| White | 214 | 29.6% |
| Unknown | 6 | 0.8% |
| Asian/PacificIslander | 4 | 0.6% |

### Sabine Parish
**Total:** 192

| Race | Count | % |
|------|-------|---|
| White | 106 | 55.2% |
| Black | 83 | 43.2% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 63

| Race | Count | % |
|------|-------|---|
| Black | 49 | 77.8% |
| White | 14 | 22.2% |

### St. Bernard Parish
**Total:** 222

| Race | Count | % |
|------|-------|---|
| Black | 130 | 58.6% |
| White | 89 | 40.1% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.5% |

### St. Charles Parish
**Total:** 187

| Race | Count | % |
|------|-------|---|
| Unknown | 118 | 63.1% |
| White | 69 | 36.9% |

### St. Helena Parish
**Total:** 51

| Race | Count | % |
|------|-------|---|
| Black | 36 | 70.6% |
| White | 14 | 27.5% |
| Unknown | 1 | 2.0% |

### St. James Parish
**Total:** 64

| Race | Count | % |
|------|-------|---|
| Black | 54 | 84.4% |
| White | 10 | 15.6% |

### St. John the Baptist Parish
**Total:** 201

| Race | Count | % |
|------|-------|---|
| Unknown | 130 | 64.7% |
| White | 71 | 35.3% |

### St. Landry Parish
**Total:** 118

| Race | Count | % |
|------|-------|---|
| Black | 77 | 65.3% |
| White | 39 | 33.1% |
| Unknown | 2 | 1.7% |

### St. Martin Parish
**Total:** 212

| Race | Count | % |
|------|-------|---|
| Black | 109 | 51.4% |
| White | 93 | 43.9% |
| Unknown | 9 | 4.2% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 279

| Race | Count | % |
|------|-------|---|
| Black | 144 | 51.6% |
| White | 134 | 48.0% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 847

| Race | Count | % |
|------|-------|---|
| White | 448 | 52.9% |
| Black | 361 | 42.6% |
| Unknown | 35 | 4.1% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sulphur Police Department
**Total:** 20

| Race | Count | % |
|------|-------|---|
| White | 18 | 90.0% |
| Black | 2 | 10.0% |

### Tangipahoa Parish
**Total:** 664

| Race | Count | % |
|------|-------|---|
| Black | 417 | 62.8% |
| White | 246 | 37.0% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 559

| Race | Count | % |
|------|-------|---|
| Black | 375 | 67.1% |
| White | 174 | 31.1% |
| Unknown | 10 | 1.8% |

### Terrebonne Parish
**Total:** 506

| Race | Count | % |
|------|-------|---|
| Black | 271 | 53.6% |
| White | 225 | 44.5% |
| American Indian/Alaska Native | 9 | 1.8% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| White | 66 | 50.4% |
| Black | 62 | 47.3% |
| Unknown | 2 | 1.5% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 167

| Race | Count | % |
|------|-------|---|
| White | 115 | 68.9% |
| Black | 49 | 29.3% |
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
**Total:** 188

| Race | Count | % |
|------|-------|---|
| Black | 95 | 50.5% |
| White | 93 | 49.5% |

### Webster Parish
**Total:** 446

| Race | Count | % |
|------|-------|---|
| Black | 239 | 53.6% |
| White | 201 | 45.1% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| Black | 92 | 69.7% |
| White | 36 | 27.3% |
| Unknown | 3 | 2.3% |
| Asian/PacificIslander | 1 | 0.8% |

### West Carroll Parish
**Total:** 30

| Race | Count | % |
|------|-------|---|
| White | 24 | 80.0% |
| Black | 6 | 20.0% |

### West Felician Parish
**Total:** 191

| Race | Count | % |
|------|-------|---|
| Black | 125 | 65.4% |
| White | 66 | 34.6% |

### Winn Parish
**Total:** 143

| Race | Count | % |
|------|-------|---|
| Black | 75 | 52.4% |
| White | 68 | 47.6% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
