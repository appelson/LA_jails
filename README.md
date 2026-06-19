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

_Last updated: 2026-06-19 03:54 UTC_

**Total inmates (latest scrape):** 26,537 across 72 parishes/jails

### Acadia Parish
**Total:** 181

| Race | Count | % |
|------|-------|---|
| White | 97 | 53.6% |
| Black | 82 | 45.3% |
| Asian/PacificIslander | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| White | 72 | 64.3% |
| Black | 37 | 33.0% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 518

| Race | Count | % |
|------|-------|---|
| Black | 277 | 53.5% |
| White | 205 | 39.6% |
| Unknown | 32 | 6.2% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 155

| Race | Count | % |
|------|-------|---|
| Unknown | 84 | 54.2% |
| White | 71 | 45.8% |

### Avoyelles Parish
**Total:** 354

| Race | Count | % |
|------|-------|---|
| Black | 197 | 55.6% |
| White | 153 | 43.2% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| White | 106 | 70.2% |
| Black | 45 | 29.8% |

### Bienville Parish
**Total:** 36

| Race | Count | % |
|------|-------|---|
| White | 23 | 63.9% |
| Unknown | 13 | 36.1% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 46

| Race | Count | % |
|------|-------|---|
| Black | 34 | 73.9% |
| White | 11 | 23.9% |
| Asian/PacificIslander | 1 | 2.2% |

### Bossier Parish
**Total:** 1,093

| Race | Count | % |
|------|-------|---|
| Black | 595 | 54.4% |
| White | 497 | 45.5% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,681

| Race | Count | % |
|------|-------|---|
| Black | 1,264 | 75.2% |
| White | 389 | 23.1% |
| Unknown | 26 | 1.5% |
| Asian/PacificIslander | 2 | 0.1% |

### Calcasieu Parish
**Total:** 1,084

| Race | Count | % |
|------|-------|---|
| Black | 602 | 55.5% |
| White | 439 | 40.5% |
| Unknown | 40 | 3.7% |
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
**Total:** 29

| Race | Count | % |
|------|-------|---|
| White | 26 | 89.7% |
| Black | 3 | 10.3% |

### Catahoula Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| Black | 91 | 70.5% |
| White | 37 | 28.7% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 665

| Race | Count | % |
|------|-------|---|
| Black | 412 | 62.0% |
| White | 253 | 38.0% |

### Concordia Parish
**Total:** 799

| Race | Count | % |
|------|-------|---|
| White | 454 | 56.8% |
| Black | 343 | 42.9% |
| Unknown | 2 | 0.3% |

### DeSoto Parish
**Total:** 124

| Race | Count | % |
|------|-------|---|
| Black | 73 | 58.9% |
| White | 50 | 40.3% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,335

| Race | Count | % |
|------|-------|---|
| Black | 1,059 | 79.3% |
| White | 210 | 15.7% |
| Unknown | 63 | 4.7% |
| Asian/PacificIslander | 3 | 0.2% |

### East Feliciana Parish
**Total:** 266

| Race | Count | % |
|------|-------|---|
| Black | 170 | 63.9% |
| White | 95 | 35.7% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 150

| Race | Count | % |
|------|-------|---|
| Black | 83 | 55.3% |
| White | 66 | 44.0% |
| Unknown | 1 | 0.7% |

### Franklin Parish
**Total:** 841

| Race | Count | % |
|------|-------|---|
| Black | 545 | 64.8% |
| White | 285 | 33.9% |
| Unknown | 11 | 1.3% |

### Hammond Police Department
**Total:** 11

| Race | Count | % |
|------|-------|---|
| Black | 7 | 63.6% |
| White | 3 | 27.3% |
| Unknown | 1 | 9.1% |

### Iberia Parish
**Total:** 454

| Race | Count | % |
|------|-------|---|
| Black | 263 | 57.9% |
| White | 180 | 39.6% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 97

| Race | Count | % |
|------|-------|---|
| Black | 64 | 66.0% |
| White | 32 | 33.0% |
| Unknown | 1 | 1.0% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 156

| Race | Count | % |
|------|-------|---|
| White | 81 | 51.9% |
| Black | 71 | 45.5% |
| American Indian/Alaska Native | 3 | 1.9% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,123

| Race | Count | % |
|------|-------|---|
| Black | 732 | 65.2% |
| White | 384 | 34.2% |
| Unknown | 6 | 0.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 69

| Race | Count | % |
|------|-------|---|
| White | 45 | 65.2% |
| Black | 23 | 33.3% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 848

| Race | Count | % |
|------|-------|---|
| Black | 552 | 65.1% |
| White | 280 | 33.0% |
| Unknown | 16 | 1.9% |

### Lafourche Parish
**Total:** 748

| Race | Count | % |
|------|-------|---|
| Black | 384 | 51.3% |
| White | 359 | 48.0% |
| American Indian/Alaska Native | 4 | 0.5% |
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
| Black | 282 | 76.0% |
| White | 86 | 23.2% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 807

| Race | Count | % |
|------|-------|---|
| White | 577 | 71.5% |
| Black | 219 | 27.1% |
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
**Total:** 214

| Race | Count | % |
|------|-------|---|
| Black | 151 | 70.6% |
| White | 63 | 29.4% |

### Natchitoches Parish
**Total:** 195

| Race | Count | % |
|------|-------|---|
| Black | 145 | 74.4% |
| White | 46 | 23.6% |
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
**Total:** 1,310

| Race | Count | % |
|------|-------|---|
| Black | 874 | 66.7% |
| White | 421 | 32.1% |
| Unknown | 15 | 1.1% |

### Plaquemines Parish
**Total:** 668

| Race | Count | % |
|------|-------|---|
| Black | 440 | 65.9% |
| White | 206 | 30.8% |
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
**Total:** 1,041

| Race | Count | % |
|------|-------|---|
| Black | 660 | 63.4% |
| White | 362 | 34.8% |
| Unknown | 17 | 1.6% |
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
**Total:** 192

| Race | Count | % |
|------|-------|---|
| White | 103 | 53.6% |
| Black | 86 | 44.8% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 62

| Race | Count | % |
|------|-------|---|
| Black | 47 | 75.8% |
| White | 15 | 24.2% |

### St. Bernard Parish
**Total:** 223

| Race | Count | % |
|------|-------|---|
| Black | 131 | 58.7% |
| White | 88 | 39.5% |
| Asian/PacificIslander | 3 | 1.3% |
| Unknown | 1 | 0.4% |

### St. Charles Parish
**Total:** 181

| Race | Count | % |
|------|-------|---|
| Unknown | 107 | 59.1% |
| White | 74 | 40.9% |

### St. Helena Parish
**Total:** 49

| Race | Count | % |
|------|-------|---|
| Black | 34 | 69.4% |
| White | 14 | 28.6% |
| Unknown | 1 | 2.0% |

### St. James Parish
**Total:** 67

| Race | Count | % |
|------|-------|---|
| Black | 56 | 83.6% |
| White | 11 | 16.4% |

### St. John the Baptist Parish
**Total:** 204

| Race | Count | % |
|------|-------|---|
| Unknown | 129 | 63.2% |
| White | 75 | 36.8% |

### St. Landry Parish
**Total:** 115

| Race | Count | % |
|------|-------|---|
| Black | 74 | 64.3% |
| White | 39 | 33.9% |
| Unknown | 2 | 1.7% |

### St. Martin Parish
**Total:** 213

| Race | Count | % |
|------|-------|---|
| Black | 108 | 50.7% |
| White | 95 | 44.6% |
| Unknown | 9 | 4.2% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 280

| Race | Count | % |
|------|-------|---|
| Black | 149 | 53.2% |
| White | 130 | 46.4% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 867

| Race | Count | % |
|------|-------|---|
| White | 453 | 52.2% |
| Black | 372 | 42.9% |
| Unknown | 39 | 4.5% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sulphur Police Department
**Total:** 18

| Race | Count | % |
|------|-------|---|
| White | 15 | 83.3% |
| Black | 3 | 16.7% |

### Tangipahoa Parish
**Total:** 656

| Race | Count | % |
|------|-------|---|
| Black | 411 | 62.7% |
| White | 243 | 37.0% |
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
**Total:** 127

| Race | Count | % |
|------|-------|---|
| White | 64 | 50.4% |
| Black | 59 | 46.5% |
| Unknown | 3 | 2.4% |
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
**Total:** 183

| Race | Count | % |
|------|-------|---|
| Black | 93 | 50.8% |
| White | 90 | 49.2% |

### Webster Parish
**Total:** 444

| Race | Count | % |
|------|-------|---|
| Black | 237 | 53.4% |
| White | 201 | 45.3% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.5% |

### West Baton Rouge Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| Black | 82 | 68.3% |
| White | 34 | 28.3% |
| Unknown | 3 | 2.5% |
| Asian/PacificIslander | 1 | 0.8% |

### West Carroll Parish
**Total:** 31

| Race | Count | % |
|------|-------|---|
| White | 24 | 77.4% |
| Black | 7 | 22.6% |

### West Felician Parish
**Total:** 188

| Race | Count | % |
|------|-------|---|
| Black | 124 | 66.0% |
| White | 64 | 34.0% |

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
