data = read.csv("/usagers3/padal/Doc/Cours/inf8775/tp1/algo/output.csv", sep="\t", header=FALSE, dec=".")
data$V2 = 2^data$V2


conv = subset(data, V1 %in% "conv")
strassen = subset(data, V1 %in% "strassen")

#conv = subset(conv, 8 < V2)
strassen = subset(strassen, 8 < V2)

regConv = lm(log(conv$V3)~log(conv$V2))
regStrassen = lm(log(strassen$V3)~log(strassen$V2))

#Test de puissance
#plot(log(conv$V3)~log(conv$V2))
#abline(regConv, untf=F)

#plot(log(strassen$V3)~log(strassen$V2))
#abline(regStrassen, untf=F)

#plot(seq(0, 30, 0.1), exp(regConv$coefficients[1] + regConv$coefficients[2] * seq(0, 30, 0.1)))
#points(seq(0, 30, 0.1), exp(regStrassen$coefficients[1] + regStrassen$coefficients[2] * seq(0, 30, 0.1)))
#- (regConv$coefficients[1] - regStrassen$coefficients[1]) / (regConv$coefficients[2] - regStrassen$coefficients[2])

#Test de rapport
plot(conv$V2, conv$V3 / (conv$V2^3))


#Test de constante
plot(conv$V2^3, conv$V3)
regConstantConv = lm(conv$V2^3 ~ conv$V3)
abline(regConstantConv)

#plot(strassen$V2^3, strassen$V3)
#regConstantStrassen = lm(strassen$V3 ~ strassen$V2^3)
#abline(regConstantStrassen)
