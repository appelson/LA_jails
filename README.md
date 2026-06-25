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

_Last updated: 2026-06-25 02:52 UTC_

**Total inmates (latest scrape):** 26,743 across 72 parishes/jails

### Acadia Parish
**Total:** 186

| Race | Count | % |
|------|-------|---|
| White | 99 | 53.2% |
| Black | 85 | 45.7% |
| Asian/PacificIslander | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Allen Parish
**Total:** 114

| Race | Count | % |
|------|-------|---|
| White | 72 | 63.2% |
| Black | 39 | 34.2% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 522

| Race | Count | % |
|------|-------|---|
| Black | 279 | 53.4% |
| White | 210 | 40.2% |
| Unknown | 29 | 5.6% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 150

| Race | Count | % |
|------|-------|---|
| Unknown | 82 | 54.7% |
| White | 68 | 45.3% |

### Avoyelles Parish
**Total:** 355

| Race | Count | % |
|------|-------|---|
| Black | 195 | 54.9% |
| White | 156 | 43.9% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 137

| Race | Count | % |
|------|-------|---|
| White | 95 | 69.3% |
| Black | 42 | 30.7% |

### Bienville Parish
**Total:** 41

| Race | Count | % |
|------|-------|---|
| White | 24 | 58.5% |
| Unknown | 17 | 41.5% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 43

| Race | Count | % |
|------|-------|---|
| Black | 30 | 69.8% |
| White | 12 | 27.9% |
| Asian/PacificIslander | 1 | 2.3% |

### Bossier Parish
**Total:** 1,113

| Race | Count | % |
|------|-------|---|
| Black | 611 | 54.9% |
| White | 501 | 45.0% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,691

| Race | Count | % |
|------|-------|---|
| Black | 1,278 | 75.6% |
| White | 385 | 22.8% |
| Unknown | 26 | 1.5% |
| Asian/PacificIslander | 2 | 0.1% |

### Calcasieu Parish
**Total:** 1,098

| Race | Count | % |
|------|-------|---|
| Black | 613 | 55.8% |
| White | 447 | 40.7% |
| Unknown | 35 | 3.2% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 625

| Race | Count | % |
|------|-------|---|
| Black | 394 | 63.0% |
| White | 210 | 33.6% |
| American Indian/Alaska Native | 20 | 3.2% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 21

| Race | Count | % |
|------|-------|---|
| White | 18 | 85.7% |
| Black | 3 | 14.3% |

### Catahoula Parish
**Total:** 134

| Race | Count | % |
|------|-------|---|
| Black | 92 | 68.7% |
| White | 41 | 30.6% |
| Unknown | 1 | 0.7% |

### Claiborne Parish
**Total:** 681

| Race | Count | % |
|------|-------|---|
| Black | 419 | 61.5% |
| White | 262 | 38.5% |

### Concordia Parish
**Total:** 815

| Race | Count | % |
|------|-------|---|
| White | 462 | 56.7% |
| Black | 351 | 43.1% |
| Unknown | 2 | 0.2% |

### DeSoto Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| Black | 71 | 59.2% |
| White | 48 | 40.0% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,331

| Race | Count | % |
|------|-------|---|
| Black | 1,059 | 79.6% |
| White | 202 | 15.2% |
| Unknown | 68 | 5.1% |
| Asian/PacificIslander | 2 | 0.2% |

### East Feliciana Parish
**Total:** 269

| Race | Count | % |
|------|-------|---|
| Black | 171 | 63.6% |
| White | 97 | 36.1% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 166

| Race | Count | % |
|------|-------|---|
| Black | 92 | 55.4% |
| White | 73 | 44.0% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 837

| Race | Count | % |
|------|-------|---|
| Black | 545 | 65.1% |
| White | 281 | 33.6% |
| Unknown | 11 | 1.3% |

### Hammond Police Department
**Total:** 9

| Race | Count | % |
|------|-------|---|
| Black | 6 | 66.7% |
| White | 3 | 33.3% |

### Iberia Parish
**Total:** 455

| Race | Count | % |
|------|-------|---|
| Black | 264 | 58.0% |
| White | 181 | 39.8% |
| Asian/PacificIslander | 5 | 1.1% |
| Unknown | 4 | 0.9% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 93

| Race | Count | % |
|------|-------|---|
| Black | 61 | 65.6% |
| White | 31 | 33.3% |
| Unknown | 1 | 1.1% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 164

| Race | Count | % |
|------|-------|---|
| White | 86 | 52.4% |
| Black | 74 | 45.1% |
| American Indian/Alaska Native | 3 | 1.8% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,165

| Race | Count | % |
|------|-------|---|
| Black | 767 | 65.8% |
| White | 391 | 33.6% |
| Unknown | 6 | 0.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 71

| Race | Count | % |
|------|-------|---|
| White | 47 | 66.2% |
| Black | 23 | 32.4% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 833

| Race | Count | % |
|------|-------|---|
| Black | 539 | 64.7% |
| White | 279 | 33.5% |
| Unknown | 14 | 1.7% |
| Asian/PacificIslander | 1 | 0.1% |

### Lafourche Parish
**Total:** 748

| Race | Count | % |
|------|-------|---|
| Black | 387 | 51.7% |
| White | 356 | 47.6% |
| American Indian/Alaska Native | 4 | 0.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 363

| Race | Count | % |
|------|-------|---|
| Black | 273 | 75.2% |
| White | 87 | 24.0% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 828

| Race | Count | % |
|------|-------|---|
| White | 592 | 71.5% |
| Black | 225 | 27.2% |
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
**Total:** 214

| Race | Count | % |
|------|-------|---|
| Black | 153 | 71.5% |
| White | 61 | 28.5% |

### Natchitoches Parish
**Total:** 197

| Race | Count | % |
|------|-------|---|
| Black | 145 | 73.6% |
| White | 47 | 23.9% |
| Unknown | 5 | 2.5% |

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
**Total:** 1,336

| Race | Count | % |
|------|-------|---|
| Black | 887 | 66.4% |
| White | 434 | 32.5% |
| Unknown | 15 | 1.1% |

### Plaquemines Parish
**Total:** 682

| Race | Count | % |
|------|-------|---|
| Black | 448 | 65.7% |
| White | 210 | 30.8% |
| Unknown | 13 | 1.9% |
| Asian/PacificIslander | 7 | 1.0% |
| American Indian/Alaska Native | 4 | 0.6% |

### Pointe Coupee Parish
**Total:** 106

| Race | Count | % |
|------|-------|---|
| Black | 65 | 61.3% |
| White | 38 | 35.8% |
| Unknown | 2 | 1.9% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,042

| Race | Count | % |
|------|-------|---|
| Black | 664 | 63.7% |
| White | 359 | 34.5% |
| Unknown | 17 | 1.6% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 45

| Race | Count | % |
|------|-------|---|
| Black | 25 | 55.6% |
| White | 19 | 42.2% |
| Asian/PacificIslander | 1 | 2.2% |

### Richland Parish
**Total:** 721

| Race | Count | % |
|------|-------|---|
| Black | 498 | 69.1% |
| White | 213 | 29.5% |
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
**Total:** 52

| Race | Count | % |
|------|-------|---|
| Black | 36 | 69.2% |
| White | 16 | 30.8% |

### St. Bernard Parish
**Total:** 225

| Race | Count | % |
|------|-------|---|
| Black | 131 | 58.2% |
| White | 91 | 40.4% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.4% |

### St. Charles Parish
**Total:** 190

| Race | Count | % |
|------|-------|---|
| Unknown | 115 | 60.5% |
| White | 75 | 39.5% |

### St. Helena Parish
**Total:** 51

| Race | Count | % |
|------|-------|---|
| Black | 36 | 70.6% |
| White | 14 | 27.5% |
| Unknown | 1 | 2.0% |

### St. James Parish
**Total:** 62

| Race | Count | % |
|------|-------|---|
| Black | 52 | 83.9% |
| White | 10 | 16.1% |

### St. John the Baptist Parish
**Total:** 197

| Race | Count | % |
|------|-------|---|
| Unknown | 127 | 64.5% |
| White | 70 | 35.5% |

### St. Landry Parish
**Total:** 127

| Race | Count | % |
|------|-------|---|
| Black | 83 | 65.4% |
| White | 42 | 33.1% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 213

| Race | Count | % |
|------|-------|---|
| Black | 109 | 51.2% |
| White | 94 | 44.1% |
| Unknown | 9 | 4.2% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 282

| Race | Count | % |
|------|-------|---|
| Black | 146 | 51.8% |
| White | 135 | 47.9% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 857

| Race | Count | % |
|------|-------|---|
| White | 457 | 53.3% |
| Black | 362 | 42.2% |
| Unknown | 35 | 4.1% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sulphur Police Department
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 15 | 88.2% |
| Black | 2 | 11.8% |

### Tangipahoa Parish
**Total:** 663

| Race | Count | % |
|------|-------|---|
| Black | 416 | 62.7% |
| White | 246 | 37.1% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 569

| Race | Count | % |
|------|-------|---|
| Black | 380 | 66.8% |
| White | 179 | 31.5% |
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
| White | 67 | 51.1% |
| Black | 61 | 46.6% |
| Unknown | 2 | 1.5% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 166

| Race | Count | % |
|------|-------|---|
| White | 114 | 68.7% |
| Black | 49 | 29.5% |
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
**Total:** 192

| Race | Count | % |
|------|-------|---|
| White | 97 | 50.5% |
| Black | 95 | 49.5% |

### Webster Parish
**Total:** 452

| Race | Count | % |
|------|-------|---|
| Black | 243 | 53.8% |
| White | 203 | 44.9% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 127

| Race | Count | % |
|------|-------|---|
| Black | 88 | 69.3% |
| White | 35 | 27.6% |
| Unknown | 3 | 2.4% |
| Asian/PacificIslander | 1 | 0.8% |

### West Carroll Parish
**Total:** 31

| Race | Count | % |
|------|-------|---|
| White | 25 | 80.6% |
| Black | 6 | 19.4% |

### West Felician Parish
**Total:** 190

| Race | Count | % |
|------|-------|---|
| Black | 124 | 65.3% |
| White | 66 | 34.7% |

### Winn Parish
**Total:** 142

| Race | Count | % |
|------|-------|---|
| Black | 74 | 52.1% |
| White | 68 | 47.9% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
