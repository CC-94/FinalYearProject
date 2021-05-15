cor(Correlation$Count, Correlation$`Trends Data`)

x <- Correlation$Count
y <- Correlation$`Trends Data`

library(car)
plot(x, y, main = "Brand Mention + Google Trends Correlation",
     xlab = "Mentions", ylab = "Google Trends Data",
     pch = 19, frame = FALSE)


plot(x, y, main = "Brand Mention + Google Trends Correlation",
     xlab = "Mentions", ylab = "Google Trends Data",
     pch = 19, frame = FALSE)
abline(lm(y ~ x, data = mtcars), col = "blue")