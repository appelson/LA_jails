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

_Last updated: 2026-07-28 02:08 UTC_

**Total inmates (latest scrape):** 26,979 across 72 parishes/jails

### Acadia Parish
**Total:** 174

| Race | Count | % |
|------|-------|---|
| White | 99 | 56.9% |
| Black | 74 | 42.5% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 122

| Race | Count | % |
|------|-------|---|
| White | 77 | 63.1% |
| Black | 41 | 33.6% |
| Unknown | 2 | 1.6% |
| American Indian/Alaska Native | 2 | 1.6% |

### Ascension Parish
**Total:** 506

| Race | Count | % |
|------|-------|---|
| Black | 266 | 52.6% |
| White | 204 | 40.3% |
| Unknown | 32 | 6.3% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 155

| Race | Count | % |
|------|-------|---|
| Unknown | 87 | 56.1% |
| White | 68 | 43.9% |

### Avoyelles Parish
**Total:** 352

| Race | Count | % |
|------|-------|---|
| Black | 199 | 56.5% |
| White | 150 | 42.6% |
| Unknown | 3 | 0.9% |

### Beauregard Parish
**Total:** 174

| Race | Count | % |
|------|-------|---|
| White | 118 | 67.8% |
| Black | 56 | 32.2% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 13

| Race | Count | % |
|------|-------|---|
| White | 7 | 53.8% |
| Black | 6 | 46.2% |

### Bossier City Police Department
**Total:** 55

| Race | Count | % |
|------|-------|---|
| Black | 39 | 70.9% |
| White | 16 | 29.1% |

### Bossier Parish
**Total:** 1,127

| Race | Count | % |
|------|-------|---|
| Black | 637 | 56.5% |
| White | 488 | 43.3% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Caddo Parish
**Total:** 1,711

| Race | Count | % |
|------|-------|---|
| Black | 1,292 | 75.5% |
| White | 394 | 23.0% |
| Unknown | 25 | 1.5% |

### Calcasieu Parish
**Total:** 1,102

| Race | Count | % |
|------|-------|---|
| Black | 611 | 55.4% |
| White | 448 | 40.7% |
| Unknown | 42 | 3.8% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 605

| Race | Count | % |
|------|-------|---|
| Black | 385 | 63.6% |
| White | 204 | 33.7% |
| American Indian/Alaska Native | 15 | 2.5% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 20

| Race | Count | % |
|------|-------|---|
| White | 19 | 95.0% |
| Black | 1 | 5.0% |

### Catahoula Parish
**Total:** 128

| Race | Count | % |
|------|-------|---|
| Black | 90 | 70.3% |
| White | 37 | 28.9% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 660

| Race | Count | % |
|------|-------|---|
| Black | 411 | 62.3% |
| White | 249 | 37.7% |

### Concordia Parish
**Total:** 809

| Race | Count | % |
|------|-------|---|
| White | 458 | 56.6% |
| Black | 351 | 43.4% |

### DeSoto Parish
**Total:** 115

| Race | Count | % |
|------|-------|---|
| Black | 70 | 60.9% |
| White | 44 | 38.3% |
| Asian/PacificIslander | 1 | 0.9% |

### East Baton Rouge Parish
**Total:** 1,354

| Race | Count | % |
|------|-------|---|
| Black | 1,056 | 78.0% |
| White | 235 | 17.4% |
| Unknown | 58 | 4.3% |
| Asian/PacificIslander | 4 | 0.3% |
| American Indian/Alaska Native | 1 | 0.1% |

### East Feliciana Parish
**Total:** 279

| Race | Count | % |
|------|-------|---|
| Black | 183 | 65.6% |
| White | 94 | 33.7% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 152

| Race | Count | % |
|------|-------|---|
| Black | 89 | 58.6% |
| White | 62 | 40.8% |
| Unknown | 1 | 0.7% |

### Franklin Parish
**Total:** 830

| Race | Count | % |
|------|-------|---|
| Black | 550 | 66.3% |
| White | 275 | 33.1% |
| Unknown | 5 | 0.6% |

### Hammond Police Department
**Total:** 20

| Race | Count | % |
|------|-------|---|
| Black | 13 | 65.0% |
| White | 6 | 30.0% |
| Unknown | 1 | 5.0% |

### Iberia Parish
**Total:** 470

| Race | Count | % |
|------|-------|---|
| Black | 282 | 60.0% |
| White | 177 | 37.7% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 48

| Race | Count | % |
|------|-------|---|
| Black | 30 | 62.5% |
| White | 18 | 37.5% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 162

| Race | Count | % |
|------|-------|---|
| White | 84 | 51.9% |
| Black | 75 | 46.3% |
| American Indian/Alaska Native | 2 | 1.2% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,204

| Race | Count | % |
|------|-------|---|
| Black | 776 | 64.5% |
| White | 422 | 35.0% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 1 | 50.0% |
| White | 1 | 50.0% |

### LaSalle Parish
**Total:** 78

| Race | Count | % |
|------|-------|---|
| White | 54 | 69.2% |
| Black | 23 | 29.5% |
| Unknown | 1 | 1.3% |

### Lafayette Parish
**Total:** 832

| Race | Count | % |
|------|-------|---|
| Black | 548 | 65.9% |
| White | 270 | 32.5% |
| Unknown | 14 | 1.7% |

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
**Total:** 365

| Race | Count | % |
|------|-------|---|
| Black | 272 | 74.5% |
| White | 90 | 24.7% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 835

| Race | Count | % |
|------|-------|---|
| White | 598 | 71.6% |
| Black | 226 | 27.1% |
| Unknown | 8 | 1.0% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 153

| Race | Count | % |
|------|-------|---|
| Black | 122 | 79.7% |
| White | 30 | 19.6% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 210

| Race | Count | % |
|------|-------|---|
| Black | 154 | 73.3% |
| White | 56 | 26.7% |

### Natchitoches Parish
**Total:** 184

| Race | Count | % |
|------|-------|---|
| Black | 140 | 76.1% |
| White | 41 | 22.3% |
| Unknown | 3 | 1.6% |

### Oakdale Police Department
**Total:** 5

| Race | Count | % |
|------|-------|---|
| White | 4 | 80.0% |
| Black | 1 | 20.0% |

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
**Total:** 1,347

| Race | Count | % |
|------|-------|---|
| Black | 894 | 66.4% |
| White | 436 | 32.4% |
| Unknown | 17 | 1.3% |

### Plaquemines Parish
**Total:** 674

| Race | Count | % |
|------|-------|---|
| Black | 442 | 65.6% |
| White | 208 | 30.9% |
| Unknown | 13 | 1.9% |
| Asian/PacificIslander | 9 | 1.3% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 118

| Race | Count | % |
|------|-------|---|
| Black | 73 | 61.9% |
| White | 42 | 35.6% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.8% |

### Rapides Parish
**Total:** 1,049

| Race | Count | % |
|------|-------|---|
| Black | 665 | 63.4% |
| White | 367 | 35.0% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 41

| Race | Count | % |
|------|-------|---|
| Black | 21 | 51.2% |
| White | 19 | 46.3% |
| Asian/PacificIslander | 1 | 2.4% |

### Richland Parish
**Total:** 712

| Race | Count | % |
|------|-------|---|
| Black | 492 | 69.1% |
| White | 211 | 29.6% |
| Unknown | 6 | 0.8% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 186

| Race | Count | % |
|------|-------|---|
| White | 107 | 57.5% |
| Black | 76 | 40.9% |
| Unknown | 2 | 1.1% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 36

| Race | Count | % |
|------|-------|---|
| Black | 28 | 77.8% |
| White | 8 | 22.2% |

### St. Bernard Parish
**Total:** 226

| Race | Count | % |
|------|-------|---|
| Black | 133 | 58.8% |
| White | 88 | 38.9% |
| Asian/PacificIslander | 3 | 1.3% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 185

| Race | Count | % |
|------|-------|---|
| Unknown | 106 | 57.3% |
| White | 79 | 42.7% |

### St. Helena Parish
**Total:** 47

| Race | Count | % |
|------|-------|---|
| Black | 33 | 70.2% |
| White | 13 | 27.7% |
| Unknown | 1 | 2.1% |

### St. James Parish
**Total:** 78

| Race | Count | % |
|------|-------|---|
| Black | 65 | 83.3% |
| White | 13 | 16.7% |

### St. John the Baptist Parish
**Total:** 220

| Race | Count | % |
|------|-------|---|
| Unknown | 144 | 65.5% |
| White | 76 | 34.5% |

### St. Landry Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| Black | 87 | 67.4% |
| White | 40 | 31.0% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 213

| Race | Count | % |
|------|-------|---|
| Black | 107 | 50.2% |
| White | 98 | 46.0% |
| Unknown | 8 | 3.8% |

### St. Mary Parish
**Total:** 289

| Race | Count | % |
|------|-------|---|
| Black | 155 | 53.6% |
| White | 133 | 46.0% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 881

| Race | Count | % |
|------|-------|---|
| White | 451 | 51.2% |
| Black | 386 | 43.8% |
| Unknown | 42 | 4.8% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| White | 12 | 80.0% |
| Black | 3 | 20.0% |

### Tangipahoa Parish
**Total:** 703

| Race | Count | % |
|------|-------|---|
| Black | 461 | 65.6% |
| White | 239 | 34.0% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 558

| Race | Count | % |
|------|-------|---|
| Black | 381 | 68.3% |
| White | 165 | 29.6% |
| Unknown | 12 | 2.2% |

### Terrebonne Parish
**Total:** 579

| Race | Count | % |
|------|-------|---|
| Black | 317 | 54.7% |
| White | 250 | 43.2% |
| American Indian/Alaska Native | 12 | 2.1% |

### Vermillion Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| White | 61 | 50.8% |
| Black | 56 | 46.7% |
| Unknown | 2 | 1.7% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 176

| Race | Count | % |
|------|-------|---|
| White | 119 | 67.6% |
| Black | 55 | 31.2% |
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
**Total:** 192

| Race | Count | % |
|------|-------|---|
| Black | 102 | 53.1% |
| White | 89 | 46.4% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 460

| Race | Count | % |
|------|-------|---|
| Black | 247 | 53.7% |
| White | 206 | 44.8% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 133

| Race | Count | % |
|------|-------|---|
| Black | 87 | 65.4% |
| White | 41 | 30.8% |
| Unknown | 3 | 2.3% |
| Asian/PacificIslander | 2 | 1.5% |

### West Carroll Parish
**Total:** 28

| Race | Count | % |
|------|-------|---|
| White | 22 | 78.6% |
| Black | 6 | 21.4% |

### West Felician Parish
**Total:** 203

| Race | Count | % |
|------|-------|---|
| Black | 131 | 64.5% |
| White | 72 | 35.5% |

### Winn Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| Black | 76 | 50.3% |
| White | 75 | 49.7% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
