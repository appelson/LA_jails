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

_Last updated: 2026-08-06 02:09 UTC_

**Total inmates (latest scrape):** 26,899 across 71 parishes/jails

### Acadia Parish
**Total:** 167

| Race | Count | % |
|------|-------|---|
| White | 88 | 52.7% |
| Black | 77 | 46.1% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 121

| Race | Count | % |
|------|-------|---|
| White | 76 | 62.8% |
| Black | 41 | 33.9% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 2 | 1.7% |

### Ascension Parish
**Total:** 518

| Race | Count | % |
|------|-------|---|
| Black | 274 | 52.9% |
| White | 207 | 40.0% |
| Unknown | 32 | 6.2% |
| Asian/PacificIslander | 5 | 1.0% |

### Assumption Parish
**Total:** 162

| Race | Count | % |
|------|-------|---|
| Unknown | 92 | 56.8% |
| White | 70 | 43.2% |

### Avoyelles Parish
**Total:** 344

| Race | Count | % |
|------|-------|---|
| Black | 193 | 56.1% |
| White | 148 | 43.0% |
| Unknown | 3 | 0.9% |

### Beauregard Parish
**Total:** 174

| Race | Count | % |
|------|-------|---|
| White | 109 | 62.6% |
| Black | 65 | 37.4% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| White | 9 | 60.0% |
| Black | 6 | 40.0% |

### Bossier City Police Department
**Total:** 60

| Race | Count | % |
|------|-------|---|
| Black | 38 | 63.3% |
| White | 22 | 36.7% |

### Bossier Parish
**Total:** 1,129

| Race | Count | % |
|------|-------|---|
| Black | 631 | 55.9% |
| White | 496 | 43.9% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Caddo Parish
**Total:** 1,726

| Race | Count | % |
|------|-------|---|
| Black | 1,300 | 75.3% |
| White | 398 | 23.1% |
| Unknown | 28 | 1.6% |

### Calcasieu Parish
**Total:** 1,099

| Race | Count | % |
|------|-------|---|
| Black | 601 | 54.7% |
| White | 455 | 41.4% |
| Unknown | 42 | 3.8% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 603

| Race | Count | % |
|------|-------|---|
| Black | 388 | 64.3% |
| White | 199 | 33.0% |
| American Indian/Alaska Native | 15 | 2.5% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 21

| Race | Count | % |
|------|-------|---|
| White | 21 | 100.0% |

### Catahoula Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| Black | 91 | 68.9% |
| White | 39 | 29.5% |
| Unknown | 2 | 1.5% |

### Claiborne Parish
**Total:** 644

| Race | Count | % |
|------|-------|---|
| Black | 397 | 61.6% |
| White | 247 | 38.4% |

### Concordia Parish
**Total:** 825

| Race | Count | % |
|------|-------|---|
| White | 466 | 56.5% |
| Black | 359 | 43.5% |

### DeSoto Parish
**Total:** 121

| Race | Count | % |
|------|-------|---|
| Black | 70 | 57.9% |
| White | 51 | 42.1% |

### East Baton Rouge Parish
**Total:** 1,292

| Race | Count | % |
|------|-------|---|
| Black | 1,001 | 77.5% |
| White | 232 | 18.0% |
| Unknown | 55 | 4.3% |
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
**Total:** 156

| Race | Count | % |
|------|-------|---|
| Black | 93 | 59.6% |
| White | 62 | 39.7% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 846

| Race | Count | % |
|------|-------|---|
| Black | 561 | 66.3% |
| White | 281 | 33.2% |
| Unknown | 4 | 0.5% |

### Hammond Police Department
**Total:** 26

| Race | Count | % |
|------|-------|---|
| Black | 12 | 46.2% |
| White | 10 | 38.5% |
| Unknown | 4 | 15.4% |

### Iberia Parish
**Total:** 469

| Race | Count | % |
|------|-------|---|
| Black | 282 | 60.1% |
| White | 176 | 37.5% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 59

| Race | Count | % |
|------|-------|---|
| Black | 33 | 55.9% |
| White | 25 | 42.4% |
| Unknown | 1 | 1.7% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 161

| Race | Count | % |
|------|-------|---|
| White | 84 | 52.2% |
| Black | 75 | 46.6% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,212

| Race | Count | % |
|------|-------|---|
| Black | 795 | 65.6% |
| White | 411 | 33.9% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 74

| Race | Count | % |
|------|-------|---|
| White | 48 | 64.9% |
| Black | 25 | 33.8% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 839

| Race | Count | % |
|------|-------|---|
| Black | 554 | 66.0% |
| White | 273 | 32.5% |
| Unknown | 12 | 1.4% |

### Lafourche Parish
**Total:** 778

| Race | Count | % |
|------|-------|---|
| Black | 397 | 51.0% |
| White | 377 | 48.5% |
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
**Total:** 821

| Race | Count | % |
|------|-------|---|
| White | 584 | 71.1% |
| Black | 228 | 27.8% |
| Unknown | 6 | 0.7% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| Black | 123 | 81.5% |
| White | 27 | 17.9% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 203

| Race | Count | % |
|------|-------|---|
| Black | 148 | 72.9% |
| White | 55 | 27.1% |

### Natchitoches Parish
**Total:** 188

| Race | Count | % |
|------|-------|---|
| Black | 143 | 76.1% |
| White | 41 | 21.8% |
| Unknown | 4 | 2.1% |

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
**Total:** 1,456

| Race | Count | % |
|------|-------|---|
| Black | 1,248 | 85.7% |
| White | 187 | 12.8% |
| Unknown | 16 | 1.1% |
| Asian/PacificIslander | 5 | 0.3% |

### Ouachita Parish
**Total:** 1,321

| Race | Count | % |
|------|-------|---|
| Black | 890 | 67.4% |
| White | 420 | 31.8% |
| Unknown | 11 | 0.8% |

### Plaquemines Parish
**Total:** 659

| Race | Count | % |
|------|-------|---|
| Black | 427 | 64.8% |
| White | 209 | 31.7% |
| Unknown | 12 | 1.8% |
| Asian/PacificIslander | 9 | 1.4% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 122

| Race | Count | % |
|------|-------|---|
| Black | 76 | 62.3% |
| White | 43 | 35.2% |
| Unknown | 2 | 1.6% |
| American Indian/Alaska Native | 1 | 0.8% |

### Rapides Parish
**Total:** 1,054

| Race | Count | % |
|------|-------|---|
| Black | 670 | 63.6% |
| White | 368 | 34.9% |
| Unknown | 14 | 1.3% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 40

| Race | Count | % |
|------|-------|---|
| Black | 22 | 55.0% |
| White | 17 | 42.5% |
| Asian/PacificIslander | 1 | 2.5% |

### Richland Parish
**Total:** 706

| Race | Count | % |
|------|-------|---|
| Black | 488 | 69.1% |
| White | 209 | 29.6% |
| Unknown | 6 | 0.8% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 189

| Race | Count | % |
|------|-------|---|
| White | 109 | 57.7% |
| Black | 78 | 41.3% |
| Unknown | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 45

| Race | Count | % |
|------|-------|---|
| Black | 32 | 71.1% |
| White | 13 | 28.9% |

### St. Bernard Parish
**Total:** 232

| Race | Count | % |
|------|-------|---|
| Black | 132 | 56.9% |
| White | 95 | 40.9% |
| Asian/PacificIslander | 3 | 1.3% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 171

| Race | Count | % |
|------|-------|---|
| Unknown | 97 | 56.7% |
| White | 74 | 43.3% |

### St. Helena Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| Black | 30 | 69.8% |
| White | 13 | 30.2% |

### St. James Parish
**Total:** 78

| Race | Count | % |
|------|-------|---|
| Black | 67 | 85.9% |
| White | 11 | 14.1% |

### St. John the Baptist Parish
**Total:** 229

| Race | Count | % |
|------|-------|---|
| Unknown | 148 | 64.6% |
| White | 81 | 35.4% |

### St. Landry Parish
**Total:** 138

| Race | Count | % |
|------|-------|---|
| Black | 91 | 65.9% |
| White | 45 | 32.6% |
| Unknown | 2 | 1.4% |

### St. Martin Parish
**Total:** 217

| Race | Count | % |
|------|-------|---|
| Black | 108 | 49.8% |
| White | 101 | 46.5% |
| Unknown | 8 | 3.7% |

### St. Mary Parish
**Total:** 292

| Race | Count | % |
|------|-------|---|
| Black | 152 | 52.1% |
| White | 139 | 47.6% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 893

| Race | Count | % |
|------|-------|---|
| White | 456 | 51.1% |
| Black | 396 | 44.3% |
| Unknown | 39 | 4.4% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 13

| Race | Count | % |
|------|-------|---|
| White | 11 | 84.6% |
| Black | 2 | 15.4% |

### Tangipahoa Parish
**Total:** 701

| Race | Count | % |
|------|-------|---|
| Black | 463 | 66.0% |
| White | 234 | 33.4% |
| Unknown | 4 | 0.6% |

### Tensas Parish
**Total:** 563

| Race | Count | % |
|------|-------|---|
| Black | 379 | 67.3% |
| White | 172 | 30.6% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 576

| Race | Count | % |
|------|-------|---|
| Black | 325 | 56.4% |
| White | 239 | 41.5% |
| American Indian/Alaska Native | 12 | 2.1% |

### Vermillion Parish
**Total:** 117

| Race | Count | % |
|------|-------|---|
| White | 57 | 48.7% |
| Black | 57 | 48.7% |
| Unknown | 2 | 1.7% |
| Asian/PacificIslander | 1 | 0.9% |

### Vernon Parish
**Total:** 173

| Race | Count | % |
|------|-------|---|
| White | 122 | 70.5% |
| Black | 49 | 28.3% |
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
**Total:** 191

| Race | Count | % |
|------|-------|---|
| Black | 100 | 52.4% |
| White | 90 | 47.1% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 442

| Race | Count | % |
|------|-------|---|
| Black | 230 | 52.0% |
| White | 205 | 46.4% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 2 | 0.5% |

### West Carroll Parish
**Total:** 29

| Race | Count | % |
|------|-------|---|
| White | 23 | 79.3% |
| Black | 6 | 20.7% |

### West Felician Parish
**Total:** 202

| Race | Count | % |
|------|-------|---|
| Black | 129 | 63.9% |
| White | 73 | 36.1% |

### Winn Parish
**Total:** 149

| Race | Count | % |
|------|-------|---|
| Black | 75 | 50.3% |
| White | 74 | 49.7% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
