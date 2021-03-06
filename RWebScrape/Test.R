library(rvest)
library(dplyr)

link = "https://en.wikipedia.org/wiki/Category:Luxury_brands"
page = read_html(link)


name = page %>% html_nodes("#mw-pages a , #mw-subcategories a") %>% html_text()
industry = page %>% html_nodes("#mw-pages a , #mw-subcategories a") %>%
  html_attr("href") %>% paste("https://en.wikipedia.org", ., sep="")


get_industry = function(industry) {
  industry = "https://en.wikipedia.org/wiki/Fiorucci"
  indsutry_page = read_html(industry)
  industry_title = industry_page %>% html_nodes(".category , .org") %>%  html_text()
}