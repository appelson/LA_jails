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

_Last updated: 2026-06-17 03:38 UTC_

**Total inmates (latest scrape):** 26,623 across 72 parishes/jails

### Acadia Parish
**Total:** 182

| Race | Count | % |
|------|-------|---|
| White | 97 | 53.3% |
| Black | 83 | 45.6% |
| Asian/PacificIslander | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Allen Parish
**Total:** 116

| Race | Count | % |
|------|-------|---|
| White | 74 | 63.8% |
| Black | 39 | 33.6% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 543

| Race | Count | % |
|------|-------|---|
| Black | 291 | 53.6% |
| White | 214 | 39.4% |
| Unknown | 34 | 6.3% |
| Asian/PacificIslander | 4 | 0.7% |

### Assumption Parish
**Total:** 154

| Race | Count | % |
|------|-------|---|
| Unknown | 83 | 53.9% |
| White | 71 | 46.1% |

### Avoyelles Parish
**Total:** 358

| Race | Count | % |
|------|-------|---|
| Black | 201 | 56.1% |
| White | 153 | 42.7% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 157

| Race | Count | % |
|------|-------|---|
| White | 109 | 69.4% |
| Black | 48 | 30.6% |

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
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 30 | 68.2% |
| White | 13 | 29.5% |
| Asian/PacificIslander | 1 | 2.3% |

### Bossier Parish
**Total:** 1,106

| Race | Count | % |
|------|-------|---|
| Black | 608 | 55.0% |
| White | 497 | 44.9% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,673

| Race | Count | % |
|------|-------|---|
| Black | 1,250 | 74.7% |
| White | 395 | 23.6% |
| Unknown | 26 | 1.6% |
| Asian/PacificIslander | 2 | 0.1% |

### Calcasieu Parish
**Total:** 1,090

| Race | Count | % |
|------|-------|---|
| Black | 602 | 55.2% |
| White | 445 | 40.8% |
| Unknown | 41 | 3.8% |
| Asian/PacificIslander | 2 | 0.2% |

### Caldwell Parish
**Total:** 610

| Race | Count | % |
|------|-------|---|
| Black | 389 | 63.8% |
| White | 200 | 32.8% |
| American Indian/Alaska Native | 20 | 3.3% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 25

| Race | Count | % |
|------|-------|---|
| White | 22 | 88.0% |
| Black | 2 | 8.0% |
| Unknown | 1 | 4.0% |

### Catahoula Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 91 | 70.0% |
| White | 38 | 29.2% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 666

| Race | Count | % |
|------|-------|---|
| Black | 414 | 62.2% |
| White | 252 | 37.8% |

### Concordia Parish
**Total:** 807

| Race | Count | % |
|------|-------|---|
| White | 458 | 56.8% |
| Black | 347 | 43.0% |
| Unknown | 2 | 0.2% |

### DeSoto Parish
**Total:** 124

| Race | Count | % |
|------|-------|---|
| Black | 71 | 57.3% |
| White | 52 | 41.9% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,346

| Race | Count | % |
|------|-------|---|
| Black | 1,067 | 79.3% |
| White | 213 | 15.8% |
| Unknown | 63 | 4.7% |
| Asian/PacificIslander | 3 | 0.2% |

### East Feliciana Parish
**Total:** 265

| Race | Count | % |
|------|-------|---|
| Black | 169 | 63.8% |
| White | 95 | 35.8% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| Black | 80 | 53.0% |
| White | 70 | 46.4% |
| Unknown | 1 | 0.7% |

### Franklin Parish
**Total:** 840

| Race | Count | % |
|------|-------|---|
| Black | 546 | 65.0% |
| White | 283 | 33.7% |
| Unknown | 11 | 1.3% |

### Hammond Police Department
**Total:** 14

| Race | Count | % |
|------|-------|---|
| Black | 8 | 57.1% |
| White | 5 | 35.7% |
| Unknown | 1 | 7.1% |

### Iberia Parish
**Total:** 447

| Race | Count | % |
|------|-------|---|
| Black | 265 | 59.3% |
| White | 172 | 38.5% |
| Asian/PacificIslander | 5 | 1.1% |
| Unknown | 4 | 0.9% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 96

| Race | Count | % |
|------|-------|---|
| Black | 63 | 65.6% |
| White | 32 | 33.3% |
| Unknown | 1 | 1.0% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 152

| Race | Count | % |
|------|-------|---|
| White | 79 | 52.0% |
| Black | 69 | 45.4% |
| American Indian/Alaska Native | 3 | 2.0% |
| Unknown | 1 | 0.7% |

### Jefferson Parish
**Total:** 1,155

| Race | Count | % |
|------|-------|---|
| Black | 750 | 64.9% |
| White | 399 | 34.5% |
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
| White | 46 | 63.9% |
| Black | 25 | 34.7% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 856

| Race | Count | % |
|------|-------|---|
| Black | 555 | 64.8% |
| White | 285 | 33.3% |
| Unknown | 16 | 1.9% |

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
**Total:** 377

| Race | Count | % |
|------|-------|---|
| Black | 286 | 75.9% |
| White | 88 | 23.3% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 792

| Race | Count | % |
|------|-------|---|
| White | 560 | 70.7% |
| Black | 221 | 27.9% |
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
**Total:** 207

| Race | Count | % |
|------|-------|---|
| Black | 141 | 68.1% |
| White | 66 | 31.9% |

### Natchitoches Parish
**Total:** 193

| Race | Count | % |
|------|-------|---|
| Black | 146 | 75.6% |
| White | 44 | 22.8% |
| Unknown | 3 | 1.6% |

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
**Total:** 1,323

| Race | Count | % |
|------|-------|---|
| Black | 883 | 66.7% |
| White | 425 | 32.1% |
| Unknown | 15 | 1.1% |

### Plaquemines Parish
**Total:** 647

| Race | Count | % |
|------|-------|---|
| Black | 431 | 66.6% |
| White | 196 | 30.3% |
| Unknown | 12 | 1.9% |
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
**Total:** 1,036

| Race | Count | % |
|------|-------|---|
| Black | 661 | 63.8% |
| White | 356 | 34.4% |
| Unknown | 17 | 1.6% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 47

| Race | Count | % |
|------|-------|---|
| Black | 28 | 59.6% |
| White | 18 | 38.3% |
| Asian/PacificIslander | 1 | 2.1% |

### Richland Parish
**Total:** 733

| Race | Count | % |
|------|-------|---|
| Black | 505 | 68.9% |
| White | 219 | 29.9% |
| Unknown | 6 | 0.8% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 196

| Race | Count | % |
|------|-------|---|
| White | 107 | 54.6% |
| Black | 86 | 43.9% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 58

| Race | Count | % |
|------|-------|---|
| Black | 42 | 72.4% |
| White | 15 | 25.9% |
| Unknown | 1 | 1.7% |

### St. Bernard Parish
**Total:** 228

| Race | Count | % |
|------|-------|---|
| Black | 136 | 59.6% |
| White | 88 | 38.6% |
| Asian/PacificIslander | 3 | 1.3% |
| Unknown | 1 | 0.4% |

### St. Charles Parish
**Total:** 185

| Race | Count | % |
|------|-------|---|
| Unknown | 111 | 60.0% |
| White | 74 | 40.0% |

### St. Helena Parish
**Total:** 47

| Race | Count | % |
|------|-------|---|
| Black | 32 | 68.1% |
| White | 14 | 29.8% |
| Unknown | 1 | 2.1% |

### St. James Parish
**Total:** 70

| Race | Count | % |
|------|-------|---|
| Black | 59 | 84.3% |
| White | 11 | 15.7% |

### St. John the Baptist Parish
**Total:** 201

| Race | Count | % |
|------|-------|---|
| Unknown | 129 | 64.2% |
| White | 72 | 35.8% |

### St. Landry Parish
**Total:** 117

| Race | Count | % |
|------|-------|---|
| Black | 76 | 65.0% |
| White | 39 | 33.3% |
| Unknown | 2 | 1.7% |

### St. Martin Parish
**Total:** 210

| Race | Count | % |
|------|-------|---|
| Black | 106 | 50.5% |
| White | 94 | 44.8% |
| Unknown | 9 | 4.3% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 281

| Race | Count | % |
|------|-------|---|
| Black | 147 | 52.3% |
| White | 133 | 47.3% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 877

| Race | Count | % |
|------|-------|---|
| White | 459 | 52.3% |
| Black | 377 | 43.0% |
| Unknown | 38 | 4.3% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sulphur Police Department
**Total:** 18

| Race | Count | % |
|------|-------|---|
| White | 15 | 83.3% |
| Black | 3 | 16.7% |

### Tangipahoa Parish
**Total:** 658

| Race | Count | % |
|------|-------|---|
| Black | 413 | 62.8% |
| White | 244 | 37.1% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 560

| Race | Count | % |
|------|-------|---|
| Black | 372 | 66.4% |
| White | 178 | 31.8% |
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
| Black | 60 | 45.8% |
| Unknown | 3 | 2.3% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 162

| Race | Count | % |
|------|-------|---|
| White | 109 | 67.3% |
| Black | 50 | 30.9% |
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
**Total:** 121

| Race | Count | % |
|------|-------|---|
| Black | 82 | 67.8% |
| White | 35 | 28.9% |
| Unknown | 3 | 2.5% |
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
**Total:** 143

| Race | Count | % |
|------|-------|---|
| Black | 77 | 53.8% |
| White | 66 | 46.2% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
