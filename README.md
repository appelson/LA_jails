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

_Last updated: 2026-04-27 15:51 UTC_

**Total inmates (latest scrape):** 25,826 across 72 parishes/jails

### Acadia Parish
**Total:** 168

| Race | Count | % |
|------|-------|---|
| White | 90 | 53.6% |
| Black | 76 | 45.2% |
| Asian/PacificIslander | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| White | 82 | 62.6% |
| Black | 47 | 35.9% |
| Unknown | 1 | 0.8% |
| American Indian/Alaska Native | 1 | 0.8% |

### Ascension Parish
**Total:** 510

| Race | Count | % |
|------|-------|---|
| Black | 271 | 53.1% |
| White | 201 | 39.4% |
| Unknown | 35 | 6.9% |
| Asian/PacificIslander | 3 | 0.6% |

### Assumption Parish
**Total:** 143

| Race | Count | % |
|------|-------|---|
| Unknown | 72 | 50.3% |
| White | 71 | 49.7% |

### Avoyelles Parish
**Total:** 387

| Race | Count | % |
|------|-------|---|
| Black | 201 | 51.9% |
| White | 179 | 46.3% |
| Unknown | 6 | 1.6% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 171

| Race | Count | % |
|------|-------|---|
| White | 119 | 69.6% |
| Black | 51 | 29.8% |
| Unknown | 1 | 0.6% |

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
**Total:** 45

| Race | Count | % |
|------|-------|---|
| Black | 29 | 64.4% |
| White | 16 | 35.6% |

### Bossier Parish
**Total:** 1,107

| Race | Count | % |
|------|-------|---|
| Black | 611 | 55.2% |
| White | 493 | 44.5% |
| Unknown | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,589

| Race | Count | % |
|------|-------|---|
| Black | 1,176 | 74.0% |
| White | 375 | 23.6% |
| Unknown | 35 | 2.2% |
| Asian/PacificIslander | 3 | 0.2% |

### Calcasieu Parish
**Total:** 1,042

| Race | Count | % |
|------|-------|---|
| Black | 561 | 53.8% |
| White | 435 | 41.7% |
| Unknown | 44 | 4.2% |
| Asian/PacificIslander | 2 | 0.2% |

### Caldwell Parish
**Total:** 604

| Race | Count | % |
|------|-------|---|
| Black | 392 | 64.9% |
| White | 192 | 31.8% |
| American Indian/Alaska Native | 20 | 3.3% |

### Cameron Parish
**Total:** 22

| Race | Count | % |
|------|-------|---|
| White | 21 | 95.5% |
| Black | 1 | 4.5% |

### Catahoula Parish
**Total:** 133

| Race | Count | % |
|------|-------|---|
| Black | 95 | 71.4% |
| White | 37 | 27.8% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 620

| Race | Count | % |
|------|-------|---|
| Black | 374 | 60.3% |
| White | 246 | 39.7% |

### Concordia Parish
**Total:** 814

| Race | Count | % |
|------|-------|---|
| White | 449 | 55.2% |
| Black | 361 | 44.3% |
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
**Total:** 275

| Race | Count | % |
|------|-------|---|
| Black | 167 | 60.7% |
| White | 107 | 38.9% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 76

| Race | Count | % |
|------|-------|---|
| Black | 39 | 51.3% |
| White | 36 | 47.4% |
| Unknown | 1 | 1.3% |

### Franklin Parish
**Total:** 849

| Race | Count | % |
|------|-------|---|
| Black | 556 | 65.5% |
| White | 282 | 33.2% |
| Unknown | 10 | 1.2% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| Black | 12 | 80.0% |
| White | 3 | 20.0% |

### Iberia Parish
**Total:** 443

| Race | Count | % |
|------|-------|---|
| Black | 276 | 62.3% |
| White | 160 | 36.1% |
| Asian/PacificIslander | 4 | 0.9% |
| Unknown | 2 | 0.5% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 106

| Race | Count | % |
|------|-------|---|
| Black | 68 | 64.2% |
| White | 36 | 34.0% |
| Unknown | 2 | 1.9% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 158

| Race | Count | % |
|------|-------|---|
| Black | 78 | 49.4% |
| White | 75 | 47.5% |
| American Indian/Alaska Native | 3 | 1.9% |
| Asian/PacificIslander | 1 | 0.6% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,164

| Race | Count | % |
|------|-------|---|
| Black | 754 | 64.8% |
| White | 398 | 34.2% |
| Unknown | 8 | 0.7% |
| Asian/PacificIslander | 4 | 0.3% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 68

| Race | Count | % |
|------|-------|---|
| White | 46 | 67.6% |
| Black | 21 | 30.9% |
| Unknown | 1 | 1.5% |

### Lafayette Parish
**Total:** 856

| Race | Count | % |
|------|-------|---|
| Black | 540 | 63.1% |
| White | 305 | 35.6% |
| Unknown | 11 | 1.3% |

### Lafourche Parish
**Total:** 758

| Race | Count | % |
|------|-------|---|
| Black | 385 | 50.8% |
| White | 363 | 47.9% |
| American Indian/Alaska Native | 5 | 0.7% |
| Asian/PacificIslander | 3 | 0.4% |
| Unknown | 2 | 0.3% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 358

| Race | Count | % |
|------|-------|---|
| Black | 264 | 73.7% |
| White | 93 | 26.0% |
| Unknown | 1 | 0.3% |

### Livingston Parish
**Total:** 815

| Race | Count | % |
|------|-------|---|
| White | 590 | 72.4% |
| Black | 217 | 26.6% |
| Unknown | 6 | 0.7% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 142

| Race | Count | % |
|------|-------|---|
| Black | 110 | 77.5% |
| White | 31 | 21.8% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 206

| Race | Count | % |
|------|-------|---|
| Black | 145 | 70.4% |
| White | 61 | 29.6% |

### Natchitoches Parish
**Total:** 197

| Race | Count | % |
|------|-------|---|
| Black | 145 | 73.6% |
| White | 48 | 24.4% |
| Unknown | 3 | 1.5% |
| Asian/PacificIslander | 1 | 0.5% |

### Oakdale Police Department
**Total:** 7

| Race | Count | % |
|------|-------|---|
| White | 4 | 57.1% |
| Black | 3 | 42.9% |

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
**Total:** 1,282

| Race | Count | % |
|------|-------|---|
| Black | 855 | 66.7% |
| White | 411 | 32.1% |
| Unknown | 16 | 1.2% |

### Plaquemines Parish
**Total:** 629

| Race | Count | % |
|------|-------|---|
| Black | 412 | 65.5% |
| White | 197 | 31.3% |
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
**Total:** 973

| Race | Count | % |
|------|-------|---|
| Black | 604 | 62.1% |
| White | 349 | 35.9% |
| Unknown | 18 | 1.8% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| Black | 26 | 60.5% |
| White | 16 | 37.2% |
| Asian/PacificIslander | 1 | 2.3% |

### Richland Parish
**Total:** 723

| Race | Count | % |
|------|-------|---|
| Black | 498 | 68.9% |
| White | 214 | 29.6% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sabine Parish
**Total:** 179

| Race | Count | % |
|------|-------|---|
| White | 101 | 56.4% |
| Black | 76 | 42.5% |
| Unknown | 2 | 1.1% |

### Shreveport Police Department
**Total:** 53

| Race | Count | % |
|------|-------|---|
| Black | 46 | 86.8% |
| White | 6 | 11.3% |
| Unknown | 1 | 1.9% |

### St. Bernard Parish
**Total:** 223

| Race | Count | % |
|------|-------|---|
| Black | 128 | 57.4% |
| White | 92 | 41.3% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.4% |

### St. Charles Parish
**Total:** 176

| Race | Count | % |
|------|-------|---|
| Unknown | 107 | 60.8% |
| White | 69 | 39.2% |

### St. Helena Parish
**Total:** 75

| Race | Count | % |
|------|-------|---|
| Black | 54 | 72.0% |
| White | 16 | 21.3% |
| Unknown | 4 | 5.3% |
| American Indian/Alaska Native | 1 | 1.3% |

### St. James Parish
**Total:** 69

| Race | Count | % |
|------|-------|---|
| Black | 56 | 81.2% |
| White | 13 | 18.8% |

### St. John the Baptist Parish
**Total:** 195

| Race | Count | % |
|------|-------|---|
| Unknown | 123 | 63.1% |
| White | 72 | 36.9% |

### St. Landry Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| Black | 70 | 62.5% |
| White | 40 | 35.7% |
| Unknown | 2 | 1.8% |

### St. Martin Parish
**Total:** 199

| Race | Count | % |
|------|-------|---|
| Black | 102 | 51.3% |
| White | 90 | 45.2% |
| Unknown | 6 | 3.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 240

| Race | Count | % |
|------|-------|---|
| White | 121 | 50.4% |
| Black | 118 | 49.2% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 810

| Race | Count | % |
|------|-------|---|
| White | 409 | 50.5% |
| Black | 361 | 44.6% |
| Unknown | 36 | 4.4% |
| American Indian/Alaska Native | 2 | 0.2% |
| Asian/PacificIslander | 2 | 0.2% |

### Sulphur Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| White | 14 | 93.3% |
| Black | 1 | 6.7% |

### Tangipahoa Parish
**Total:** 721

| Race | Count | % |
|------|-------|---|
| Black | 462 | 64.1% |
| White | 258 | 35.8% |
| Unknown | 1 | 0.1% |

### Tensas Parish
**Total:** 539

| Race | Count | % |
|------|-------|---|
| Black | 354 | 65.7% |
| White | 171 | 31.7% |
| Unknown | 14 | 2.6% |

### Terrebonne Parish
**Total:** 479

| Race | Count | % |
|------|-------|---|
| Black | 251 | 52.4% |
| White | 222 | 46.3% |
| American Indian/Alaska Native | 6 | 1.3% |

### Vermillion Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| White | 68 | 52.3% |
| Black | 60 | 46.2% |
| Unknown | 2 | 1.5% |

### Vernon Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| White | 105 | 69.5% |
| Black | 43 | 28.5% |
| Unknown | 2 | 1.3% |
| Asian/PacificIslander | 1 | 0.7% |

### Ville Platte Police Department
**Total:** 31

| Race | Count | % |
|------|-------|---|
| Black | 18 | 58.1% |
| White | 12 | 38.7% |
| Unknown | 1 | 3.2% |

### Washington Parish
**Total:** 173

| Race | Count | % |
|------|-------|---|
| Black | 92 | 53.2% |
| White | 81 | 46.8% |

### Webster Parish
**Total:** 429

| Race | Count | % |
|------|-------|---|
| White | 213 | 49.7% |
| Black | 211 | 49.2% |
| Unknown | 3 | 0.7% |
| Asian/PacificIslander | 2 | 0.5% |

### West Baton Rouge Parish
**Total:** 124

| Race | Count | % |
|------|-------|---|
| Black | 72 | 58.1% |
| White | 48 | 38.7% |
| Unknown | 3 | 2.4% |
| Asian/PacificIslander | 1 | 0.8% |

### West Carroll Parish
**Total:** 29

| Race | Count | % |
|------|-------|---|
| White | 25 | 86.2% |
| Black | 4 | 13.8% |

### West Felician Parish
**Total:** 183

| Race | Count | % |
|------|-------|---|
| Black | 111 | 60.7% |
| White | 72 | 39.3% |

### Winn Parish
**Total:** 144

| Race | Count | % |
|------|-------|---|
| White | 75 | 52.1% |
| Black | 69 | 47.9% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
