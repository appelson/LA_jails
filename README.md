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

_Last updated: 2026-07-05 02:41 UTC_

**Total inmates (latest scrape):** 26,780 across 72 parishes/jails

### Acadia Parish
**Total:** 165

| Race | Count | % |
|------|-------|---|
| White | 96 | 58.2% |
| Black | 67 | 40.6% |
| Asian/PacificIslander | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 116

| Race | Count | % |
|------|-------|---|
| White | 73 | 62.9% |
| Black | 40 | 34.5% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 523

| Race | Count | % |
|------|-------|---|
| Black | 277 | 53.0% |
| White | 212 | 40.5% |
| Unknown | 30 | 5.7% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 157

| Race | Count | % |
|------|-------|---|
| Unknown | 88 | 56.1% |
| White | 69 | 43.9% |

### Avoyelles Parish
**Total:** 364

| Race | Count | % |
|------|-------|---|
| Black | 200 | 54.9% |
| White | 160 | 44.0% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 146

| Race | Count | % |
|------|-------|---|
| White | 103 | 70.5% |
| Black | 43 | 29.5% |

### Bienville Parish
**Total:** 41

| Race | Count | % |
|------|-------|---|
| White | 22 | 53.7% |
| Unknown | 19 | 46.3% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 48

| Race | Count | % |
|------|-------|---|
| Black | 28 | 58.3% |
| White | 20 | 41.7% |

### Bossier Parish
**Total:** 1,131

| Race | Count | % |
|------|-------|---|
| Black | 631 | 55.8% |
| White | 498 | 44.0% |
| American Indian/Alaska Native | 1 | 0.1% |
| Unknown | 1 | 0.1% |

### Caddo Parish
**Total:** 1,700

| Race | Count | % |
|------|-------|---|
| Black | 1,279 | 75.2% |
| White | 392 | 23.1% |
| Unknown | 27 | 1.6% |
| Asian/PacificIslander | 2 | 0.1% |

### Calcasieu Parish
**Total:** 1,107

| Race | Count | % |
|------|-------|---|
| Black | 614 | 55.5% |
| White | 449 | 40.6% |
| Unknown | 41 | 3.7% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 618

| Race | Count | % |
|------|-------|---|
| Black | 389 | 62.9% |
| White | 208 | 33.7% |
| American Indian/Alaska Native | 20 | 3.2% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 18

| Race | Count | % |
|------|-------|---|
| White | 17 | 94.4% |
| Unknown | 1 | 5.6% |

### Catahoula Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 91 | 69.5% |
| White | 39 | 29.8% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 676

| Race | Count | % |
|------|-------|---|
| Black | 421 | 62.3% |
| White | 255 | 37.7% |

### Concordia Parish
**Total:** 803

| Race | Count | % |
|------|-------|---|
| White | 450 | 56.0% |
| Black | 352 | 43.8% |
| Unknown | 1 | 0.1% |

### DeSoto Parish
**Total:** 122

| Race | Count | % |
|------|-------|---|
| Black | 70 | 57.4% |
| White | 51 | 41.8% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,318

| Race | Count | % |
|------|-------|---|
| Black | 1,045 | 79.3% |
| White | 207 | 15.7% |
| Unknown | 65 | 4.9% |
| Asian/PacificIslander | 1 | 0.1% |

### East Feliciana Parish
**Total:** 271

| Race | Count | % |
|------|-------|---|
| Black | 174 | 64.2% |
| White | 96 | 35.4% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 170

| Race | Count | % |
|------|-------|---|
| Black | 93 | 54.7% |
| White | 76 | 44.7% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 847

| Race | Count | % |
|------|-------|---|
| Black | 556 | 65.6% |
| White | 281 | 33.2% |
| Unknown | 10 | 1.2% |

### Hammond Police Department
**Total:** 14

| Race | Count | % |
|------|-------|---|
| Black | 11 | 78.6% |
| White | 2 | 14.3% |
| Unknown | 1 | 7.1% |

### Iberia Parish
**Total:** 465

| Race | Count | % |
|------|-------|---|
| Black | 268 | 57.6% |
| White | 186 | 40.0% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 32

| Race | Count | % |
|------|-------|---|
| White | 18 | 56.2% |
| Black | 14 | 43.8% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 161

| Race | Count | % |
|------|-------|---|
| White | 87 | 54.0% |
| Black | 70 | 43.5% |
| American Indian/Alaska Native | 3 | 1.9% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,125

| Race | Count | % |
|------|-------|---|
| Black | 727 | 64.6% |
| White | 391 | 34.8% |
| Unknown | 5 | 0.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 80

| Race | Count | % |
|------|-------|---|
| White | 52 | 65.0% |
| Black | 27 | 33.8% |
| Unknown | 1 | 1.2% |

### Lafayette Parish
**Total:** 843

| Race | Count | % |
|------|-------|---|
| Black | 550 | 65.2% |
| White | 278 | 33.0% |
| Unknown | 14 | 1.7% |
| Asian/PacificIslander | 1 | 0.1% |

### Lafourche Parish
**Total:** 761

| Race | Count | % |
|------|-------|---|
| Black | 390 | 51.2% |
| White | 367 | 48.2% |
| American Indian/Alaska Native | 3 | 0.4% |
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
| Black | 280 | 74.7% |
| White | 92 | 24.5% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 831

| Race | Count | % |
|------|-------|---|
| White | 586 | 70.5% |
| Black | 233 | 28.0% |
| Unknown | 10 | 1.2% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 143

| Race | Count | % |
|------|-------|---|
| Black | 116 | 81.1% |
| White | 26 | 18.2% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 218

| Race | Count | % |
|------|-------|---|
| Black | 154 | 70.6% |
| White | 64 | 29.4% |

### Natchitoches Parish
**Total:** 186

| Race | Count | % |
|------|-------|---|
| Black | 138 | 74.2% |
| White | 45 | 24.2% |
| Unknown | 3 | 1.6% |

### Oakdale Police Department
**Total:** 4

| Race | Count | % |
|------|-------|---|
| White | 3 | 75.0% |
| Black | 1 | 25.0% |

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
| Black | 871 | 66.5% |
| White | 425 | 32.4% |
| Unknown | 14 | 1.1% |

### Plaquemines Parish
**Total:** 688

| Race | Count | % |
|------|-------|---|
| Black | 443 | 64.4% |
| White | 218 | 31.7% |
| Unknown | 15 | 2.2% |
| Asian/PacificIslander | 8 | 1.2% |
| American Indian/Alaska Native | 4 | 0.6% |

### Pointe Coupee Parish
**Total:** 113

| Race | Count | % |
|------|-------|---|
| Black | 70 | 61.9% |
| White | 40 | 35.4% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,029

| Race | Count | % |
|------|-------|---|
| Black | 660 | 64.1% |
| White | 353 | 34.3% |
| Unknown | 14 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 44

| Race | Count | % |
|------|-------|---|
| White | 22 | 50.0% |
| Black | 21 | 47.7% |
| Asian/PacificIslander | 1 | 2.3% |

### Richland Parish
**Total:** 695

| Race | Count | % |
|------|-------|---|
| Black | 479 | 68.9% |
| White | 206 | 29.6% |
| Unknown | 6 | 0.9% |
| Asian/PacificIslander | 4 | 0.6% |

### Sabine Parish
**Total:** 199

| Race | Count | % |
|------|-------|---|
| White | 111 | 55.8% |
| Black | 85 | 42.7% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 40

| Race | Count | % |
|------|-------|---|
| Black | 29 | 72.5% |
| White | 11 | 27.5% |

### St. Bernard Parish
**Total:** 219

| Race | Count | % |
|------|-------|---|
| Black | 130 | 59.4% |
| White | 85 | 38.8% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 190

| Race | Count | % |
|------|-------|---|
| Unknown | 117 | 61.6% |
| White | 73 | 38.4% |

### St. Helena Parish
**Total:** 52

| Race | Count | % |
|------|-------|---|
| Black | 36 | 69.2% |
| White | 15 | 28.8% |
| Unknown | 1 | 1.9% |

### St. James Parish
**Total:** 69

| Race | Count | % |
|------|-------|---|
| Black | 57 | 82.6% |
| White | 12 | 17.4% |

### St. John the Baptist Parish
**Total:** 207

| Race | Count | % |
|------|-------|---|
| Unknown | 134 | 64.7% |
| White | 73 | 35.3% |

### St. Landry Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| Black | 85 | 65.9% |
| White | 42 | 32.6% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 214

| Race | Count | % |
|------|-------|---|
| Black | 111 | 51.9% |
| White | 93 | 43.5% |
| Unknown | 9 | 4.2% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 294

| Race | Count | % |
|------|-------|---|
| Black | 154 | 52.4% |
| White | 139 | 47.3% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 872

| Race | Count | % |
|------|-------|---|
| White | 460 | 52.8% |
| Black | 371 | 42.5% |
| Unknown | 38 | 4.4% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sulphur Police Department
**Total:** 20

| Race | Count | % |
|------|-------|---|
| White | 18 | 90.0% |
| Black | 2 | 10.0% |

### Tangipahoa Parish
**Total:** 672

| Race | Count | % |
|------|-------|---|
| Black | 437 | 65.0% |
| White | 234 | 34.8% |
| Unknown | 1 | 0.1% |

### Tensas Parish
**Total:** 572

| Race | Count | % |
|------|-------|---|
| Black | 380 | 66.4% |
| White | 180 | 31.5% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 543

| Race | Count | % |
|------|-------|---|
| Black | 298 | 54.9% |
| White | 233 | 42.9% |
| American Indian/Alaska Native | 10 | 1.8% |
| Unknown | 2 | 0.4% |

### Vermillion Parish
**Total:** 135

| Race | Count | % |
|------|-------|---|
| White | 67 | 49.6% |
| Black | 65 | 48.1% |
| Unknown | 2 | 1.5% |
| Asian/PacificIslander | 1 | 0.7% |

### Vernon Parish
**Total:** 168

| Race | Count | % |
|------|-------|---|
| White | 118 | 70.2% |
| Black | 48 | 28.6% |
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
**Total:** 199

| Race | Count | % |
|------|-------|---|
| White | 100 | 50.3% |
| Black | 99 | 49.7% |

### Webster Parish
**Total:** 448

| Race | Count | % |
|------|-------|---|
| Black | 240 | 53.6% |
| White | 202 | 45.1% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 128

| Race | Count | % |
|------|-------|---|
| Black | 87 | 68.0% |
| White | 35 | 27.3% |
| Unknown | 4 | 3.1% |
| Asian/PacificIslander | 2 | 1.6% |

### West Carroll Parish
**Total:** 30

| Race | Count | % |
|------|-------|---|
| White | 23 | 76.7% |
| Black | 7 | 23.3% |

### West Felician Parish
**Total:** 198

| Race | Count | % |
|------|-------|---|
| Black | 129 | 65.2% |
| White | 69 | 34.8% |

### Winn Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| Black | 78 | 51.7% |
| White | 73 | 48.3% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
