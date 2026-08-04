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

_Last updated: 2026-08-04 02:07 UTC_

**Total inmates (latest scrape):** 27,080 across 72 parishes/jails

### Acadia Parish
**Total:** 166

| Race | Count | % |
|------|-------|---|
| White | 89 | 53.6% |
| Black | 75 | 45.2% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 121

| Race | Count | % |
|------|-------|---|
| White | 77 | 63.6% |
| Black | 40 | 33.1% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 2 | 1.7% |

### Ascension Parish
**Total:** 510

| Race | Count | % |
|------|-------|---|
| Black | 271 | 53.1% |
| White | 202 | 39.6% |
| Unknown | 32 | 6.3% |
| Asian/PacificIslander | 5 | 1.0% |

### Assumption Parish
**Total:** 159

| Race | Count | % |
|------|-------|---|
| Unknown | 91 | 57.2% |
| White | 68 | 42.8% |

### Avoyelles Parish
**Total:** 351

| Race | Count | % |
|------|-------|---|
| Black | 201 | 57.3% |
| White | 147 | 41.9% |
| Unknown | 3 | 0.9% |

### Beauregard Parish
**Total:** 176

| Race | Count | % |
|------|-------|---|
| White | 120 | 68.2% |
| Black | 56 | 31.8% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 13

| Race | Count | % |
|------|-------|---|
| White | 8 | 61.5% |
| Black | 5 | 38.5% |

### Bossier City Police Department
**Total:** 61

| Race | Count | % |
|------|-------|---|
| Black | 39 | 63.9% |
| White | 22 | 36.1% |

### Bossier Parish
**Total:** 1,123

| Race | Count | % |
|------|-------|---|
| Black | 631 | 56.2% |
| White | 490 | 43.6% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Caddo Parish
**Total:** 1,716

| Race | Count | % |
|------|-------|---|
| Black | 1,294 | 75.4% |
| White | 393 | 22.9% |
| Unknown | 29 | 1.7% |

### Calcasieu Parish
**Total:** 1,103

| Race | Count | % |
|------|-------|---|
| Black | 605 | 54.9% |
| White | 455 | 41.3% |
| Unknown | 42 | 3.8% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 607

| Race | Count | % |
|------|-------|---|
| Black | 389 | 64.1% |
| White | 202 | 33.3% |
| American Indian/Alaska Native | 15 | 2.5% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 20

| Race | Count | % |
|------|-------|---|
| White | 20 | 100.0% |

### Catahoula Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 92 | 70.2% |
| White | 38 | 29.0% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 651

| Race | Count | % |
|------|-------|---|
| Black | 404 | 62.1% |
| White | 247 | 37.9% |

### Concordia Parish
**Total:** 825

| Race | Count | % |
|------|-------|---|
| White | 470 | 57.0% |
| Black | 355 | 43.0% |

### DeSoto Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| Black | 70 | 58.3% |
| White | 49 | 40.8% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,278

| Race | Count | % |
|------|-------|---|
| Black | 994 | 77.8% |
| White | 225 | 17.6% |
| Unknown | 56 | 4.4% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### East Feliciana Parish
**Total:** 282

| Race | Count | % |
|------|-------|---|
| Black | 183 | 64.9% |
| White | 97 | 34.4% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 159

| Race | Count | % |
|------|-------|---|
| Black | 94 | 59.1% |
| White | 64 | 40.3% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 849

| Race | Count | % |
|------|-------|---|
| Black | 563 | 66.3% |
| White | 282 | 33.2% |
| Unknown | 4 | 0.5% |

### Hammond Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 11 | 47.8% |
| White | 9 | 39.1% |
| Unknown | 3 | 13.0% |

### Iberia Parish
**Total:** 478

| Race | Count | % |
|------|-------|---|
| Black | 288 | 60.3% |
| White | 179 | 37.4% |
| Unknown | 5 | 1.0% |
| Asian/PacificIslander | 5 | 1.0% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 49

| Race | Count | % |
|------|-------|---|
| Black | 29 | 59.2% |
| White | 20 | 40.8% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 163

| Race | Count | % |
|------|-------|---|
| White | 86 | 52.8% |
| Black | 75 | 46.0% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,205

| Race | Count | % |
|------|-------|---|
| Black | 782 | 64.9% |
| White | 417 | 34.6% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 72

| Race | Count | % |
|------|-------|---|
| White | 47 | 65.3% |
| Black | 24 | 33.3% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 853

| Race | Count | % |
|------|-------|---|
| Black | 558 | 65.4% |
| White | 283 | 33.2% |
| Unknown | 12 | 1.4% |

### Lafourche Parish
**Total:** 774

| Race | Count | % |
|------|-------|---|
| Black | 402 | 51.9% |
| White | 368 | 47.5% |
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
| Black | 272 | 73.9% |
| White | 93 | 25.3% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 840

| Race | Count | % |
|------|-------|---|
| White | 590 | 70.2% |
| Black | 240 | 28.6% |
| Unknown | 7 | 0.8% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| Black | 122 | 80.8% |
| White | 28 | 18.5% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 200

| Race | Count | % |
|------|-------|---|
| Black | 146 | 73.0% |
| White | 54 | 27.0% |

### Natchitoches Parish
**Total:** 190

| Race | Count | % |
|------|-------|---|
| Black | 142 | 74.7% |
| White | 43 | 22.6% |
| Unknown | 5 | 2.6% |

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
**Total:** 1,459

| Race | Count | % |
|------|-------|---|
| Black | 1,253 | 85.9% |
| White | 186 | 12.7% |
| Unknown | 16 | 1.1% |
| Asian/PacificIslander | 4 | 0.3% |

### Ouachita Parish
**Total:** 1,330

| Race | Count | % |
|------|-------|---|
| Black | 892 | 67.1% |
| White | 423 | 31.8% |
| Unknown | 15 | 1.1% |

### Plaquemines Parish
**Total:** 665

| Race | Count | % |
|------|-------|---|
| Black | 432 | 65.0% |
| White | 210 | 31.6% |
| Unknown | 12 | 1.8% |
| Asian/PacificIslander | 9 | 1.4% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 122

| Race | Count | % |
|------|-------|---|
| Black | 75 | 61.5% |
| White | 44 | 36.1% |
| Unknown | 2 | 1.6% |
| American Indian/Alaska Native | 1 | 0.8% |

### Rapides Parish
**Total:** 1,045

| Race | Count | % |
|------|-------|---|
| Black | 658 | 63.0% |
| White | 370 | 35.4% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 41

| Race | Count | % |
|------|-------|---|
| Black | 21 | 51.2% |
| White | 19 | 46.3% |
| Asian/PacificIslander | 1 | 2.4% |

### Richland Parish
**Total:** 714

| Race | Count | % |
|------|-------|---|
| Black | 492 | 68.9% |
| White | 213 | 29.8% |
| Unknown | 6 | 0.8% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 191

| Race | Count | % |
|------|-------|---|
| White | 110 | 57.6% |
| Black | 77 | 40.3% |
| Unknown | 3 | 1.6% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 41

| Race | Count | % |
|------|-------|---|
| Black | 29 | 70.7% |
| White | 11 | 26.8% |
| Unknown | 1 | 2.4% |

### St. Bernard Parish
**Total:** 235

| Race | Count | % |
|------|-------|---|
| Black | 138 | 58.7% |
| White | 92 | 39.1% |
| Asian/PacificIslander | 3 | 1.3% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 172

| Race | Count | % |
|------|-------|---|
| Unknown | 97 | 56.4% |
| White | 75 | 43.6% |

### St. Helena Parish
**Total:** 42

| Race | Count | % |
|------|-------|---|
| Black | 30 | 71.4% |
| White | 12 | 28.6% |

### St. James Parish
**Total:** 75

| Race | Count | % |
|------|-------|---|
| Black | 65 | 86.7% |
| White | 10 | 13.3% |

### St. John the Baptist Parish
**Total:** 228

| Race | Count | % |
|------|-------|---|
| Unknown | 152 | 66.7% |
| White | 76 | 33.3% |

### St. Landry Parish
**Total:** 138

| Race | Count | % |
|------|-------|---|
| Black | 87 | 63.0% |
| White | 49 | 35.5% |
| Unknown | 2 | 1.4% |

### St. Martin Parish
**Total:** 212

| Race | Count | % |
|------|-------|---|
| Black | 104 | 49.1% |
| White | 100 | 47.2% |
| Unknown | 8 | 3.8% |

### St. Mary Parish
**Total:** 292

| Race | Count | % |
|------|-------|---|
| Black | 152 | 52.1% |
| White | 139 | 47.6% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 901

| Race | Count | % |
|------|-------|---|
| White | 459 | 50.9% |
| Black | 399 | 44.3% |
| Unknown | 41 | 4.6% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 13

| Race | Count | % |
|------|-------|---|
| White | 10 | 76.9% |
| Black | 3 | 23.1% |

### Tangipahoa Parish
**Total:** 699

| Race | Count | % |
|------|-------|---|
| Black | 463 | 66.2% |
| White | 233 | 33.3% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 569

| Race | Count | % |
|------|-------|---|
| Black | 382 | 67.1% |
| White | 175 | 30.8% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 570

| Race | Count | % |
|------|-------|---|
| Black | 319 | 56.0% |
| White | 239 | 41.9% |
| American Indian/Alaska Native | 12 | 2.1% |

### Vermillion Parish
**Total:** 113

| Race | Count | % |
|------|-------|---|
| White | 55 | 48.7% |
| Black | 55 | 48.7% |
| Unknown | 2 | 1.8% |
| Asian/PacificIslander | 1 | 0.9% |

### Vernon Parish
**Total:** 184

| Race | Count | % |
|------|-------|---|
| White | 128 | 69.6% |
| Black | 54 | 29.3% |
| Asian/PacificIslander | 1 | 0.5% |
| Unknown | 1 | 0.5% |

### Ville Platte Police Department
**Total:** 31

| Race | Count | % |
|------|-------|---|
| Black | 18 | 58.1% |
| White | 12 | 38.7% |
| Unknown | 1 | 3.2% |

### Washington Parish
**Total:** 194

| Race | Count | % |
|------|-------|---|
| Black | 104 | 53.6% |
| White | 89 | 45.9% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 453

| Race | Count | % |
|------|-------|---|
| Black | 236 | 52.1% |
| White | 210 | 46.4% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 134

| Race | Count | % |
|------|-------|---|
| Black | 88 | 65.7% |
| White | 42 | 31.3% |
| Unknown | 3 | 2.2% |
| Asian/PacificIslander | 1 | 0.7% |

### West Carroll Parish
**Total:** 28

| Race | Count | % |
|------|-------|---|
| White | 22 | 78.6% |
| Black | 6 | 21.4% |

### West Felician Parish
**Total:** 203

| Race | Count | % |
|------|-------|---|
| Black | 130 | 64.0% |
| White | 73 | 36.0% |

### Winn Parish
**Total:** 147

| Race | Count | % |
|------|-------|---|
| Black | 74 | 50.3% |
| White | 73 | 49.7% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
