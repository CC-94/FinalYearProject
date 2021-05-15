shapiro.test(Data$Male)
shapiro.test(Data$Female)

hist(Data$Male,
     main="Brand Mentions by Male Artists",
     xlab="Number of mentions",
     xlim=c(0,250),
     col="darkmagenta",
     freq=FALSE
)
hist(Data$Female,
     main="Brand Mentions by Female Artists",
     xlab="Number of mentions",
     xlim=c(0,140),
     col="darkblue",
     freq=FALSE
)

t.test(Data$Male, Data$Female)
