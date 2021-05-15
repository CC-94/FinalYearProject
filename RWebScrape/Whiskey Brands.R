library(rvest)
library(dplyr)

link = "https://brandirectory.com/rankings/tobacco/2017/table"
page = read_html(link)

name = page %>% html_nodes(".tight-text") %>% html_text()

brands = data.frame(name)

write.csv(brands, "Tobaccobrands.csv")