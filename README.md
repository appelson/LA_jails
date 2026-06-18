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

_Last updated: 2026-06-18 03:06 UTC_

**Total inmates (latest scrape):** 26,607 across 72 parishes/jails

### Acadia Parish
**Total:** 182

| Race | Count | % |
|------|-------|---|
| White | 99 | 54.4% |
| Black | 81 | 44.5% |
| Asian/PacificIslander | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Allen Parish
**Total:** 111

| Race | Count | % |
|------|-------|---|
| White | 71 | 64.0% |
| Black | 37 | 33.3% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 530

| Race | Count | % |
|------|-------|---|
| Black | 283 | 53.4% |
| White | 209 | 39.4% |
| Unknown | 34 | 6.4% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 155

| Race | Count | % |
|------|-------|---|
| Unknown | 83 | 53.5% |
| White | 72 | 46.5% |

### Avoyelles Parish
**Total:** 354

| Race | Count | % |
|------|-------|---|
| Black | 198 | 55.9% |
| White | 152 | 42.9% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 156

| Race | Count | % |
|------|-------|---|
| White | 110 | 70.5% |
| Black | 46 | 29.5% |

### Bienville Parish
**Total:** 36

| Race | Count | % |
|------|-------|---|
| White | 22 | 61.1% |
| Unknown | 14 | 38.9% |

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
| Black | 35 | 72.9% |
| White | 12 | 25.0% |
| Asian/PacificIslander | 1 | 2.1% |

### Bossier Parish
**Total:** 1,106

| Race | Count | % |
|------|-------|---|
| Black | 604 | 54.6% |
| White | 501 | 45.3% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,671

| Race | Count | % |
|------|-------|---|
| Black | 1,257 | 75.2% |
| White | 386 | 23.1% |
| Unknown | 26 | 1.6% |
| Asian/PacificIslander | 2 | 0.1% |

### Calcasieu Parish
**Total:** 1,091

| Race | Count | % |
|------|-------|---|
| Black | 605 | 55.5% |
| White | 443 | 40.6% |
| Unknown | 41 | 3.8% |
| Asian/PacificIslander | 2 | 0.2% |

### Caldwell Parish
**Total:** 622

| Race | Count | % |
|------|-------|---|
| Black | 393 | 63.2% |
| White | 208 | 33.4% |
| American Indian/Alaska Native | 20 | 3.2% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 26

| Race | Count | % |
|------|-------|---|
| White | 23 | 88.5% |
| Black | 3 | 11.5% |

### Catahoula Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| Black | 91 | 70.5% |
| White | 37 | 28.7% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 664

| Race | Count | % |
|------|-------|---|
| Black | 411 | 61.9% |
| White | 253 | 38.1% |

### Concordia Parish
**Total:** 802

| Race | Count | % |
|------|-------|---|
| White | 457 | 57.0% |
| Black | 343 | 42.8% |
| Unknown | 2 | 0.2% |

### DeSoto Parish
**Total:** 123

| Race | Count | % |
|------|-------|---|
| Black | 72 | 58.5% |
| White | 50 | 40.7% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,345

| Race | Count | % |
|------|-------|---|
| Black | 1,069 | 79.5% |
| White | 210 | 15.6% |
| Unknown | 63 | 4.7% |
| Asian/PacificIslander | 3 | 0.2% |

### East Feliciana Parish
**Total:** 269

| Race | Count | % |
|------|-------|---|
| Black | 172 | 63.9% |
| White | 96 | 35.7% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| Black | 84 | 55.6% |
| White | 66 | 43.7% |
| Unknown | 1 | 0.7% |

### Franklin Parish
**Total:** 841

| Race | Count | % |
|------|-------|---|
| Black | 545 | 64.8% |
| White | 285 | 33.9% |
| Unknown | 11 | 1.3% |

### Hammond Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| Black | 9 | 60.0% |
| White | 5 | 33.3% |
| Unknown | 1 | 6.7% |

### Iberia Parish
**Total:** 450

| Race | Count | % |
|------|-------|---|
| Black | 265 | 58.9% |
| White | 175 | 38.9% |
| Asian/PacificIslander | 5 | 1.1% |
| Unknown | 4 | 0.9% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 98

| Race | Count | % |
|------|-------|---|
| Black | 64 | 65.3% |
| White | 32 | 32.7% |
| Unknown | 2 | 2.0% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 153

| Race | Count | % |
|------|-------|---|
| White | 79 | 51.6% |
| Black | 70 | 45.8% |
| American Indian/Alaska Native | 3 | 2.0% |
| Unknown | 1 | 0.7% |

### Jefferson Parish
**Total:** 1,144

| Race | Count | % |
|------|-------|---|
| Black | 750 | 65.6% |
| White | 388 | 33.9% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 72

| Race | Count | % |
|------|-------|---|
| White | 46 | 63.9% |
| Black | 25 | 34.7% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 847

| Race | Count | % |
|------|-------|---|
| Black | 550 | 64.9% |
| White | 281 | 33.2% |
| Unknown | 16 | 1.9% |

### Lafourche Parish
**Total:** 750

| Race | Count | % |
|------|-------|---|
| Black | 384 | 51.2% |
| White | 361 | 48.1% |
| American Indian/Alaska Native | 4 | 0.5% |
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
| Black | 284 | 75.9% |
| White | 87 | 23.3% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 804

| Race | Count | % |
|------|-------|---|
| White | 571 | 71.0% |
| Black | 222 | 27.6% |
| Unknown | 9 | 1.1% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 143

| Race | Count | % |
|------|-------|---|
| Black | 114 | 79.7% |
| White | 28 | 19.6% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 207

| Race | Count | % |
|------|-------|---|
| Black | 142 | 68.6% |
| White | 65 | 31.4% |

### Natchitoches Parish
**Total:** 194

| Race | Count | % |
|------|-------|---|
| Black | 144 | 74.2% |
| White | 46 | 23.7% |
| Unknown | 4 | 2.1% |

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
**Total:** 1,333

| Race | Count | % |
|------|-------|---|
| Black | 887 | 66.5% |
| White | 431 | 32.3% |
| Unknown | 15 | 1.1% |

### Plaquemines Parish
**Total:** 653

| Race | Count | % |
|------|-------|---|
| Black | 433 | 66.3% |
| White | 200 | 30.6% |
| Unknown | 12 | 1.8% |
| Asian/PacificIslander | 6 | 0.9% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 106

| Race | Count | % |
|------|-------|---|
| Black | 66 | 62.3% |
| White | 37 | 34.9% |
| Unknown | 2 | 1.9% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,035

| Race | Count | % |
|------|-------|---|
| Black | 653 | 63.1% |
| White | 363 | 35.1% |
| Unknown | 17 | 1.6% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 46

| Race | Count | % |
|------|-------|---|
| Black | 27 | 58.7% |
| White | 18 | 39.1% |
| Asian/PacificIslander | 1 | 2.2% |

### Richland Parish
**Total:** 725

| Race | Count | % |
|------|-------|---|
| Black | 501 | 69.1% |
| White | 214 | 29.5% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 196

| Race | Count | % |
|------|-------|---|
| White | 105 | 53.6% |
| Black | 88 | 44.9% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 58

| Race | Count | % |
|------|-------|---|
| Black | 44 | 75.9% |
| White | 13 | 22.4% |
| Unknown | 1 | 1.7% |

### St. Bernard Parish
**Total:** 222

| Race | Count | % |
|------|-------|---|
| Black | 132 | 59.5% |
| White | 86 | 38.7% |
| Asian/PacificIslander | 3 | 1.4% |
| Unknown | 1 | 0.5% |

### St. Charles Parish
**Total:** 180

| Race | Count | % |
|------|-------|---|
| Unknown | 107 | 59.4% |
| White | 73 | 40.6% |

### St. Helena Parish
**Total:** 48

| Race | Count | % |
|------|-------|---|
| Black | 33 | 68.8% |
| White | 14 | 29.2% |
| Unknown | 1 | 2.1% |

### St. James Parish
**Total:** 69

| Race | Count | % |
|------|-------|---|
| Black | 58 | 84.1% |
| White | 11 | 15.9% |

### St. John the Baptist Parish
**Total:** 202

| Race | Count | % |
|------|-------|---|
| Unknown | 130 | 64.4% |
| White | 72 | 35.6% |

### St. Landry Parish
**Total:** 117

| Race | Count | % |
|------|-------|---|
| Black | 75 | 64.1% |
| White | 40 | 34.2% |
| Unknown | 2 | 1.7% |

### St. Martin Parish
**Total:** 210

| Race | Count | % |
|------|-------|---|
| Black | 106 | 50.5% |
| White | 94 | 44.8% |
| Unknown | 9 | 4.3% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 284

| Race | Count | % |
|------|-------|---|
| Black | 148 | 52.1% |
| White | 135 | 47.5% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 868

| Race | Count | % |
|------|-------|---|
| White | 452 | 52.1% |
| Black | 374 | 43.1% |
| Unknown | 39 | 4.5% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sulphur Police Department
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 14 | 82.4% |
| Black | 2 | 11.8% |
| Asian/PacificIslander | 1 | 5.9% |

### Tangipahoa Parish
**Total:** 664

| Race | Count | % |
|------|-------|---|
| Black | 418 | 63.0% |
| White | 245 | 36.9% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 560

| Race | Count | % |
|------|-------|---|
| Black | 372 | 66.4% |
| White | 178 | 31.8% |
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
**Total:** 128

| Race | Count | % |
|------|-------|---|
| White | 65 | 50.8% |
| Black | 59 | 46.1% |
| Unknown | 3 | 2.3% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 159

| Race | Count | % |
|------|-------|---|
| White | 108 | 67.9% |
| Black | 48 | 30.2% |
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
**Total:** 190

| Race | Count | % |
|------|-------|---|
| Black | 95 | 50.0% |
| White | 95 | 50.0% |

### Webster Parish
**Total:** 445

| Race | Count | % |
|------|-------|---|
| Black | 238 | 53.5% |
| White | 201 | 45.2% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 118

| Race | Count | % |
|------|-------|---|
| Black | 82 | 69.5% |
| White | 32 | 27.1% |
| Unknown | 3 | 2.5% |
| Asian/PacificIslander | 1 | 0.8% |

### West Carroll Parish
**Total:** 30

| Race | Count | % |
|------|-------|---|
| White | 24 | 80.0% |
| Black | 6 | 20.0% |

### West Felician Parish
**Total:** 188

| Race | Count | % |
|------|-------|---|
| Black | 123 | 65.4% |
| White | 65 | 34.6% |

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
