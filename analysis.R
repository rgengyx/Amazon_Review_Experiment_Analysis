# RM 2-way ANOVA
model <- aov(Rating ~ 
               verified * authenticity + Error(userId), 
             data = df)

#view the model output
summary(model)

#calculate Eta Squared using the effectsize package
effectsize::eta_squared(model)

# Posthoc: Effect of authenticity at each level verified
pairwise.t.test(x=df$Rating, g=df$authenticity, p.adj="bonf")

# Simple effect: Pairwise comparisons t-test between authenticity points
pwc <- df %>%
  group_by(verified) %>%
  pairwise_t_test(
    Rating ~ authenticity, paired = TRUE,
    p.adjust.method = "bonferroni"
  )
pwc

# calculate effect size t tests cohen's d (example with only a pair)
cohensD(df[df$verified==1 &
                  df$authenticity==1,]$Rating, 
        df[df$verified==1 &
                  df$authenticity== 0,]$Rating)
# plot the interaction
interaction.plot(x.factor     = df$authenticity,
                 trace.factor = df$verified,
                 response     = df$Rating,
                 fun = mean,
                 type="b",
                 col=c("black","red"),  ### Colors for levels of trace var.
                 pch=c(19, 17),             ### Symbols for levels of trace var.
                 fixed=TRUE,                    ### Order by factor order in data
                 leg.bty = "o",
                 trace.label = "Verified",
                 ylab = "Helpfulness",
                 xlab = "Authenticity")
