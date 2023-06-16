# Crimes and Nuisance Exploratory Data Analysis Report
- Panna

---

As part of my assigned responsibilities, I have been entrusted with the task of collecting, cleaning, and processing data on crimes and nuisances. The data has been sourced from openly available platform, from the official website of the police department (https://www.politie.nl). My primary role entailed conducting an Exploratory Data Analysis (EDA) on the gathered data to uncover valuable insights related to crimes and nuisances.
The insights derived from this analysis can contribute to a better understanding of the factors influencing crime rates and the prevalence of nuisances within a given area. This knowledge can aid in informed decision-making processes, enabling the development of effective strategies to address and mitigate these issues. Additionally, the findings can support the development of policies and initiatives aimed at creating safer and more liveable Breda. 
First of all, I dived into this topic due to the high number of crime incidents registered last year. (11K) This data highlights a clear need for improvement, prompting us to take immediate and effective actions to address this pressing matter.

![imgur](https://i.imgur.com/pGp2iLK.png)

During the initial phase of my analysis, I focused on examining the registered crimes by type. By analysing the data, I identified specific types of crimes that require heightened attention due to their significant occurrence. The top five crime categories that stood out in terms of frequency were road accidents, horizontal fraud, theft of bikes and models, other property crimes, and destruction or property damage.

![Imgur](https://i.imgur.com/Si9S5sx.png)

Among these categories, bike theft, in particular, caught my attention as it influences most of my friends, peers and mentors. To gain further insights into this issue, I decided to delve deeper into the data related to bike theft. By conducting a more detailed analysis, I aimed to propose ideas and recommendations to the municipality that could help mitigate this problem.

## I have identified the neighbourhoods with the highest risks associated with bike theft. Based on these findings, I have developed the following professional recommendations:
1.	Integration of GPS Tracking System: It is highly recommended to integrate GPS tracking systems into mopeds and bicycles to enable real-time monitoring. This can be achieved by creating a dedicated mobile application that allows users to track the precise location of their vehicles. Implementing such a system will significantly enhance security measures.
2.	Establishment of Secure Parking Zones: To mitigate the risks of bike theft, it is essential to establish designated parking areas equipped with robust security measures. These measures should include the installation of surveillance cameras, ensuring well-lit spaces, and implementing secure locking mechanisms. Collaborating with insurance companies will provide additional support and comprehensive coverage for these initiatives.
3.	Utilization of Data Analytics and Predictive Modelling: Leveraging advanced data analytics and predictive modelling techniques, it is possible to accurately identify high-risk areas in Breda that are particularly susceptible to bike theft. Utilizing this information, law enforcement agencies can increase their presence in these identified areas, conducting more frequent patrols and implementing targeted surveillance efforts. This proactive approach will serve as a strong deterrent to potential thieves and significantly improve the likelihood of detecting and apprehending them in the act.

## By implementing these recommendations, we can effectively enhance the security measures for bicycles and mopeds, thereby reducing the incidence of bike theft in the identified high-risk neighbourhoods. 

![Imgur](https://i.imgur.com/D7m4Rey.png)

A noticeable trend has emerged, indicating an increasing number of theft incidents from August onwards. (it reaches the highest) The observed increase in theft incidents could potentially be linked to opportunistic behaviour capitalizing on the presence of newly arrived students in the area who may have limited familiarity with strategies for deterring thefts.

![Imgur](https://i.imgur.com/6lGGRQz.png)

Also, I examined correlations between different features with the hope that I find some relevant connection. (Correlation is a statistical concept that tells us how two things are related to each other. It measures the strength and direction of their connection. When there is a positive correlation, it means that when one thing goes up, the other tends to go up as well. In a negative correlation, one thing goes up while the other goes down. A correlation of zero means there is no apparent relationship between the two things. It's important to remember that correlation doesn't always mean causation – just because two things are correlated doesn't mean that one causes the other.) The strongest correlations primarily involved various types of crimes that are positively associated with each other but it is important to note that these relationships do not imply causation.

Upon further investigation, I wanted to see the level of illumination influences the number of bike thefts. (assuming that at nights if the area have more lights less common the crime occurs) However, the correlation between these factors was surprisingly low, indicating that the brightness of the area may not significantly influence the occurrence of such incidents. This insight underscores the need to explore alternative factors and strategies in order to effectively address bike theft and its contributing factors.

![Imgur](https://i.imgur.com/CRx4T0B.png)

A correlation of -0.32 between house prices and the total number of crimes suggests a moderate negative relationship. The number of crimes exhibits a significant impact on house prices, making it an influential feature. This is evident in the observed inverse relationship, where an increase in the number of crimes tends to lead to a decrease in house prices, and vice versa. However, it is crucial to acknowledge that this correlation does not establish a causal relationship. Other factors may also contribute to the dynamics between the number of crimes and house prices.

![Imgur](https://i.imgur.com/rkI5a2E.png)
![Imgur](https://i.imgur.com/gTL9swE.png)

# Nuisance

The plotted distribution of different nuisance types clearly reveals a significant distinction between the top two categories and the rest. This discrepancy highlights the need for heightened attention and focus on addressing these top two nuisance types.

![Imgur](https://i.imgur.com/Zpa6cvg.png)

I examined the variables with the lowest (minimum) correlations. These findings suggest that as the nuisance levels increase, there is a tendency for these specific features to decrease. However, it is important to note that correlation alone does not establish a causal relationship. While the observed correlations indicate an association, further investigation is required to determine the underlying factors and mechanisms driving these relationships.

![Imgur](https://i.imgur.com/Lmaqdzz.png)

Also, I have uncovered a substantial correlation between public intoxication and instances of abuse. The data analysis reveals a strong association between these two variables, indicating that a significant number of cases involving public intoxication are accompanied by incidents of abuse. 

![Imgur](https://i.imgur.com/hPJKfJ9.png)

