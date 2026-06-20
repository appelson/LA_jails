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

_Last updated: 2026-06-20 02:57 UTC_

**Total inmates (latest scrape):** 26,577 across 72 parishes/jails

### Acadia Parish
**Total:** 183

| Race | Count | % |
|------|-------|---|
| White | 98 | 53.6% |
| Black | 83 | 45.4% |
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
**Total:** 523

| Race | Count | % |
|------|-------|---|
| Black | 281 | 53.7% |
| White | 206 | 39.4% |
| Unknown | 32 | 6.1% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 154

| Race | Count | % |
|------|-------|---|
| Unknown | 85 | 55.2% |
| White | 69 | 44.8% |

### Avoyelles Parish
**Total:** 353

| Race | Count | % |
|------|-------|---|
| Black | 196 | 55.5% |
| White | 153 | 43.3% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 153

| Race | Count | % |
|------|-------|---|
| White | 106 | 69.3% |
| Black | 47 | 30.7% |

### Bienville Parish
**Total:** 39

| Race | Count | % |
|------|-------|---|
| White | 24 | 61.5% |
| Unknown | 15 | 38.5% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 55

| Race | Count | % |
|------|-------|---|
| Black | 39 | 70.9% |
| White | 15 | 27.3% |
| Asian/PacificIslander | 1 | 1.8% |

### Bossier Parish
**Total:** 1,093

| Race | Count | % |
|------|-------|---|
| Black | 595 | 54.4% |
| White | 497 | 45.5% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,679

| Race | Count | % |
|------|-------|---|
| Black | 1,262 | 75.2% |
| White | 389 | 23.2% |
| Unknown | 26 | 1.5% |
| Asian/PacificIslander | 2 | 0.1% |

### Calcasieu Parish
**Total:** 1,092

| Race | Count | % |
|------|-------|---|
| Black | 610 | 55.9% |
| White | 441 | 40.4% |
| Unknown | 38 | 3.5% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 625

| Race | Count | % |
|------|-------|---|
| Black | 395 | 63.2% |
| White | 209 | 33.4% |
| American Indian/Alaska Native | 20 | 3.2% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 23

| Race | Count | % |
|------|-------|---|
| White | 20 | 87.0% |
| Black | 3 | 13.0% |

### Catahoula Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| Black | 91 | 70.5% |
| White | 37 | 28.7% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 661

| Race | Count | % |
|------|-------|---|
| Black | 410 | 62.0% |
| White | 251 | 38.0% |

### Concordia Parish
**Total:** 810

| Race | Count | % |
|------|-------|---|
| White | 460 | 56.8% |
| Black | 348 | 43.0% |
| Unknown | 2 | 0.2% |

### DeSoto Parish
**Total:** 124

| Race | Count | % |
|------|-------|---|
| Black | 72 | 58.1% |
| White | 51 | 41.1% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,314

| Race | Count | % |
|------|-------|---|
| Black | 1,039 | 79.1% |
| White | 207 | 15.8% |
| Unknown | 65 | 4.9% |
| Asian/PacificIslander | 3 | 0.2% |

### East Feliciana Parish
**Total:** 266

| Race | Count | % |
|------|-------|---|
| Black | 170 | 63.9% |
| White | 95 | 35.7% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 149

| Race | Count | % |
|------|-------|---|
| Black | 84 | 56.4% |
| White | 64 | 43.0% |
| Unknown | 1 | 0.7% |

### Franklin Parish
**Total:** 843

| Race | Count | % |
|------|-------|---|
| Black | 546 | 64.8% |
| White | 286 | 33.9% |
| Unknown | 11 | 1.3% |

### Hammond Police Department
**Total:** 10

| Race | Count | % |
|------|-------|---|
| Black | 7 | 70.0% |
| White | 3 | 30.0% |

### Iberia Parish
**Total:** 456

| Race | Count | % |
|------|-------|---|
| Black | 263 | 57.7% |
| White | 182 | 39.9% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 95

| Race | Count | % |
|------|-------|---|
| Black | 63 | 66.3% |
| White | 31 | 32.6% |
| Unknown | 1 | 1.1% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 159

| Race | Count | % |
|------|-------|---|
| White | 84 | 52.8% |
| Black | 71 | 44.7% |
| American Indian/Alaska Native | 3 | 1.9% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,124

| Race | Count | % |
|------|-------|---|
| Black | 734 | 65.3% |
| White | 384 | 34.2% |
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
**Total:** 843

| Race | Count | % |
|------|-------|---|
| Black | 552 | 65.5% |
| White | 278 | 33.0% |
| Unknown | 13 | 1.5% |

### Lafourche Parish
**Total:** 753

| Race | Count | % |
|------|-------|---|
| Black | 388 | 51.5% |
| White | 360 | 47.8% |
| American Indian/Alaska Native | 4 | 0.5% |
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
| Black | 281 | 75.9% |
| White | 86 | 23.2% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 810

| Race | Count | % |
|------|-------|---|
| White | 580 | 71.6% |
| Black | 219 | 27.0% |
| Unknown | 9 | 1.1% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 144

| Race | Count | % |
|------|-------|---|
| Black | 115 | 79.9% |
| White | 28 | 19.4% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 217

| Race | Count | % |
|------|-------|---|
| Black | 153 | 70.5% |
| White | 64 | 29.5% |

### Natchitoches Parish
**Total:** 196

| Race | Count | % |
|------|-------|---|
| Black | 146 | 74.5% |
| White | 46 | 23.5% |
| Unknown | 4 | 2.0% |

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
**Total:** 1,315

| Race | Count | % |
|------|-------|---|
| Black | 878 | 66.8% |
| White | 423 | 32.2% |
| Unknown | 14 | 1.1% |

### Plaquemines Parish
**Total:** 668

| Race | Count | % |
|------|-------|---|
| Black | 441 | 66.0% |
| White | 205 | 30.7% |
| Unknown | 12 | 1.8% |
| Asian/PacificIslander | 6 | 0.9% |
| American Indian/Alaska Native | 4 | 0.6% |

### Pointe Coupee Parish
**Total:** 106

| Race | Count | % |
|------|-------|---|
| Black | 66 | 62.3% |
| White | 37 | 34.9% |
| Unknown | 2 | 1.9% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,043

| Race | Count | % |
|------|-------|---|
| Black | 661 | 63.4% |
| White | 364 | 34.9% |
| Unknown | 16 | 1.5% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| Black | 24 | 55.8% |
| White | 18 | 41.9% |
| Asian/PacificIslander | 1 | 2.3% |

### Richland Parish
**Total:** 722

| Race | Count | % |
|------|-------|---|
| Black | 498 | 69.0% |
| White | 214 | 29.6% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 191

| Race | Count | % |
|------|-------|---|
| White | 104 | 54.5% |
| Black | 84 | 44.0% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 70

| Race | Count | % |
|------|-------|---|
| Black | 55 | 78.6% |
| White | 15 | 21.4% |

### St. Bernard Parish
**Total:** 225

| Race | Count | % |
|------|-------|---|
| Black | 135 | 60.0% |
| White | 86 | 38.2% |
| Asian/PacificIslander | 3 | 1.3% |
| Unknown | 1 | 0.4% |

### St. Charles Parish
**Total:** 177

| Race | Count | % |
|------|-------|---|
| Unknown | 109 | 61.6% |
| White | 68 | 38.4% |

### St. Helena Parish
**Total:** 49

| Race | Count | % |
|------|-------|---|
| Black | 34 | 69.4% |
| White | 14 | 28.6% |
| Unknown | 1 | 2.0% |

### St. James Parish
**Total:** 68

| Race | Count | % |
|------|-------|---|
| Black | 57 | 83.8% |
| White | 11 | 16.2% |

### St. John the Baptist Parish
**Total:** 205

| Race | Count | % |
|------|-------|---|
| Unknown | 130 | 63.4% |
| White | 75 | 36.6% |

### St. Landry Parish
**Total:** 114

| Race | Count | % |
|------|-------|---|
| Black | 73 | 64.0% |
| White | 39 | 34.2% |
| Unknown | 2 | 1.8% |

### St. Martin Parish
**Total:** 214

| Race | Count | % |
|------|-------|---|
| Black | 109 | 50.9% |
| White | 95 | 44.4% |
| Unknown | 9 | 4.2% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 278

| Race | Count | % |
|------|-------|---|
| Black | 148 | 53.2% |
| White | 129 | 46.4% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 869

| Race | Count | % |
|------|-------|---|
| White | 453 | 52.1% |
| Black | 373 | 42.9% |
| Unknown | 40 | 4.6% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sulphur Police Department
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 15 | 88.2% |
| Black | 2 | 11.8% |

### Tangipahoa Parish
**Total:** 662

| Race | Count | % |
|------|-------|---|
| Black | 413 | 62.4% |
| White | 247 | 37.3% |
| Unknown | 2 | 0.3% |

### Tensas Parish
**Total:** 559

| Race | Count | % |
|------|-------|---|
| Black | 372 | 66.5% |
| White | 177 | 31.7% |
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
**Total:** 129

| Race | Count | % |
|------|-------|---|
| White | 64 | 49.6% |
| Black | 61 | 47.3% |
| Unknown | 3 | 2.3% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 165

| Race | Count | % |
|------|-------|---|
| White | 113 | 68.5% |
| Black | 49 | 29.7% |
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
**Total:** 181

| Race | Count | % |
|------|-------|---|
| Black | 91 | 50.3% |
| White | 90 | 49.7% |

### Webster Parish
**Total:** 443

| Race | Count | % |
|------|-------|---|
| Black | 237 | 53.5% |
| White | 200 | 45.1% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.5% |

### West Baton Rouge Parish
**Total:** 119

| Race | Count | % |
|------|-------|---|
| Black | 82 | 68.9% |
| White | 33 | 27.7% |
| Unknown | 3 | 2.5% |
| Asian/PacificIslander | 1 | 0.8% |

### West Carroll Parish
**Total:** 31

| Race | Count | % |
|------|-------|---|
| White | 24 | 77.4% |
| Black | 7 | 22.6% |

### West Felician Parish
**Total:** 192

| Race | Count | % |
|------|-------|---|
| Black | 127 | 66.1% |
| White | 65 | 33.9% |

### Winn Parish
**Total:** 143

| Race | Count | % |
|------|-------|---|
| Black | 74 | 51.7% |
| White | 69 | 48.3% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
