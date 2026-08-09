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

_Last updated: 2026-08-09 01:22 UTC_

**Total inmates (latest scrape):** 27,014 across 72 parishes/jails

### Acadia Parish
**Total:** 158

| Race | Count | % |
|------|-------|---|
| White | 86 | 54.4% |
| Black | 70 | 44.3% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 117

| Race | Count | % |
|------|-------|---|
| White | 72 | 61.5% |
| Black | 41 | 35.0% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 2 | 1.7% |

### Ascension Parish
**Total:** 524

| Race | Count | % |
|------|-------|---|
| Black | 278 | 53.1% |
| White | 210 | 40.1% |
| Unknown | 31 | 5.9% |
| Asian/PacificIslander | 5 | 1.0% |

### Assumption Parish
**Total:** 163

| Race | Count | % |
|------|-------|---|
| Unknown | 95 | 58.3% |
| White | 68 | 41.7% |

### Avoyelles Parish
**Total:** 349

| Race | Count | % |
|------|-------|---|
| Black | 195 | 55.9% |
| White | 151 | 43.3% |
| Unknown | 3 | 0.9% |

### Beauregard Parish
**Total:** 182

| Race | Count | % |
|------|-------|---|
| White | 116 | 63.7% |
| Black | 66 | 36.3% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 19

| Race | Count | % |
|------|-------|---|
| White | 11 | 57.9% |
| Black | 8 | 42.1% |

### Bossier City Police Department
**Total:** 63

| Race | Count | % |
|------|-------|---|
| Black | 39 | 61.9% |
| White | 24 | 38.1% |

### Bossier Parish
**Total:** 1,125

| Race | Count | % |
|------|-------|---|
| Black | 631 | 56.1% |
| White | 491 | 43.6% |
| American Indian/Alaska Native | 2 | 0.2% |
| Asian/PacificIslander | 1 | 0.1% |

### Caddo Parish
**Total:** 1,719

| Race | Count | % |
|------|-------|---|
| Black | 1,305 | 75.9% |
| White | 385 | 22.4% |
| Unknown | 29 | 1.7% |

### Calcasieu Parish
**Total:** 1,099

| Race | Count | % |
|------|-------|---|
| Black | 597 | 54.3% |
| White | 458 | 41.7% |
| Unknown | 43 | 3.9% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 603

| Race | Count | % |
|------|-------|---|
| Black | 386 | 64.0% |
| White | 201 | 33.3% |
| American Indian/Alaska Native | 15 | 2.5% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 26

| Race | Count | % |
|------|-------|---|
| White | 24 | 92.3% |
| Black | 1 | 3.8% |
| Unknown | 1 | 3.8% |

### Catahoula Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 91 | 69.5% |
| White | 38 | 29.0% |
| Unknown | 2 | 1.5% |

### Claiborne Parish
**Total:** 656

| Race | Count | % |
|------|-------|---|
| Black | 408 | 62.2% |
| White | 248 | 37.8% |

### Concordia Parish
**Total:** 816

| Race | Count | % |
|------|-------|---|
| White | 464 | 56.9% |
| Black | 352 | 43.1% |

### DeSoto Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 76 | 58.0% |
| White | 55 | 42.0% |

### East Baton Rouge Parish
**Total:** 1,286

| Race | Count | % |
|------|-------|---|
| Black | 996 | 77.4% |
| White | 230 | 17.9% |
| Unknown | 56 | 4.4% |
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
**Total:** 159

| Race | Count | % |
|------|-------|---|
| Black | 95 | 59.7% |
| White | 63 | 39.6% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 848

| Race | Count | % |
|------|-------|---|
| Black | 561 | 66.2% |
| White | 282 | 33.3% |
| Unknown | 4 | 0.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 9 | 52.9% |
| Black | 8 | 47.1% |

### Iberia Parish
**Total:** 475

| Race | Count | % |
|------|-------|---|
| Black | 283 | 59.6% |
| White | 180 | 37.9% |
| Unknown | 6 | 1.3% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 54

| Race | Count | % |
|------|-------|---|
| Black | 34 | 63.0% |
| White | 20 | 37.0% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 162

| Race | Count | % |
|------|-------|---|
| White | 83 | 51.2% |
| Black | 77 | 47.5% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,209

| Race | Count | % |
|------|-------|---|
| Black | 795 | 65.8% |
| White | 407 | 33.7% |
| Unknown | 7 | 0.6% |

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
| Black | 28 | 35.9% |
| Unknown | 2 | 2.6% |

### Lafayette Parish
**Total:** 827

| Race | Count | % |
|------|-------|---|
| Black | 548 | 66.3% |
| White | 269 | 32.5% |
| Unknown | 10 | 1.2% |

### Lafourche Parish
**Total:** 783

| Race | Count | % |
|------|-------|---|
| Black | 394 | 50.3% |
| White | 385 | 49.2% |
| American Indian/Alaska Native | 3 | 0.4% |
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
| Black | 270 | 73.8% |
| White | 90 | 24.6% |
| Unknown | 5 | 1.4% |
| Asian/PacificIslander | 1 | 0.3% |

### Livingston Parish
**Total:** 825

| Race | Count | % |
|------|-------|---|
| White | 585 | 70.9% |
| Black | 231 | 28.0% |
| Unknown | 6 | 0.7% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 145

| Race | Count | % |
|------|-------|---|
| Black | 118 | 81.4% |
| White | 26 | 17.9% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 201

| Race | Count | % |
|------|-------|---|
| Black | 147 | 73.1% |
| White | 53 | 26.4% |
| Unknown | 1 | 0.5% |

### Natchitoches Parish
**Total:** 186

| Race | Count | % |
|------|-------|---|
| Black | 143 | 76.9% |
| White | 39 | 21.0% |
| Unknown | 4 | 2.2% |

### Oakdale Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### Opelousas Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| African American | 1 | 100.0% |

### Orleans Parish
**Total:** 1,438

| Race | Count | % |
|------|-------|---|
| Black | 1,238 | 86.1% |
| White | 182 | 12.7% |
| Unknown | 14 | 1.0% |
| Asian/PacificIslander | 4 | 0.3% |

### Ouachita Parish
**Total:** 1,336

| Race | Count | % |
|------|-------|---|
| Black | 899 | 67.3% |
| White | 426 | 31.9% |
| Unknown | 11 | 0.8% |

### Plaquemines Parish
**Total:** 662

| Race | Count | % |
|------|-------|---|
| Black | 429 | 64.8% |
| White | 210 | 31.7% |
| Unknown | 12 | 1.8% |
| Asian/PacificIslander | 9 | 1.4% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 83 | 63.8% |
| White | 44 | 33.8% |
| Unknown | 2 | 1.5% |
| American Indian/Alaska Native | 1 | 0.8% |

### Rapides Parish
**Total:** 1,054

| Race | Count | % |
|------|-------|---|
| Black | 674 | 63.9% |
| White | 364 | 34.5% |
| Unknown | 14 | 1.3% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| Black | 23 | 53.5% |
| White | 19 | 44.2% |
| Asian/PacificIslander | 1 | 2.3% |

### Richland Parish
**Total:** 701

| Race | Count | % |
|------|-------|---|
| Black | 486 | 69.3% |
| White | 207 | 29.5% |
| Unknown | 5 | 0.7% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 187

| Race | Count | % |
|------|-------|---|
| White | 110 | 58.8% |
| Black | 75 | 40.1% |
| Unknown | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 30

| Race | Count | % |
|------|-------|---|
| Black | 23 | 76.7% |
| White | 7 | 23.3% |

### St. Bernard Parish
**Total:** 226

| Race | Count | % |
|------|-------|---|
| Black | 129 | 57.1% |
| White | 93 | 41.2% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 173

| Race | Count | % |
|------|-------|---|
| Unknown | 101 | 58.4% |
| White | 72 | 41.6% |

### St. Helena Parish
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 34 | 77.3% |
| White | 10 | 22.7% |

### St. James Parish
**Total:** 78

| Race | Count | % |
|------|-------|---|
| Black | 65 | 83.3% |
| White | 13 | 16.7% |

### St. John the Baptist Parish
**Total:** 226

| Race | Count | % |
|------|-------|---|
| Unknown | 149 | 65.9% |
| White | 77 | 34.1% |

### St. Landry Parish
**Total:** 136

| Race | Count | % |
|------|-------|---|
| Black | 91 | 66.9% |
| White | 43 | 31.6% |
| Unknown | 2 | 1.5% |

### St. Martin Parish
**Total:** 217

| Race | Count | % |
|------|-------|---|
| Black | 108 | 49.8% |
| White | 100 | 46.1% |
| Unknown | 9 | 4.1% |

### St. Mary Parish
**Total:** 287

| Race | Count | % |
|------|-------|---|
| White | 143 | 49.8% |
| Black | 143 | 49.8% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 888

| Race | Count | % |
|------|-------|---|
| White | 453 | 51.0% |
| Black | 392 | 44.1% |
| Unknown | 41 | 4.6% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 15 | 88.2% |
| Black | 2 | 11.8% |

### Tangipahoa Parish
**Total:** 708

| Race | Count | % |
|------|-------|---|
| Black | 465 | 65.7% |
| White | 240 | 33.9% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 564

| Race | Count | % |
|------|-------|---|
| Black | 381 | 67.6% |
| White | 171 | 30.3% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 579

| Race | Count | % |
|------|-------|---|
| Black | 332 | 57.3% |
| White | 233 | 40.2% |
| American Indian/Alaska Native | 13 | 2.2% |
| Asian/PacificIslander | 1 | 0.2% |

### Vermillion Parish
**Total:** 118

| Race | Count | % |
|------|-------|---|
| White | 58 | 49.2% |
| Black | 57 | 48.3% |
| Unknown | 2 | 1.7% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 176

| Race | Count | % |
|------|-------|---|
| White | 124 | 70.5% |
| Black | 50 | 28.4% |
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
**Total:** 188

| Race | Count | % |
|------|-------|---|
| Black | 96 | 51.1% |
| White | 91 | 48.4% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 444

| Race | Count | % |
|------|-------|---|
| Black | 231 | 52.0% |
| White | 206 | 46.4% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 2 | 0.5% |

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
**Total:** 202

| Race | Count | % |
|------|-------|---|
| Black | 128 | 63.4% |
| White | 74 | 36.6% |

### Winn Parish
**Total:** 146

| Race | Count | % |
|------|-------|---|
| Black | 74 | 50.7% |
| White | 72 | 49.3% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
