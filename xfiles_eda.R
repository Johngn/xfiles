library(tidyverse)

xfiles_episodes <- read_csv('./xfiles/xfiles_episodes_full.csv')

season1 <- subset(xfiles_episodes, season == 1 | season == 2)
season2 <- subset(xfiles_episodes, season == 2)
  
ggplot(season1) +
  geom_point(aes(x = airdate,
                 y = rating,
                 size = votes,
                 color = phenomena)) +
  labs(y = "",
       title = "IMDB ratings of seasons 1 and 2 of the X-files")

ggplot(xfiles_episodes) +
  geom_point(aes(x = number,
                 y = rating,
                 size = votes,
                 color = main_story)) +
  labs(x = "",
       y = "",
       title = "IMDB ratings for X-files per season") +
  facet_wrap(~ season)

xfiles_episodes %>%
  count(phenomena, sort = TRUE) %>%
  mutate(phenomena = fct_reorder(phenomena, n)) %>%
  ggplot(aes(n, phenomena)) +
  labs(x = "",
       y = "",
       title = "Frequency of each type of phenomena in X-files episodes") +
  geom_col()
