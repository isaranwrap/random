# Making my résumé in R

# library()
# > devtools::install_github("nstrayer/datadrivencv")
# Using github PAT from envvar GITHUB_PAT
# Error: Failed to install 'unknown package' from GitHub:
#   HTTP error 401.
# Bad credentials
#
# Rate limit remaining: 59/60
# Rate limit reset at: 2022-04-11 01:33:58 UTC
<<<<<<< HEAD

install.packages("devtools")
#devtools::install_github("nstrayer/datadrivencv")
library(datadrivencv)
#devtools::install_github("tidyverse/googlesheets4")
library(googlesheets4)


datadrivencv::use_datadriven_cv(
  full_name = "Ishan Saran",
  data_location = "https://docs.google.com/spreadsheets/d/1-wnLVEmF8TawSyaYPL_njfHp0lcrFBFxQTtTdoO87yE/edit?usp=sharing",
  pdf_location = "https://github.com/isaranwrap/random/resume.pdf",
  html_location = "https://github.com/isaranwrap/random/resume.html",
  source_location = "https://github.com/isaranwrap/"
)

# list.files()
=======
>>>>>>> 3391ea8... Added resume folder and creating data-driven resume with datadrivencv in R
