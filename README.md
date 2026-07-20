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

_Last updated: 2026-07-20 02:35 UTC_

**Total inmates (latest scrape):** 26,978 across 72 parishes/jails

### Acadia Parish
**Total:** 167

| Race | Count | % |
|------|-------|---|
| White | 93 | 55.7% |
| Black | 73 | 43.7% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 123

| Race | Count | % |
|------|-------|---|
| White | 79 | 64.2% |
| Black | 41 | 33.3% |
| Unknown | 2 | 1.6% |
| American Indian/Alaska Native | 1 | 0.8% |

### Ascension Parish
**Total:** 511

| Race | Count | % |
|------|-------|---|
| Black | 272 | 53.2% |
| White | 203 | 39.7% |
| Unknown | 32 | 6.3% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 164

| Race | Count | % |
|------|-------|---|
| Unknown | 90 | 54.9% |
| White | 74 | 45.1% |

### Avoyelles Parish
**Total:** 348

| Race | Count | % |
|------|-------|---|
| Black | 194 | 55.7% |
| White | 150 | 43.1% |
| Unknown | 3 | 0.9% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 165

| Race | Count | % |
|------|-------|---|
| White | 114 | 69.1% |
| Black | 51 | 30.9% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 34

| Race | Count | % |
|------|-------|---|
| White | 20 | 58.8% |
| Black | 14 | 41.2% |

### Bossier City Police Department
**Total:** 45

| Race | Count | % |
|------|-------|---|
| Black | 23 | 51.1% |
| White | 22 | 48.9% |

### Bossier Parish
**Total:** 1,118

| Race | Count | % |
|------|-------|---|
| Black | 628 | 56.2% |
| White | 489 | 43.7% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,726

| Race | Count | % |
|------|-------|---|
| Black | 1,301 | 75.4% |
| White | 398 | 23.1% |
| Unknown | 26 | 1.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Calcasieu Parish
**Total:** 1,105

| Race | Count | % |
|------|-------|---|
| Black | 618 | 55.9% |
| White | 442 | 40.0% |
| Unknown | 43 | 3.9% |
| Asian/PacificIslander | 2 | 0.2% |

### Caldwell Parish
**Total:** 611

| Race | Count | % |
|------|-------|---|
| Black | 384 | 62.8% |
| White | 212 | 34.7% |
| American Indian/Alaska Native | 15 | 2.5% |

### Cameron Parish
**Total:** 19

| Race | Count | % |
|------|-------|---|
| White | 19 | 100.0% |

### Catahoula Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 92 | 70.8% |
| White | 37 | 28.5% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 651

| Race | Count | % |
|------|-------|---|
| Black | 403 | 61.9% |
| White | 248 | 38.1% |

### Concordia Parish
**Total:** 825

| Race | Count | % |
|------|-------|---|
| White | 462 | 56.0% |
| Black | 363 | 44.0% |

### DeSoto Parish
**Total:** 118

| Race | Count | % |
|------|-------|---|
| Black | 73 | 61.9% |
| White | 44 | 37.3% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,345

| Race | Count | % |
|------|-------|---|
| Black | 1,058 | 78.7% |
| White | 221 | 16.4% |
| Unknown | 62 | 4.6% |
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
**Total:** 155

| Race | Count | % |
|------|-------|---|
| Black | 89 | 57.4% |
| White | 65 | 41.9% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 838

| Race | Count | % |
|------|-------|---|
| Black | 551 | 65.8% |
| White | 281 | 33.5% |
| Unknown | 6 | 0.7% |

### Hammond Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 15 | 65.2% |
| White | 7 | 30.4% |
| Unknown | 1 | 4.3% |

### Iberia Parish
**Total:** 469

| Race | Count | % |
|------|-------|---|
| Black | 280 | 59.7% |
| White | 179 | 38.2% |
| Asian/PacificIslander | 5 | 1.1% |
| Unknown | 4 | 0.9% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 39

| Race | Count | % |
|------|-------|---|
| Black | 22 | 56.4% |
| White | 17 | 43.6% |

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
| Black | 75 | 45.7% |
| American Indian/Alaska Native | 2 | 1.2% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,200

| Race | Count | % |
|------|-------|---|
| Black | 761 | 63.4% |
| White | 433 | 36.1% |
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
**Total:** 828

| Race | Count | % |
|------|-------|---|
| Black | 552 | 66.7% |
| White | 264 | 31.9% |
| Unknown | 12 | 1.4% |

### Lafourche Parish
**Total:** 752

| Race | Count | % |
|------|-------|---|
| Black | 391 | 52.0% |
| White | 357 | 47.5% |
| American Indian/Alaska Native | 3 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 369

| Race | Count | % |
|------|-------|---|
| Black | 274 | 74.3% |
| White | 92 | 24.9% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 838

| Race | Count | % |
|------|-------|---|
| White | 591 | 70.5% |
| Black | 236 | 28.2% |
| Unknown | 9 | 1.1% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 144

| Race | Count | % |
|------|-------|---|
| Black | 116 | 80.6% |
| White | 27 | 18.8% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 210

| Race | Count | % |
|------|-------|---|
| Black | 151 | 71.9% |
| White | 59 | 28.1% |

### Natchitoches Parish
**Total:** 188

| Race | Count | % |
|------|-------|---|
| Black | 138 | 73.4% |
| White | 46 | 24.5% |
| Unknown | 4 | 2.1% |

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
**Total:** 1,359

| Race | Count | % |
|------|-------|---|
| Black | 901 | 66.3% |
| White | 441 | 32.5% |
| Unknown | 17 | 1.3% |

### Plaquemines Parish
**Total:** 666

| Race | Count | % |
|------|-------|---|
| Black | 436 | 65.5% |
| White | 208 | 31.2% |
| Unknown | 13 | 2.0% |
| Asian/PacificIslander | 7 | 1.1% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| Black | 72 | 60.0% |
| White | 44 | 36.7% |
| Unknown | 3 | 2.5% |
| American Indian/Alaska Native | 1 | 0.8% |

### Rapides Parish
**Total:** 1,054

| Race | Count | % |
|------|-------|---|
| Black | 663 | 62.9% |
| White | 374 | 35.5% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 41

| Race | Count | % |
|------|-------|---|
| Black | 20 | 48.8% |
| White | 20 | 48.8% |
| Asian/PacificIslander | 1 | 2.4% |

### Richland Parish
**Total:** 678

| Race | Count | % |
|------|-------|---|
| Black | 469 | 69.2% |
| White | 200 | 29.5% |
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
**Total:** 41

| Race | Count | % |
|------|-------|---|
| Black | 31 | 75.6% |
| White | 10 | 24.4% |

### St. Bernard Parish
**Total:** 216

| Race | Count | % |
|------|-------|---|
| Black | 131 | 60.6% |
| White | 81 | 37.5% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 186

| Race | Count | % |
|------|-------|---|
| Unknown | 108 | 58.1% |
| White | 78 | 41.9% |

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
**Total:** 212

| Race | Count | % |
|------|-------|---|
| Unknown | 138 | 65.1% |
| White | 74 | 34.9% |

### St. Landry Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 89 | 68.5% |
| White | 39 | 30.0% |
| Unknown | 2 | 1.5% |

### St. Martin Parish
**Total:** 220

| Race | Count | % |
|------|-------|---|
| Black | 107 | 48.6% |
| White | 104 | 47.3% |
| Unknown | 8 | 3.6% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 286

| Race | Count | % |
|------|-------|---|
| Black | 151 | 52.8% |
| White | 134 | 46.9% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 887

| Race | Count | % |
|------|-------|---|
| White | 468 | 52.8% |
| Black | 376 | 42.4% |
| Unknown | 41 | 4.6% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 14

| Race | Count | % |
|------|-------|---|
| White | 11 | 78.6% |
| Black | 3 | 21.4% |

### Tangipahoa Parish
**Total:** 708

| Race | Count | % |
|------|-------|---|
| Black | 460 | 65.0% |
| White | 244 | 34.5% |
| Unknown | 4 | 0.6% |

### Tensas Parish
**Total:** 562

| Race | Count | % |
|------|-------|---|
| Black | 377 | 67.1% |
| White | 173 | 30.8% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 571

| Race | Count | % |
|------|-------|---|
| Black | 307 | 53.8% |
| White | 251 | 44.0% |
| American Indian/Alaska Native | 12 | 2.1% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 124

| Race | Count | % |
|------|-------|---|
| White | 60 | 48.4% |
| Black | 60 | 48.4% |
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
**Total:** 208

| Race | Count | % |
|------|-------|---|
| Black | 109 | 52.4% |
| White | 98 | 47.1% |
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
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 85 | 64.9% |
| White | 41 | 31.3% |
| Unknown | 3 | 2.3% |
| Asian/PacificIslander | 2 | 1.5% |

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
**Total:** 151

| Race | Count | % |
|------|-------|---|
| White | 76 | 50.3% |
| Black | 75 | 49.7% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
