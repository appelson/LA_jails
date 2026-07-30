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

_Last updated: 2026-07-30 02:01 UTC_

**Total inmates (latest scrape):** 26,923 across 72 parishes/jails

### Acadia Parish
**Total:** 158

| Race | Count | % |
|------|-------|---|
| White | 90 | 57.0% |
| Black | 66 | 41.8% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 118

| Race | Count | % |
|------|-------|---|
| White | 74 | 62.7% |
| Black | 40 | 33.9% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 2 | 1.7% |

### Ascension Parish
**Total:** 511

| Race | Count | % |
|------|-------|---|
| Black | 273 | 53.4% |
| White | 201 | 39.3% |
| Unknown | 33 | 6.5% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 152

| Race | Count | % |
|------|-------|---|
| Unknown | 85 | 55.9% |
| White | 67 | 44.1% |

### Avoyelles Parish
**Total:** 352

| Race | Count | % |
|------|-------|---|
| Black | 199 | 56.5% |
| White | 150 | 42.6% |
| Unknown | 3 | 0.9% |

### Beauregard Parish
**Total:** 176

| Race | Count | % |
|------|-------|---|
| White | 120 | 68.2% |
| Black | 56 | 31.8% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 14

| Race | Count | % |
|------|-------|---|
| White | 8 | 57.1% |
| Black | 6 | 42.9% |

### Bossier City Police Department
**Total:** 61

| Race | Count | % |
|------|-------|---|
| Black | 45 | 73.8% |
| White | 16 | 26.2% |

### Bossier Parish
**Total:** 1,119

| Race | Count | % |
|------|-------|---|
| Black | 629 | 56.2% |
| White | 488 | 43.6% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Caddo Parish
**Total:** 1,710

| Race | Count | % |
|------|-------|---|
| Black | 1,294 | 75.7% |
| White | 390 | 22.8% |
| Unknown | 26 | 1.5% |

### Calcasieu Parish
**Total:** 1,106

| Race | Count | % |
|------|-------|---|
| Black | 612 | 55.3% |
| White | 452 | 40.9% |
| Unknown | 41 | 3.7% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 607

| Race | Count | % |
|------|-------|---|
| Black | 390 | 64.3% |
| White | 201 | 33.1% |
| American Indian/Alaska Native | 15 | 2.5% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 20

| Race | Count | % |
|------|-------|---|
| White | 20 | 100.0% |

### Catahoula Parish
**Total:** 128

| Race | Count | % |
|------|-------|---|
| Black | 91 | 71.1% |
| White | 36 | 28.1% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 657

| Race | Count | % |
|------|-------|---|
| Black | 407 | 61.9% |
| White | 250 | 38.1% |

### Concordia Parish
**Total:** 812

| Race | Count | % |
|------|-------|---|
| White | 460 | 56.7% |
| Black | 352 | 43.3% |

### DeSoto Parish
**Total:** 122

| Race | Count | % |
|------|-------|---|
| Black | 74 | 60.7% |
| White | 47 | 38.5% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,324

| Race | Count | % |
|------|-------|---|
| Black | 1,023 | 77.3% |
| White | 235 | 17.7% |
| Unknown | 63 | 4.8% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### East Feliciana Parish
**Total:** 281

| Race | Count | % |
|------|-------|---|
| Black | 185 | 65.8% |
| White | 94 | 33.5% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 159

| Race | Count | % |
|------|-------|---|
| Black | 95 | 59.7% |
| White | 63 | 39.6% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 844

| Race | Count | % |
|------|-------|---|
| Black | 561 | 66.5% |
| White | 279 | 33.1% |
| Unknown | 4 | 0.5% |

### Hammond Police Department
**Total:** 20

| Race | Count | % |
|------|-------|---|
| Black | 13 | 65.0% |
| White | 6 | 30.0% |
| Unknown | 1 | 5.0% |

### Iberia Parish
**Total:** 475

| Race | Count | % |
|------|-------|---|
| Black | 286 | 60.2% |
| White | 177 | 37.3% |
| Unknown | 6 | 1.3% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 46

| Race | Count | % |
|------|-------|---|
| Black | 28 | 60.9% |
| White | 18 | 39.1% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 164

| Race | Count | % |
|------|-------|---|
| White | 84 | 51.2% |
| Black | 77 | 47.0% |
| American Indian/Alaska Native | 2 | 1.2% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,192

| Race | Count | % |
|------|-------|---|
| Black | 766 | 64.3% |
| White | 420 | 35.2% |
| Unknown | 6 | 0.5% |

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
**Total:** 841

| Race | Count | % |
|------|-------|---|
| Black | 557 | 66.2% |
| White | 273 | 32.5% |
| Unknown | 11 | 1.3% |

### Lafourche Parish
**Total:** 760

| Race | Count | % |
|------|-------|---|
| Black | 389 | 51.2% |
| White | 367 | 48.3% |
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
**Total:** 841

| Race | Count | % |
|------|-------|---|
| White | 600 | 71.3% |
| Black | 230 | 27.3% |
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
**Total:** 206

| Race | Count | % |
|------|-------|---|
| Black | 152 | 73.8% |
| White | 54 | 26.2% |

### Natchitoches Parish
**Total:** 184

| Race | Count | % |
|------|-------|---|
| Black | 139 | 75.5% |
| White | 41 | 22.3% |
| Unknown | 4 | 2.2% |

### Oakdale Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 3 | 100.0% |

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
**Total:** 1,333

| Race | Count | % |
|------|-------|---|
| Black | 894 | 67.1% |
| White | 424 | 31.8% |
| Unknown | 15 | 1.1% |

### Plaquemines Parish
**Total:** 657

| Race | Count | % |
|------|-------|---|
| Black | 427 | 65.0% |
| White | 207 | 31.5% |
| Unknown | 12 | 1.8% |
| Asian/PacificIslander | 9 | 1.4% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 118

| Race | Count | % |
|------|-------|---|
| Black | 72 | 61.0% |
| White | 43 | 36.4% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.8% |

### Rapides Parish
**Total:** 1,047

| Race | Count | % |
|------|-------|---|
| Black | 662 | 63.2% |
| White | 368 | 35.1% |
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
**Total:** 706

| Race | Count | % |
|------|-------|---|
| Black | 490 | 69.4% |
| White | 208 | 29.5% |
| Unknown | 5 | 0.7% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 184

| Race | Count | % |
|------|-------|---|
| White | 105 | 57.1% |
| Black | 76 | 41.3% |
| Unknown | 2 | 1.1% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 43

| Race | Count | % |
|------|-------|---|
| Black | 33 | 76.7% |
| White | 9 | 20.9% |
| Unknown | 1 | 2.3% |

### St. Bernard Parish
**Total:** 231

| Race | Count | % |
|------|-------|---|
| Black | 135 | 58.4% |
| White | 91 | 39.4% |
| Asian/PacificIslander | 3 | 1.3% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 176

| Race | Count | % |
|------|-------|---|
| Unknown | 100 | 56.8% |
| White | 76 | 43.2% |

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
| Black | 64 | 82.1% |
| White | 14 | 17.9% |

### St. John the Baptist Parish
**Total:** 222

| Race | Count | % |
|------|-------|---|
| Unknown | 146 | 65.8% |
| White | 76 | 34.2% |

### St. Landry Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 86 | 65.6% |
| White | 43 | 32.8% |
| Unknown | 2 | 1.5% |

### St. Martin Parish
**Total:** 210

| Race | Count | % |
|------|-------|---|
| Black | 104 | 49.5% |
| White | 98 | 46.7% |
| Unknown | 8 | 3.8% |

### St. Mary Parish
**Total:** 284

| Race | Count | % |
|------|-------|---|
| Black | 151 | 53.2% |
| White | 132 | 46.5% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 890

| Race | Count | % |
|------|-------|---|
| White | 456 | 51.2% |
| Black | 391 | 43.9% |
| Unknown | 41 | 4.6% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 14

| Race | Count | % |
|------|-------|---|
| White | 10 | 71.4% |
| Black | 4 | 28.6% |

### Tangipahoa Parish
**Total:** 702

| Race | Count | % |
|------|-------|---|
| Black | 461 | 65.7% |
| White | 238 | 33.9% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 568

| Race | Count | % |
|------|-------|---|
| Black | 384 | 67.6% |
| White | 172 | 30.3% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 578

| Race | Count | % |
|------|-------|---|
| Black | 319 | 55.2% |
| White | 247 | 42.7% |
| American Indian/Alaska Native | 12 | 2.1% |

### Vermillion Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| Black | 59 | 49.2% |
| White | 58 | 48.3% |
| Unknown | 2 | 1.7% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 177

| Race | Count | % |
|------|-------|---|
| White | 123 | 69.5% |
| Black | 52 | 29.4% |
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
**Total:** 186

| Race | Count | % |
|------|-------|---|
| Black | 96 | 51.6% |
| White | 89 | 47.8% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 451

| Race | Count | % |
|------|-------|---|
| Black | 237 | 52.5% |
| White | 207 | 45.9% |
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
**Total:** 201

| Race | Count | % |
|------|-------|---|
| Black | 129 | 64.2% |
| White | 72 | 35.8% |

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
