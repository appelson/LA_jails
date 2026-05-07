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

_Last updated: 2026-05-07 02:34 UTC_

**Total inmates (latest scrape):** 25,802 across 72 parishes/jails

### Acadia Parish
**Total:** 173

| Race | Count | % |
|------|-------|---|
| White | 91 | 52.6% |
| Black | 80 | 46.2% |
| Asian/PacificIslander | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 122

| Race | Count | % |
|------|-------|---|
| White | 74 | 60.7% |
| Black | 45 | 36.9% |
| American Indian/Alaska Native | 2 | 1.6% |
| Unknown | 1 | 0.8% |

### Ascension Parish
**Total:** 500

| Race | Count | % |
|------|-------|---|
| Black | 263 | 52.6% |
| White | 202 | 40.4% |
| Unknown | 31 | 6.2% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 144

| Race | Count | % |
|------|-------|---|
| Unknown | 74 | 51.4% |
| White | 70 | 48.6% |

### Avoyelles Parish
**Total:** 390

| Race | Count | % |
|------|-------|---|
| Black | 207 | 53.1% |
| White | 177 | 45.4% |
| Unknown | 5 | 1.3% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 168

| Race | Count | % |
|------|-------|---|
| White | 118 | 70.2% |
| Black | 50 | 29.8% |

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
**Total:** 45

| Race | Count | % |
|------|-------|---|
| Black | 29 | 64.4% |
| White | 16 | 35.6% |

### Bossier Parish
**Total:** 1,126

| Race | Count | % |
|------|-------|---|
| Black | 619 | 55.0% |
| White | 504 | 44.8% |
| Unknown | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,609

| Race | Count | % |
|------|-------|---|
| Black | 1,189 | 73.9% |
| White | 384 | 23.9% |
| Unknown | 33 | 2.1% |
| Asian/PacificIslander | 3 | 0.2% |

### Calcasieu Parish
**Total:** 1,026

| Race | Count | % |
|------|-------|---|
| Black | 558 | 54.4% |
| White | 425 | 41.4% |
| Unknown | 41 | 4.0% |
| Asian/PacificIslander | 2 | 0.2% |

### Caldwell Parish
**Total:** 615

| Race | Count | % |
|------|-------|---|
| Black | 398 | 64.7% |
| White | 196 | 31.9% |
| American Indian/Alaska Native | 20 | 3.3% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 16 | 94.1% |
| Black | 1 | 5.9% |

### Catahoula Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| Black | 92 | 69.7% |
| White | 39 | 29.5% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 670

| Race | Count | % |
|------|-------|---|
| Black | 412 | 61.5% |
| White | 258 | 38.5% |

### Concordia Parish
**Total:** 821

| Race | Count | % |
|------|-------|---|
| White | 458 | 55.8% |
| Black | 359 | 43.7% |
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
**Total:** 265

| Race | Count | % |
|------|-------|---|
| Black | 163 | 61.5% |
| White | 101 | 38.1% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 83

| Race | Count | % |
|------|-------|---|
| White | 44 | 53.0% |
| Black | 38 | 45.8% |
| Unknown | 1 | 1.2% |

### Franklin Parish
**Total:** 849

| Race | Count | % |
|------|-------|---|
| Black | 555 | 65.4% |
| White | 282 | 33.2% |
| Unknown | 11 | 1.3% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 8

| Race | Count | % |
|------|-------|---|
| Black | 6 | 75.0% |
| White | 2 | 25.0% |

### Iberia Parish
**Total:** 440

| Race | Count | % |
|------|-------|---|
| Black | 274 | 62.3% |
| White | 159 | 36.1% |
| Unknown | 3 | 0.7% |
| Asian/PacificIslander | 3 | 0.7% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 107

| Race | Count | % |
|------|-------|---|
| Black | 67 | 62.6% |
| White | 38 | 35.5% |
| Unknown | 2 | 1.9% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 148

| Race | Count | % |
|------|-------|---|
| White | 73 | 49.3% |
| Black | 70 | 47.3% |
| American Indian/Alaska Native | 3 | 2.0% |
| Asian/PacificIslander | 1 | 0.7% |
| Unknown | 1 | 0.7% |

### Jefferson Parish
**Total:** 1,191

| Race | Count | % |
|------|-------|---|
| Black | 778 | 65.3% |
| White | 400 | 33.6% |
| Unknown | 9 | 0.8% |
| Asian/PacificIslander | 4 | 0.3% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Black | 1 | 100.0% |

### LaSalle Parish
**Total:** 73

| Race | Count | % |
|------|-------|---|
| White | 51 | 69.9% |
| Black | 21 | 28.8% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 845

| Race | Count | % |
|------|-------|---|
| Black | 534 | 63.2% |
| White | 299 | 35.4% |
| Unknown | 12 | 1.4% |

### Lafourche Parish
**Total:** 750

| Race | Count | % |
|------|-------|---|
| Black | 382 | 50.9% |
| White | 361 | 48.1% |
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
**Total:** 371

| Race | Count | % |
|------|-------|---|
| Black | 276 | 74.4% |
| White | 93 | 25.1% |
| Unknown | 2 | 0.5% |

### Livingston Parish
**Total:** 803

| Race | Count | % |
|------|-------|---|
| White | 577 | 71.9% |
| Black | 216 | 26.9% |
| Unknown | 7 | 0.9% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 138

| Race | Count | % |
|------|-------|---|
| Black | 107 | 77.5% |
| White | 30 | 21.7% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 207

| Race | Count | % |
|------|-------|---|
| Black | 141 | 68.1% |
| White | 66 | 31.9% |

### Natchitoches Parish
**Total:** 197

| Race | Count | % |
|------|-------|---|
| Black | 143 | 72.6% |
| White | 50 | 25.4% |
| Unknown | 3 | 1.5% |
| Asian/PacificIslander | 1 | 0.5% |

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
**Total:** 1,276

| Race | Count | % |
|------|-------|---|
| Black | 848 | 66.5% |
| White | 414 | 32.4% |
| Unknown | 14 | 1.1% |

### Plaquemines Parish
**Total:** 635

| Race | Count | % |
|------|-------|---|
| Black | 412 | 64.9% |
| White | 203 | 32.0% |
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
**Total:** 987

| Race | Count | % |
|------|-------|---|
| Black | 618 | 62.6% |
| White | 351 | 35.6% |
| Unknown | 16 | 1.6% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 39

| Race | Count | % |
|------|-------|---|
| Black | 24 | 61.5% |
| White | 14 | 35.9% |
| Asian/PacificIslander | 1 | 2.6% |

### Richland Parish
**Total:** 713

| Race | Count | % |
|------|-------|---|
| Black | 489 | 68.6% |
| White | 214 | 30.0% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 182

| Race | Count | % |
|------|-------|---|
| White | 104 | 57.1% |
| Black | 78 | 42.9% |

### Shreveport Police Department
**Total:** 48

| Race | Count | % |
|------|-------|---|
| Black | 41 | 85.4% |
| White | 7 | 14.6% |

### St. Bernard Parish
**Total:** 218

| Race | Count | % |
|------|-------|---|
| Black | 129 | 59.2% |
| White | 86 | 39.4% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.5% |

### St. Charles Parish
**Total:** 172

| Race | Count | % |
|------|-------|---|
| Unknown | 98 | 57.0% |
| White | 74 | 43.0% |

### St. Helena Parish
**Total:** 78

| Race | Count | % |
|------|-------|---|
| Black | 56 | 71.8% |
| White | 17 | 21.8% |
| Unknown | 4 | 5.1% |
| American Indian/Alaska Native | 1 | 1.3% |

### St. James Parish
**Total:** 78

| Race | Count | % |
|------|-------|---|
| Black | 62 | 79.5% |
| White | 16 | 20.5% |

### St. John the Baptist Parish
**Total:** 196

| Race | Count | % |
|------|-------|---|
| Unknown | 123 | 62.8% |
| White | 73 | 37.2% |

### St. Landry Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| Black | 70 | 62.5% |
| White | 40 | 35.7% |
| Unknown | 2 | 1.8% |

### St. Martin Parish
**Total:** 190

| Race | Count | % |
|------|-------|---|
| Black | 93 | 48.9% |
| White | 89 | 46.8% |
| Unknown | 7 | 3.7% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 243

| Race | Count | % |
|------|-------|---|
| Black | 124 | 51.0% |
| White | 118 | 48.6% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 808

| Race | Count | % |
|------|-------|---|
| White | 407 | 50.4% |
| Black | 360 | 44.6% |
| Unknown | 36 | 4.5% |
| Asian/PacificIslander | 3 | 0.4% |
| American Indian/Alaska Native | 2 | 0.2% |

### Sulphur Police Department
**Total:** 16

| Race | Count | % |
|------|-------|---|
| White | 14 | 87.5% |
| Black | 2 | 12.5% |

### Tangipahoa Parish
**Total:** 630

| Race | Count | % |
|------|-------|---|
| Black | 384 | 61.0% |
| White | 245 | 38.9% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 555

| Race | Count | % |
|------|-------|---|
| Black | 364 | 65.6% |
| White | 175 | 31.5% |
| Unknown | 16 | 2.9% |

### Terrebonne Parish
**Total:** 470

| Race | Count | % |
|------|-------|---|
| Black | 244 | 51.9% |
| White | 219 | 46.6% |
| American Indian/Alaska Native | 7 | 1.5% |

### Vermillion Parish
**Total:** 128

| Race | Count | % |
|------|-------|---|
| White | 68 | 53.1% |
| Black | 58 | 45.3% |
| Unknown | 2 | 1.6% |

### Vernon Parish
**Total:** 154

| Race | Count | % |
|------|-------|---|
| White | 103 | 66.9% |
| Black | 48 | 31.2% |
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
**Total:** 160

| Race | Count | % |
|------|-------|---|
| Black | 86 | 53.8% |
| White | 74 | 46.2% |

### Webster Parish
**Total:** 436

| Race | Count | % |
|------|-------|---|
| Black | 215 | 49.3% |
| White | 214 | 49.1% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 3 | 0.7% |

### West Baton Rouge Parish
**Total:** 139

| Race | Count | % |
|------|-------|---|
| Black | 87 | 62.6% |
| White | 48 | 34.5% |
| Unknown | 3 | 2.2% |
| Asian/PacificIslander | 1 | 0.7% |

### West Carroll Parish
**Total:** 30

| Race | Count | % |
|------|-------|---|
| White | 26 | 86.7% |
| Black | 3 | 10.0% |
| Unknown | 1 | 3.3% |

### West Felician Parish
**Total:** 177

| Race | Count | % |
|------|-------|---|
| Black | 110 | 62.1% |
| White | 67 | 37.9% |

### Winn Parish
**Total:** 148

| Race | Count | % |
|------|-------|---|
| White | 75 | 50.7% |
| Black | 73 | 49.3% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
