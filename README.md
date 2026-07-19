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

_Last updated: 2026-07-19 02:15 UTC_

**Total inmates (latest scrape):** 26,886 across 72 parishes/jails

### Acadia Parish
**Total:** 166

| Race | Count | % |
|------|-------|---|
| White | 92 | 55.4% |
| Black | 73 | 44.0% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 124

| Race | Count | % |
|------|-------|---|
| White | 80 | 64.5% |
| Black | 41 | 33.1% |
| Unknown | 2 | 1.6% |
| American Indian/Alaska Native | 1 | 0.8% |

### Ascension Parish
**Total:** 506

| Race | Count | % |
|------|-------|---|
| Black | 269 | 53.2% |
| White | 201 | 39.7% |
| Unknown | 32 | 6.3% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 163

| Race | Count | % |
|------|-------|---|
| Unknown | 90 | 55.2% |
| White | 73 | 44.8% |

### Avoyelles Parish
**Total:** 347

| Race | Count | % |
|------|-------|---|
| Black | 193 | 55.6% |
| White | 150 | 43.2% |
| Unknown | 3 | 0.9% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 163

| Race | Count | % |
|------|-------|---|
| White | 112 | 68.7% |
| Black | 51 | 31.3% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 30

| Race | Count | % |
|------|-------|---|
| White | 16 | 53.3% |
| Black | 14 | 46.7% |

### Bossier City Police Department
**Total:** 52

| Race | Count | % |
|------|-------|---|
| Black | 29 | 55.8% |
| White | 23 | 44.2% |

### Bossier Parish
**Total:** 1,120

| Race | Count | % |
|------|-------|---|
| Black | 627 | 56.0% |
| White | 492 | 43.9% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,720

| Race | Count | % |
|------|-------|---|
| Black | 1,297 | 75.4% |
| White | 397 | 23.1% |
| Unknown | 25 | 1.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Calcasieu Parish
**Total:** 1,102

| Race | Count | % |
|------|-------|---|
| Black | 616 | 55.9% |
| White | 442 | 40.1% |
| Unknown | 42 | 3.8% |
| Asian/PacificIslander | 2 | 0.2% |

### Caldwell Parish
**Total:** 613

| Race | Count | % |
|------|-------|---|
| Black | 384 | 62.6% |
| White | 213 | 34.7% |
| American Indian/Alaska Native | 16 | 2.6% |

### Cameron Parish
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 17 | 100.0% |

### Catahoula Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 92 | 70.8% |
| White | 37 | 28.5% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 656

| Race | Count | % |
|------|-------|---|
| Black | 405 | 61.7% |
| White | 251 | 38.3% |

### Concordia Parish
**Total:** 824

| Race | Count | % |
|------|-------|---|
| White | 462 | 56.1% |
| Black | 362 | 43.9% |

### DeSoto Parish
**Total:** 118

| Race | Count | % |
|------|-------|---|
| Black | 73 | 61.9% |
| White | 44 | 37.3% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,339

| Race | Count | % |
|------|-------|---|
| Black | 1,056 | 78.9% |
| White | 219 | 16.4% |
| Unknown | 61 | 4.6% |
| Asian/PacificIslander | 2 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### East Feliciana Parish
**Total:** 270

| Race | Count | % |
|------|-------|---|
| Black | 174 | 64.4% |
| White | 94 | 34.8% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 154

| Race | Count | % |
|------|-------|---|
| Black | 89 | 57.8% |
| White | 64 | 41.6% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 837

| Race | Count | % |
|------|-------|---|
| Black | 552 | 65.9% |
| White | 279 | 33.3% |
| Unknown | 6 | 0.7% |

### Hammond Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 15 | 65.2% |
| White | 8 | 34.8% |

### Iberia Parish
**Total:** 466

| Race | Count | % |
|------|-------|---|
| Black | 277 | 59.4% |
| White | 179 | 38.4% |
| Asian/PacificIslander | 5 | 1.1% |
| Unknown | 4 | 0.9% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 37

| Race | Count | % |
|------|-------|---|
| Black | 21 | 56.8% |
| White | 16 | 43.2% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 165

| Race | Count | % |
|------|-------|---|
| White | 87 | 52.7% |
| Black | 75 | 45.5% |
| American Indian/Alaska Native | 2 | 1.2% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,188

| Race | Count | % |
|------|-------|---|
| Black | 755 | 63.6% |
| White | 427 | 35.9% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 77

| Race | Count | % |
|------|-------|---|
| White | 52 | 67.5% |
| Black | 24 | 31.2% |
| Unknown | 1 | 1.3% |

### Lafayette Parish
**Total:** 822

| Race | Count | % |
|------|-------|---|
| Black | 549 | 66.8% |
| White | 260 | 31.6% |
| Unknown | 13 | 1.6% |

### Lafourche Parish
**Total:** 755

| Race | Count | % |
|------|-------|---|
| Black | 391 | 51.8% |
| White | 360 | 47.7% |
| American Indian/Alaska Native | 3 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 368

| Race | Count | % |
|------|-------|---|
| Black | 274 | 74.5% |
| White | 91 | 24.7% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 837

| Race | Count | % |
|------|-------|---|
| White | 590 | 70.5% |
| Black | 236 | 28.2% |
| Unknown | 9 | 1.1% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 145

| Race | Count | % |
|------|-------|---|
| Black | 117 | 80.7% |
| White | 27 | 18.6% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 211

| Race | Count | % |
|------|-------|---|
| Black | 151 | 71.6% |
| White | 60 | 28.4% |

### Natchitoches Parish
**Total:** 182

| Race | Count | % |
|------|-------|---|
| Black | 136 | 74.7% |
| White | 42 | 23.1% |
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
**Total:** 1,353

| Race | Count | % |
|------|-------|---|
| Black | 900 | 66.5% |
| White | 436 | 32.2% |
| Unknown | 17 | 1.3% |

### Plaquemines Parish
**Total:** 667

| Race | Count | % |
|------|-------|---|
| Black | 435 | 65.2% |
| White | 210 | 31.5% |
| Unknown | 13 | 1.9% |
| Asian/PacificIslander | 7 | 1.0% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 121

| Race | Count | % |
|------|-------|---|
| Black | 72 | 59.5% |
| White | 43 | 35.5% |
| American Indian/Alaska Native | 4 | 3.3% |
| Unknown | 2 | 1.7% |

### Rapides Parish
**Total:** 1,041

| Race | Count | % |
|------|-------|---|
| Black | 654 | 62.8% |
| White | 370 | 35.5% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 39

| Race | Count | % |
|------|-------|---|
| Black | 20 | 51.3% |
| White | 18 | 46.2% |
| Asian/PacificIslander | 1 | 2.6% |

### Richland Parish
**Total:** 676

| Race | Count | % |
|------|-------|---|
| Black | 469 | 69.4% |
| White | 198 | 29.3% |
| Unknown | 6 | 0.9% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 195

| Race | Count | % |
|------|-------|---|
| White | 109 | 55.9% |
| Black | 83 | 42.6% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 35 | 79.5% |
| White | 9 | 20.5% |

### St. Bernard Parish
**Total:** 216

| Race | Count | % |
|------|-------|---|
| Black | 131 | 60.6% |
| White | 81 | 37.5% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 183

| Race | Count | % |
|------|-------|---|
| Unknown | 105 | 57.4% |
| White | 78 | 42.6% |

### St. Helena Parish
**Total:** 54

| Race | Count | % |
|------|-------|---|
| Black | 35 | 64.8% |
| White | 17 | 31.5% |
| Unknown | 2 | 3.7% |

### St. James Parish
**Total:** 74

| Race | Count | % |
|------|-------|---|
| Black | 62 | 83.8% |
| White | 12 | 16.2% |

### St. John the Baptist Parish
**Total:** 208

| Race | Count | % |
|------|-------|---|
| Unknown | 135 | 64.9% |
| White | 73 | 35.1% |

### St. Landry Parish
**Total:** 127

| Race | Count | % |
|------|-------|---|
| Black | 87 | 68.5% |
| White | 38 | 29.9% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 219

| Race | Count | % |
|------|-------|---|
| Black | 107 | 48.9% |
| White | 103 | 47.0% |
| Unknown | 8 | 3.7% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 288

| Race | Count | % |
|------|-------|---|
| Black | 151 | 52.4% |
| White | 136 | 47.2% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 881

| Race | Count | % |
|------|-------|---|
| White | 463 | 52.6% |
| Black | 375 | 42.6% |
| Unknown | 41 | 4.7% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 14

| Race | Count | % |
|------|-------|---|
| White | 12 | 85.7% |
| Black | 2 | 14.3% |

### Tangipahoa Parish
**Total:** 700

| Race | Count | % |
|------|-------|---|
| Black | 454 | 64.9% |
| White | 243 | 34.7% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 562

| Race | Count | % |
|------|-------|---|
| Black | 377 | 67.1% |
| White | 173 | 30.8% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 566

| Race | Count | % |
|------|-------|---|
| Black | 305 | 53.9% |
| White | 248 | 43.8% |
| American Indian/Alaska Native | 12 | 2.1% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 127

| Race | Count | % |
|------|-------|---|
| White | 63 | 49.6% |
| Black | 60 | 47.2% |
| Unknown | 3 | 2.4% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 162

| Race | Count | % |
|------|-------|---|
| White | 110 | 67.9% |
| Black | 50 | 30.9% |
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
**Total:** 202

| Race | Count | % |
|------|-------|---|
| Black | 104 | 51.5% |
| White | 97 | 48.0% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 470

| Race | Count | % |
|------|-------|---|
| Black | 249 | 53.0% |
| White | 214 | 45.5% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| Black | 84 | 65.1% |
| White | 41 | 31.8% |
| Unknown | 2 | 1.6% |
| Asian/PacificIslander | 2 | 1.6% |

### West Carroll Parish
**Total:** 29

| Race | Count | % |
|------|-------|---|
| White | 23 | 79.3% |
| Black | 6 | 20.7% |

### West Felician Parish
**Total:** 195

| Race | Count | % |
|------|-------|---|
| Black | 126 | 64.6% |
| White | 69 | 35.4% |

### Winn Parish
**Total:** 152

| Race | Count | % |
|------|-------|---|
| White | 77 | 50.7% |
| Black | 75 | 49.3% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
