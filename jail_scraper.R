library(rvest)
library(pdftools)
library(dplyr)
library(stringr)
library(readr)
library(furrr)

plan(multisession, workers = parallel::detectCores() - 1)

parishes <- c(
  "Acadia", "Allen", "Ascension", "Assumption", "Avoyelles", "Beauregard",
  "Bienville", "Bossier", "Caddo", "Calcasieu", "Caldwell", "Cameron",
  "Catahoula", "Claiborne", "Concordia", "De Soto", "East Baton Rouge",
  "East Feliciana", "Evangeline", "Franklin", "Iberia", "Iberville",
  "Jackson", "Jefferson", "Jefferson Davis", "LaSalle", "Lafayette",
  "Lafourche", "Lincoln", "Livingston", "Madison", "Morehouse",
  "Natchitoches", "Orleans", "Ouachita", "Plaquemines", "Pointe Coupee",
  "Rapides", "Red River", "Richland", "Sabine", "St. Bernard", "St. Charles",
  "St. Helena", "St. James", "St. John the Baptist", "St. Landry",
  "St. Martin", "St. Mary", "St. Tammany", "Tangipahoa", "Tensas",
  "Vermilion", "Vernon", "Washington", "Webster", "West Baton Rouge",
  "West Carroll", "West Feliciana", "Winn"
)

pattern <- "^(.+?)\\s+(\\d{2}/\\d{2}/\\d{4})\\s+(.+?)\\s+(Male|Female)(?:\\s+(\\d{2}/\\d{2}/\\d{4}))?$"

parse_pdf <- function(url, parish, pattern, i, n) {
  cat(sprintf("  [%d/%d] %s\n", i, n, url))
  tryCatch({
    lines <- pdftools::pdf_text(url) |>
      paste(collapse = "\n") |>
      stringr::str_split("\n") |>
      unlist() |>
      stringr::str_trim() |>
      (\(x) x[nchar(x) > 0])()
    dplyr::mutate(
      dplyr::select(
        as.data.frame(stringr::str_match(
          lines[stringr::str_detect(lines, pattern)], pattern
        )),
        name = V2, dob = V3, race = V4, gender = V5, arrest_date = V6
      ),
      dob         = as.Date(dob,         format = "%m/%d/%Y"),
      arrest_date = as.Date(arrest_date, format = "%m/%d/%Y"),
      parish      = parish,
      roster_date = as.Date(stringr::str_extract(url, "\\d{4}-\\d{2}-\\d{2}"))
    )
  }, error = function(e) NULL)
}

dir.create("rosters", showWarnings = FALSE)
already_done <- gsub("\\.csv$", "", list.files("rosters"))

for (parish in parishes) {
  if (parish %in% already_done) { cat("Skipping (already done):", parish, "\n"); next }
  cat("Parish:", parish, "\n")

  hrefs <- tryCatch(
    rvest::read_html(paste0("https://jailrosters.org/la/", URLencode(parish, reserved = TRUE), "/")) |>
      rvest::html_elements("li a") |>
      rvest::html_attr("href"),
    error = function(e) { cat("  PAGE ERROR:", e$message, "\n"); character(0) }
  )

  pdf_paths <- stringr::str_extract(hrefs, "(?<=pdf=).+")
  pdf_paths <- pdf_paths[!is.na(pdf_paths)]
  pdf_urls  <- paste0("https://jailrosters.org/la/", URLencode(pdf_paths, repeated = TRUE))
  n <- length(pdf_urls)

  if (n == 0) { cat("  No PDFs found\n"); next }

  df <- future_map_dfr(seq_along(pdf_urls), function(i) {
    parse_pdf(pdf_urls[[i]], parish = parish, pattern = pattern, i = i, n = n)
  }, .options = furrr_options(seed = NULL))

  if (nrow(df) > 0) {
    write_csv(df, paste0("rosters/", parish, ".csv"), na = "")
    cat("  Saved", nrow(df), "rows\n")
  }
}

all_rosters <- list.files("rosters", full.names = TRUE) |>
  lapply(read_csv, show_col_types = FALSE) |>
  bind_rows()

write_csv(all_rosters, "la_all_rosters.csv", na = "")
