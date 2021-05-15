library(rvest)
library(dplyr)

link = "https://eu.usatoday.com/story/money/2019/06/19/beer-brands-americas-31-most-popular-beers/39490347/"
page = read_html(link)

name = page %>% html_nodes(".presto-h2 strong") %>% html_text()

brands = data.frame(name)

write.csv(brands, "Beerbrands.csv")