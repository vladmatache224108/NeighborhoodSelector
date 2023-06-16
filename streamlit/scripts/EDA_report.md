## Correlation analysis
After examining the correlations between different columns, no unusual pattern emerged.
The highest correlations consisted mostly of different types of crimes correlating with each other.
Additionally, crimes produce higher correlations with the number of neighborhood inhabitants.
However, despite high correlations, no real causation was found.

Fortunately, some patterns were found after creating visuals

### Proximity score analysis
Using the proximity data, a proximity score was created. It consists of 
the average number of childcare, education, health and well-being,
hospitality and retail faciliites within 3km for each neighborhood.

![imgur](https://i.imgur.com/EyMSUdq.png)

However, the proximity score falls off drasticaly as the distance from the city centre increases.

![imgur](https://i.imgur.com/wVnbcdK.png)

### Distance from the centre analysis
Distance from centre was created by calculating the centre of each neighborhood polygon and checking
the distance from the City neighborhood.

![imgur](https://i.imgur.com/JYGw4BV.png)

The green score has a pretty strong correlation (Spearman method: 0.679) 
with the distance from the city centre.
It seems like the green score gets lower, the closer we get to the centre.

Livability score also seems to follow that pattern. The closer to the centre,
the lower the livability score.

![imgur](https://i.imgur.com/DuwCYGd.png)

As expected, the density (inhabitants / area km<sup>2</sup>) drops down with the increasing distance from the centre.

![imgur](https://i.imgur.com/sWtKr8Z.png)

### Standing out neighborhood analysis
During the EDA process, one neighborhood has been identified to have nuisance statistics
similar to the city centre, yet not being close to it. Further investigation showed that Kesteren is not big nor dense and does not have a lot of inhabitants, yet its total nuisance count is almost as high as in the centre (neighborhood with the highest nuisance).

![imgur](https://i.imgur.com/i3mpD4X.png)

![imgur](https://i.imgur.com/lW4vkZe.png)

The Kesteren neighborhood also sticks out when it comes to nuisance by confused person.



![imgur](https://i.imgur.com/H56qnbW.png)

Nuisance by confused person might be more important than just a standalone
statistic since it has a pretty strong spearman correlation (-0.568) with house prices.

### House prices analysis
The analysis shows that there are not enough useful features in the gathered dataset to reliably predict
house prices for each neighborhood.
However there are patterns regarding some singular features.

The plot below suggests that the house price might be influenced by the amount of nuisance caused by confused person.

![imgur](https://i.imgur.com/yW8zgAf.png)