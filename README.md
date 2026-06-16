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

_Last updated: 2026-06-16 03:41 UTC_

**Total inmates (latest scrape):** 26,645 across 72 parishes/jails

### Acadia Parish
**Total:** 185

| Race | Count | % |
|------|-------|---|
| White | 100 | 54.1% |
| Black | 83 | 44.9% |
| Asian/PacificIslander | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Allen Parish
**Total:** 116

| Race | Count | % |
|------|-------|---|
| White | 74 | 63.8% |
| Black | 40 | 34.5% |
| Unknown | 1 | 0.9% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 543

| Race | Count | % |
|------|-------|---|
| Black | 288 | 53.0% |
| White | 217 | 40.0% |
| Unknown | 34 | 6.3% |
| Asian/PacificIslander | 4 | 0.7% |

### Assumption Parish
**Total:** 155

| Race | Count | % |
|------|-------|---|
| Unknown | 84 | 54.2% |
| White | 71 | 45.8% |

### Avoyelles Parish
**Total:** 360

| Race | Count | % |
|------|-------|---|
| Black | 204 | 56.7% |
| White | 152 | 42.2% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 162

| Race | Count | % |
|------|-------|---|
| White | 113 | 69.8% |
| Black | 49 | 30.2% |

### Bienville Parish
**Total:** 35

| Race | Count | % |
|------|-------|---|
| White | 22 | 62.9% |
| Unknown | 13 | 37.1% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 41

| Race | Count | % |
|------|-------|---|
| Black | 22 | 53.7% |
| White | 18 | 43.9% |
| Asian/PacificIslander | 1 | 2.4% |

### Bossier Parish
**Total:** 1,107

| Race | Count | % |
|------|-------|---|
| Black | 608 | 54.9% |
| White | 498 | 45.0% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,666

| Race | Count | % |
|------|-------|---|
| Black | 1,249 | 75.0% |
| White | 389 | 23.3% |
| Unknown | 26 | 1.6% |
| Asian/PacificIslander | 2 | 0.1% |

### Calcasieu Parish
**Total:** 1,085

| Race | Count | % |
|------|-------|---|
| Black | 603 | 55.6% |
| White | 441 | 40.6% |
| Unknown | 40 | 3.7% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 611

| Race | Count | % |
|------|-------|---|
| Black | 390 | 63.8% |
| White | 201 | 32.9% |
| American Indian/Alaska Native | 19 | 3.1% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 27

| Race | Count | % |
|------|-------|---|
| White | 24 | 88.9% |
| Black | 2 | 7.4% |
| Unknown | 1 | 3.7% |

### Catahoula Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 91 | 70.0% |
| White | 38 | 29.2% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 663

| Race | Count | % |
|------|-------|---|
| Black | 413 | 62.3% |
| White | 250 | 37.7% |

### Concordia Parish
**Total:** 801

| Race | Count | % |
|------|-------|---|
| White | 453 | 56.6% |
| Black | 346 | 43.2% |
| Unknown | 2 | 0.2% |

### DeSoto Parish
**Total:** 125

| Race | Count | % |
|------|-------|---|
| Black | 72 | 57.6% |
| White | 52 | 41.6% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,347

| Race | Count | % |
|------|-------|---|
| Black | 1,065 | 79.1% |
| White | 215 | 16.0% |
| Unknown | 65 | 4.8% |
| Asian/PacificIslander | 2 | 0.1% |

### East Feliciana Parish
**Total:** 266

| Race | Count | % |
|------|-------|---|
| Black | 169 | 63.5% |
| White | 96 | 36.1% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 152

| Race | Count | % |
|------|-------|---|
| Black | 80 | 52.6% |
| White | 70 | 46.1% |
| Unknown | 2 | 1.3% |

### Franklin Parish
**Total:** 827

| Race | Count | % |
|------|-------|---|
| Black | 535 | 64.7% |
| White | 281 | 34.0% |
| Unknown | 11 | 1.3% |

### Hammond Police Department
**Total:** 13

| Race | Count | % |
|------|-------|---|
| Black | 8 | 61.5% |
| White | 4 | 30.8% |
| Unknown | 1 | 7.7% |

### Iberia Parish
**Total:** 451

| Race | Count | % |
|------|-------|---|
| Black | 268 | 59.4% |
| White | 173 | 38.4% |
| Asian/PacificIslander | 5 | 1.1% |
| Unknown | 4 | 0.9% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 98

| Race | Count | % |
|------|-------|---|
| Black | 63 | 64.3% |
| White | 34 | 34.7% |
| Unknown | 1 | 1.0% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 154

| Race | Count | % |
|------|-------|---|
| White | 81 | 52.6% |
| Black | 69 | 44.8% |
| American Indian/Alaska Native | 3 | 1.9% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,154

| Race | Count | % |
|------|-------|---|
| Black | 757 | 65.6% |
| White | 391 | 33.9% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### LaSalle Parish
**Total:** 71

| Race | Count | % |
|------|-------|---|
| White | 45 | 63.4% |
| Black | 25 | 35.2% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 877

| Race | Count | % |
|------|-------|---|
| Black | 571 | 65.1% |
| White | 290 | 33.1% |
| Unknown | 16 | 1.8% |

### Lafourche Parish
**Total:** 748

| Race | Count | % |
|------|-------|---|
| Black | 384 | 51.3% |
| White | 358 | 47.9% |
| American Indian/Alaska Native | 4 | 0.5% |
| Unknown | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 375

| Race | Count | % |
|------|-------|---|
| Black | 287 | 76.5% |
| White | 85 | 22.7% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 797

| Race | Count | % |
|------|-------|---|
| White | 565 | 70.9% |
| Black | 221 | 27.7% |
| Unknown | 9 | 1.1% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 144

| Race | Count | % |
|------|-------|---|
| Black | 114 | 79.2% |
| White | 28 | 19.4% |
| Unknown | 2 | 1.4% |

### Morehouse Parish
**Total:** 202

| Race | Count | % |
|------|-------|---|
| Black | 138 | 68.3% |
| White | 64 | 31.7% |

### Natchitoches Parish
**Total:** 192

| Race | Count | % |
|------|-------|---|
| Black | 145 | 75.5% |
| White | 45 | 23.4% |
| Unknown | 2 | 1.0% |

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
**Total:** 1,320

| Race | Count | % |
|------|-------|---|
| Black | 881 | 66.7% |
| White | 425 | 32.2% |
| Unknown | 14 | 1.1% |

### Plaquemines Parish
**Total:** 650

| Race | Count | % |
|------|-------|---|
| Black | 431 | 66.3% |
| White | 198 | 30.5% |
| Unknown | 13 | 2.0% |
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
**Total:** 1,026

| Race | Count | % |
|------|-------|---|
| Black | 653 | 63.6% |
| White | 354 | 34.5% |
| Unknown | 17 | 1.7% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 47

| Race | Count | % |
|------|-------|---|
| Black | 27 | 57.4% |
| White | 19 | 40.4% |
| Asian/PacificIslander | 1 | 2.1% |

### Richland Parish
**Total:** 735

| Race | Count | % |
|------|-------|---|
| Black | 506 | 68.8% |
| White | 220 | 29.9% |
| Unknown | 6 | 0.8% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 195

| Race | Count | % |
|------|-------|---|
| White | 108 | 55.4% |
| Black | 84 | 43.1% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 56

| Race | Count | % |
|------|-------|---|
| Black | 40 | 71.4% |
| White | 15 | 26.8% |
| Unknown | 1 | 1.8% |

### St. Bernard Parish
**Total:** 224

| Race | Count | % |
|------|-------|---|
| Black | 133 | 59.4% |
| White | 87 | 38.8% |
| Asian/PacificIslander | 3 | 1.3% |
| Unknown | 1 | 0.4% |

### St. Charles Parish
**Total:** 188

| Race | Count | % |
|------|-------|---|
| Unknown | 113 | 60.1% |
| White | 75 | 39.9% |

### St. Helena Parish
**Total:** 48

| Race | Count | % |
|------|-------|---|
| Black | 33 | 68.8% |
| White | 14 | 29.2% |
| Unknown | 1 | 2.1% |

### St. James Parish
**Total:** 68

| Race | Count | % |
|------|-------|---|
| Black | 57 | 83.8% |
| White | 11 | 16.2% |

### St. John the Baptist Parish
**Total:** 204

| Race | Count | % |
|------|-------|---|
| Unknown | 131 | 64.2% |
| White | 73 | 35.8% |

### St. Landry Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| Black | 78 | 65.0% |
| White | 40 | 33.3% |
| Unknown | 2 | 1.7% |

### St. Martin Parish
**Total:** 210

| Race | Count | % |
|------|-------|---|
| Black | 108 | 51.4% |
| White | 92 | 43.8% |
| Unknown | 9 | 4.3% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 279

| Race | Count | % |
|------|-------|---|
| Black | 145 | 52.0% |
| White | 133 | 47.7% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 884

| Race | Count | % |
|------|-------|---|
| White | 462 | 52.3% |
| Black | 380 | 43.0% |
| Unknown | 39 | 4.4% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sulphur Police Department
**Total:** 18

| Race | Count | % |
|------|-------|---|
| White | 16 | 88.9% |
| Black | 2 | 11.1% |

### Tangipahoa Parish
**Total:** 658

| Race | Count | % |
|------|-------|---|
| Black | 412 | 62.6% |
| White | 245 | 37.2% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 568

| Race | Count | % |
|------|-------|---|
| Black | 375 | 66.0% |
| White | 181 | 31.9% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 506

| Race | Count | % |
|------|-------|---|
| Black | 271 | 53.6% |
| White | 225 | 44.5% |
| American Indian/Alaska Native | 9 | 1.8% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 133

| Race | Count | % |
|------|-------|---|
| White | 69 | 51.9% |
| Black | 60 | 45.1% |
| Unknown | 3 | 2.3% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 160

| Race | Count | % |
|------|-------|---|
| White | 109 | 68.1% |
| Black | 48 | 30.0% |
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
**Total:** 186

| Race | Count | % |
|------|-------|---|
| White | 94 | 50.5% |
| Black | 92 | 49.5% |

### Webster Parish
**Total:** 446

| Race | Count | % |
|------|-------|---|
| Black | 236 | 52.9% |
| White | 204 | 45.7% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 125

| Race | Count | % |
|------|-------|---|
| Black | 85 | 68.0% |
| White | 35 | 28.0% |
| Unknown | 4 | 3.2% |
| Asian/PacificIslander | 1 | 0.8% |

### West Carroll Parish
**Total:** 29

| Race | Count | % |
|------|-------|---|
| White | 24 | 82.8% |
| Black | 5 | 17.2% |

### West Felician Parish
**Total:** 187

| Race | Count | % |
|------|-------|---|
| Black | 123 | 65.8% |
| White | 64 | 34.2% |

### Winn Parish
**Total:** 145

| Race | Count | % |
|------|-------|---|
| Black | 79 | 54.5% |
| White | 66 | 45.5% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
