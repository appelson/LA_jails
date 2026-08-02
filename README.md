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

_Last updated: 2026-08-02 02:18 UTC_

**Total inmates (latest scrape):** 26,929 across 72 parishes/jails

### Acadia Parish
**Total:** 165

| Race | Count | % |
|------|-------|---|
| White | 90 | 54.5% |
| Black | 73 | 44.2% |
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
**Total:** 510

| Race | Count | % |
|------|-------|---|
| Black | 274 | 53.7% |
| White | 200 | 39.2% |
| Unknown | 32 | 6.3% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 161

| Race | Count | % |
|------|-------|---|
| Unknown | 92 | 57.1% |
| White | 69 | 42.9% |

### Avoyelles Parish
**Total:** 346

| Race | Count | % |
|------|-------|---|
| Black | 197 | 56.9% |
| White | 146 | 42.2% |
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
**Total:** 16

| Race | Count | % |
|------|-------|---|
| White | 10 | 62.5% |
| Black | 6 | 37.5% |

### Bossier City Police Department
**Total:** 66

| Race | Count | % |
|------|-------|---|
| Black | 43 | 65.2% |
| White | 23 | 34.8% |

### Bossier Parish
**Total:** 1,124

| Race | Count | % |
|------|-------|---|
| Black | 632 | 56.2% |
| White | 490 | 43.6% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Caddo Parish
**Total:** 1,700

| Race | Count | % |
|------|-------|---|
| Black | 1,281 | 75.4% |
| White | 390 | 22.9% |
| Unknown | 29 | 1.7% |

### Calcasieu Parish
**Total:** 1,099

| Race | Count | % |
|------|-------|---|
| Black | 603 | 54.9% |
| White | 452 | 41.1% |
| Unknown | 43 | 3.9% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 617

| Race | Count | % |
|------|-------|---|
| Black | 395 | 64.0% |
| White | 206 | 33.4% |
| American Indian/Alaska Native | 15 | 2.4% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 21

| Race | Count | % |
|------|-------|---|
| White | 21 | 100.0% |

### Catahoula Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 92 | 70.2% |
| White | 38 | 29.0% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 652

| Race | Count | % |
|------|-------|---|
| Black | 404 | 62.0% |
| White | 248 | 38.0% |

### Concordia Parish
**Total:** 822

| Race | Count | % |
|------|-------|---|
| White | 469 | 57.1% |
| Black | 353 | 42.9% |

### DeSoto Parish
**Total:** 125

| Race | Count | % |
|------|-------|---|
| Black | 73 | 58.4% |
| White | 51 | 40.8% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,255

| Race | Count | % |
|------|-------|---|
| Black | 969 | 77.2% |
| White | 229 | 18.2% |
| Unknown | 54 | 4.3% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### East Feliciana Parish
**Total:** 282

| Race | Count | % |
|------|-------|---|
| Black | 184 | 65.2% |
| White | 96 | 34.0% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 158

| Race | Count | % |
|------|-------|---|
| Black | 93 | 58.9% |
| White | 64 | 40.5% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 854

| Race | Count | % |
|------|-------|---|
| Black | 565 | 66.2% |
| White | 285 | 33.4% |
| Unknown | 4 | 0.5% |

### Hammond Police Department
**Total:** 25

| Race | Count | % |
|------|-------|---|
| Black | 12 | 48.0% |
| White | 10 | 40.0% |
| Unknown | 3 | 12.0% |

### Iberia Parish
**Total:** 478

| Race | Count | % |
|------|-------|---|
| Black | 286 | 59.8% |
| White | 180 | 37.7% |
| Unknown | 6 | 1.3% |
| Asian/PacificIslander | 5 | 1.0% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 48

| Race | Count | % |
|------|-------|---|
| Black | 28 | 58.3% |
| White | 20 | 41.7% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 165

| Race | Count | % |
|------|-------|---|
| White | 86 | 52.1% |
| Black | 76 | 46.1% |
| American Indian/Alaska Native | 2 | 1.2% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,194

| Race | Count | % |
|------|-------|---|
| Black | 768 | 64.3% |
| White | 419 | 35.1% |
| Unknown | 6 | 0.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 74

| Race | Count | % |
|------|-------|---|
| White | 49 | 66.2% |
| Black | 24 | 32.4% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 837

| Race | Count | % |
|------|-------|---|
| Black | 550 | 65.7% |
| White | 276 | 33.0% |
| Unknown | 11 | 1.3% |

### Lafourche Parish
**Total:** 771

| Race | Count | % |
|------|-------|---|
| Black | 397 | 51.5% |
| White | 370 | 48.0% |
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
| White | 93 | 25.4% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 830

| Race | Count | % |
|------|-------|---|
| White | 584 | 70.4% |
| Black | 235 | 28.3% |
| Unknown | 8 | 1.0% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 152

| Race | Count | % |
|------|-------|---|
| Black | 122 | 80.3% |
| White | 29 | 19.1% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 205

| Race | Count | % |
|------|-------|---|
| Black | 149 | 72.7% |
| White | 53 | 25.9% |
| Unknown | 3 | 1.5% |

### Natchitoches Parish
**Total:** 184

| Race | Count | % |
|------|-------|---|
| Black | 140 | 76.1% |
| White | 40 | 21.7% |
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
**Total:** 1,331

| Race | Count | % |
|------|-------|---|
| Black | 888 | 66.7% |
| White | 428 | 32.2% |
| Unknown | 15 | 1.1% |

### Plaquemines Parish
**Total:** 661

| Race | Count | % |
|------|-------|---|
| Black | 428 | 64.8% |
| White | 210 | 31.8% |
| Unknown | 12 | 1.8% |
| Asian/PacificIslander | 9 | 1.4% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| Black | 75 | 62.5% |
| White | 42 | 35.0% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.8% |

### Rapides Parish
**Total:** 1,041

| Race | Count | % |
|------|-------|---|
| Black | 656 | 63.0% |
| White | 369 | 35.4% |
| Unknown | 14 | 1.3% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 40

| Race | Count | % |
|------|-------|---|
| Black | 20 | 50.0% |
| White | 19 | 47.5% |
| Asian/PacificIslander | 1 | 2.5% |

### Richland Parish
**Total:** 712

| Race | Count | % |
|------|-------|---|
| Black | 492 | 69.1% |
| White | 211 | 29.6% |
| Unknown | 6 | 0.8% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 189

| Race | Count | % |
|------|-------|---|
| White | 108 | 57.1% |
| Black | 77 | 40.7% |
| Unknown | 3 | 1.6% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 45

| Race | Count | % |
|------|-------|---|
| Black | 38 | 84.4% |
| White | 7 | 15.6% |

### St. Bernard Parish
**Total:** 230

| Race | Count | % |
|------|-------|---|
| Black | 134 | 58.3% |
| White | 91 | 39.6% |
| Asian/PacificIslander | 3 | 1.3% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 171

| Race | Count | % |
|------|-------|---|
| Unknown | 100 | 58.5% |
| White | 71 | 41.5% |

### St. Helena Parish
**Total:** 41

| Race | Count | % |
|------|-------|---|
| Black | 29 | 70.7% |
| White | 12 | 29.3% |

### St. James Parish
**Total:** 78

| Race | Count | % |
|------|-------|---|
| Black | 66 | 84.6% |
| White | 12 | 15.4% |

### St. John the Baptist Parish
**Total:** 228

| Race | Count | % |
|------|-------|---|
| Unknown | 152 | 66.7% |
| White | 76 | 33.3% |

### St. Landry Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 86 | 66.2% |
| White | 42 | 32.3% |
| Unknown | 2 | 1.5% |

### St. Martin Parish
**Total:** 212

| Race | Count | % |
|------|-------|---|
| Black | 106 | 50.0% |
| White | 98 | 46.2% |
| Unknown | 8 | 3.8% |

### St. Mary Parish
**Total:** 290

| Race | Count | % |
|------|-------|---|
| Black | 151 | 52.1% |
| White | 138 | 47.6% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 905

| Race | Count | % |
|------|-------|---|
| White | 462 | 51.0% |
| Black | 400 | 44.2% |
| Unknown | 41 | 4.5% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| White | 11 | 73.3% |
| Black | 4 | 26.7% |

### Tangipahoa Parish
**Total:** 700

| Race | Count | % |
|------|-------|---|
| Black | 464 | 66.3% |
| White | 233 | 33.3% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 572

| Race | Count | % |
|------|-------|---|
| Black | 386 | 67.5% |
| White | 174 | 30.4% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 569

| Race | Count | % |
|------|-------|---|
| Black | 317 | 55.7% |
| White | 240 | 42.2% |
| American Indian/Alaska Native | 12 | 2.1% |

### Vermillion Parish
**Total:** 114

| Race | Count | % |
|------|-------|---|
| Black | 56 | 49.1% |
| White | 55 | 48.2% |
| Unknown | 2 | 1.8% |
| Asian/PacificIslander | 1 | 0.9% |

### Vernon Parish
**Total:** 182

| Race | Count | % |
|------|-------|---|
| White | 126 | 69.2% |
| Black | 54 | 29.7% |
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
**Total:** 188

| Race | Count | % |
|------|-------|---|
| Black | 101 | 53.7% |
| White | 86 | 45.7% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 458

| Race | Count | % |
|------|-------|---|
| Black | 239 | 52.2% |
| White | 211 | 46.1% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 3 | 0.7% |

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
**Total:** 204

| Race | Count | % |
|------|-------|---|
| Black | 131 | 64.2% |
| White | 73 | 35.8% |

### Winn Parish
**Total:** 146

| Race | Count | % |
|------|-------|---|
| White | 73 | 50.0% |
| Black | 73 | 50.0% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
