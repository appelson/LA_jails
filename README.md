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

_Last updated: 2026-05-16 02:37 UTC_

**Total inmates (latest scrape):** 25,835 across 72 parishes/jails

### Acadia Parish
**Total:** 178

| Race | Count | % |
|------|-------|---|
| White | 92 | 51.7% |
| Black | 84 | 47.2% |
| Asian/PacificIslander | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| White | 79 | 61.2% |
| Black | 47 | 36.4% |
| American Indian/Alaska Native | 2 | 1.6% |
| Unknown | 1 | 0.8% |

### Ascension Parish
**Total:** 505

| Race | Count | % |
|------|-------|---|
| Black | 266 | 52.7% |
| White | 207 | 41.0% |
| Unknown | 28 | 5.5% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 147

| Race | Count | % |
|------|-------|---|
| Unknown | 79 | 53.7% |
| White | 68 | 46.3% |

### Avoyelles Parish
**Total:** 374

| Race | Count | % |
|------|-------|---|
| Black | 198 | 52.9% |
| White | 172 | 46.0% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 168

| Race | Count | % |
|------|-------|---|
| White | 115 | 68.5% |
| Black | 53 | 31.5% |

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
| Black | 33 | 68.8% |
| White | 15 | 31.2% |

### Bossier Parish
**Total:** 1,121

| Race | Count | % |
|------|-------|---|
| Black | 620 | 55.3% |
| White | 499 | 44.5% |
| American Indian/Alaska Native | 1 | 0.1% |
| Unknown | 1 | 0.1% |

### Caddo Parish
**Total:** 1,606

| Race | Count | % |
|------|-------|---|
| Black | 1,189 | 74.0% |
| White | 386 | 24.0% |
| Unknown | 29 | 1.8% |
| Asian/PacificIslander | 2 | 0.1% |

### Calcasieu Parish
**Total:** 1,033

| Race | Count | % |
|------|-------|---|
| Black | 564 | 54.6% |
| White | 428 | 41.4% |
| Unknown | 40 | 3.9% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 607

| Race | Count | % |
|------|-------|---|
| Black | 390 | 64.3% |
| White | 198 | 32.6% |
| American Indian/Alaska Native | 19 | 3.1% |

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
| Black | 91 | 68.4% |
| White | 41 | 30.8% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 649

| Race | Count | % |
|------|-------|---|
| Black | 396 | 61.0% |
| White | 253 | 39.0% |

### Concordia Parish
**Total:** 801

| Race | Count | % |
|------|-------|---|
| White | 447 | 55.8% |
| Black | 350 | 43.7% |
| Unknown | 4 | 0.5% |

### DeSoto Parish
**Total:** 117

| Race | Count | % |
|------|-------|---|
| Black | 70 | 59.8% |
| White | 46 | 39.3% |
| Asian/PacificIslander | 1 | 0.9% |

### East Baton Rouge Parish
**Total:** 1,046

| Race | Count | % |
|------|-------|---|
| Black | 798 | 76.3% |
| White | 196 | 18.7% |
| Unknown | 51 | 4.9% |
| Asian/PacificIslander | 1 | 0.1% |

### East Feliciana Parish
**Total:** 263

| Race | Count | % |
|------|-------|---|
| Black | 162 | 61.6% |
| White | 100 | 38.0% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 102

| Race | Count | % |
|------|-------|---|
| Black | 53 | 52.0% |
| White | 48 | 47.1% |
| Unknown | 1 | 1.0% |

### Franklin Parish
**Total:** 826

| Race | Count | % |
|------|-------|---|
| Black | 533 | 64.5% |
| White | 282 | 34.1% |
| Unknown | 10 | 1.2% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 8

| Race | Count | % |
|------|-------|---|
| Black | 7 | 87.5% |
| White | 1 | 12.5% |

### Iberia Parish
**Total:** 445

| Race | Count | % |
|------|-------|---|
| Black | 270 | 60.7% |
| White | 166 | 37.3% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 4 | 0.9% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 109

| Race | Count | % |
|------|-------|---|
| Black | 68 | 62.4% |
| White | 39 | 35.8% |
| Unknown | 2 | 1.8% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 150

| Race | Count | % |
|------|-------|---|
| White | 77 | 51.3% |
| Black | 68 | 45.3% |
| American Indian/Alaska Native | 3 | 2.0% |
| Asian/PacificIslander | 1 | 0.7% |
| Unknown | 1 | 0.7% |

### Jefferson Parish
**Total:** 1,164

| Race | Count | % |
|------|-------|---|
| Black | 771 | 66.2% |
| White | 381 | 32.7% |
| Unknown | 9 | 0.8% |
| Asian/PacificIslander | 3 | 0.3% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Black | 1 | 100.0% |

### LaSalle Parish
**Total:** 70

| Race | Count | % |
|------|-------|---|
| White | 49 | 70.0% |
| Black | 20 | 28.6% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 851

| Race | Count | % |
|------|-------|---|
| Black | 552 | 64.9% |
| White | 287 | 33.7% |
| Unknown | 12 | 1.4% |

### Lafourche Parish
**Total:** 735

| Race | Count | % |
|------|-------|---|
| Black | 383 | 52.1% |
| White | 345 | 46.9% |
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
**Total:** 367

| Race | Count | % |
|------|-------|---|
| Black | 272 | 74.1% |
| White | 92 | 25.1% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 778

| Race | Count | % |
|------|-------|---|
| White | 555 | 71.3% |
| Black | 214 | 27.5% |
| Unknown | 7 | 0.9% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| Black | 103 | 78.0% |
| White | 28 | 21.2% |
| Unknown | 1 | 0.8% |

### Morehouse Parish
**Total:** 203

| Race | Count | % |
|------|-------|---|
| Black | 138 | 68.0% |
| White | 65 | 32.0% |

### Natchitoches Parish
**Total:** 196

| Race | Count | % |
|------|-------|---|
| Black | 147 | 75.0% |
| White | 45 | 23.0% |
| Unknown | 3 | 1.5% |
| Asian/PacificIslander | 1 | 0.5% |

### Oakdale Police Department
**Total:** 7

| Race | Count | % |
|------|-------|---|
| White | 4 | 57.1% |
| Black | 2 | 28.6% |
| Unknown | 1 | 14.3% |

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
**Total:** 1,290

| Race | Count | % |
|------|-------|---|
| Black | 872 | 67.6% |
| White | 401 | 31.1% |
| Unknown | 17 | 1.3% |

### Plaquemines Parish
**Total:** 647

| Race | Count | % |
|------|-------|---|
| Black | 423 | 65.4% |
| White | 205 | 31.7% |
| Unknown | 12 | 1.9% |
| Asian/PacificIslander | 6 | 0.9% |
| American Indian/Alaska Native | 1 | 0.2% |

### Pointe Coupee Parish
**Total:** 103

| Race | Count | % |
|------|-------|---|
| Black | 68 | 66.0% |
| White | 34 | 33.0% |
| Unknown | 1 | 1.0% |

### Rapides Parish
**Total:** 999

| Race | Count | % |
|------|-------|---|
| Black | 618 | 61.9% |
| White | 364 | 36.4% |
| Unknown | 15 | 1.5% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 41

| Race | Count | % |
|------|-------|---|
| Black | 23 | 56.1% |
| White | 17 | 41.5% |
| Asian/PacificIslander | 1 | 2.4% |

### Richland Parish
**Total:** 715

| Race | Count | % |
|------|-------|---|
| Black | 486 | 68.0% |
| White | 218 | 30.5% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sabine Parish
**Total:** 182

| Race | Count | % |
|------|-------|---|
| White | 102 | 56.0% |
| Black | 80 | 44.0% |

### Shreveport Police Department
**Total:** 47

| Race | Count | % |
|------|-------|---|
| Black | 37 | 78.7% |
| White | 10 | 21.3% |

### St. Bernard Parish
**Total:** 230

| Race | Count | % |
|------|-------|---|
| Black | 128 | 55.7% |
| White | 97 | 42.2% |
| Unknown | 3 | 1.3% |
| Asian/PacificIslander | 2 | 0.9% |

### St. Charles Parish
**Total:** 170

| Race | Count | % |
|------|-------|---|
| Unknown | 100 | 58.8% |
| White | 70 | 41.2% |

### St. Helena Parish
**Total:** 76

| Race | Count | % |
|------|-------|---|
| Black | 54 | 71.1% |
| White | 17 | 22.4% |
| Unknown | 4 | 5.3% |
| American Indian/Alaska Native | 1 | 1.3% |

### St. James Parish
**Total:** 75

| Race | Count | % |
|------|-------|---|
| Black | 59 | 78.7% |
| White | 16 | 21.3% |

### St. John the Baptist Parish
**Total:** 204

| Race | Count | % |
|------|-------|---|
| Unknown | 129 | 63.2% |
| White | 75 | 36.8% |

### St. Landry Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| Black | 70 | 62.5% |
| White | 40 | 35.7% |
| Unknown | 2 | 1.8% |

### St. Martin Parish
**Total:** 196

| Race | Count | % |
|------|-------|---|
| White | 95 | 48.5% |
| Black | 93 | 47.4% |
| Unknown | 7 | 3.6% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 258

| Race | Count | % |
|------|-------|---|
| Black | 135 | 52.3% |
| White | 122 | 47.3% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 822

| Race | Count | % |
|------|-------|---|
| White | 426 | 51.8% |
| Black | 356 | 43.3% |
| Unknown | 35 | 4.3% |
| Asian/PacificIslander | 3 | 0.4% |
| American Indian/Alaska Native | 2 | 0.2% |

### Sulphur Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| White | 13 | 86.7% |
| Black | 2 | 13.3% |

### Tangipahoa Parish
**Total:** 649

| Race | Count | % |
|------|-------|---|
| Black | 401 | 61.8% |
| White | 247 | 38.1% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 570

| Race | Count | % |
|------|-------|---|
| Black | 377 | 66.1% |
| White | 178 | 31.2% |
| Unknown | 15 | 2.6% |

### Terrebonne Parish
**Total:** 479

| Race | Count | % |
|------|-------|---|
| Black | 251 | 52.4% |
| White | 221 | 46.1% |
| American Indian/Alaska Native | 6 | 1.3% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 133

| Race | Count | % |
|------|-------|---|
| White | 73 | 54.9% |
| Black | 58 | 43.6% |
| Unknown | 2 | 1.5% |

### Vernon Parish
**Total:** 163

| Race | Count | % |
|------|-------|---|
| White | 109 | 66.9% |
| Black | 51 | 31.3% |
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
**Total:** 169

| Race | Count | % |
|------|-------|---|
| Black | 88 | 52.1% |
| White | 81 | 47.9% |

### Webster Parish
**Total:** 431

| Race | Count | % |
|------|-------|---|
| Black | 214 | 49.7% |
| White | 210 | 48.7% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 3 | 0.7% |

### West Baton Rouge Parish
**Total:** 137

| Race | Count | % |
|------|-------|---|
| Black | 87 | 63.5% |
| White | 44 | 32.1% |
| Unknown | 5 | 3.6% |
| Asian/PacificIslander | 1 | 0.7% |

### West Carroll Parish
**Total:** 26

| Race | Count | % |
|------|-------|---|
| White | 23 | 88.5% |
| Black | 3 | 11.5% |

### West Felician Parish
**Total:** 182

| Race | Count | % |
|------|-------|---|
| Black | 116 | 63.7% |
| White | 66 | 36.3% |

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
