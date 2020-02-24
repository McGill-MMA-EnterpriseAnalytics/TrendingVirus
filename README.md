# Project's motivation

Our team decided to dive deep into various features that may act as crucial in determining as to who can be strongly  or moderately impacted by the MERS Coronavirus.

The current state in the healthcare industry is problematic; it is difficult to lower the risk of contagion if vulnerable people are not identified beforehand.
The ideal state with our model will be to predict beforehand the risk of fatality for each individual.


# Our initial assumptions
Localization, gender, age, a job as healthcare worker and environement are variables which might determine the fatality of an individual towards the MERS Coronavirus.

# Data Preprocessing
Our data set was not clean and we add to follow theses steps before using it.
1. Data Formatting
2. Date Difference column added
3. Blanks columns replaced with NA
4. Dummification using Label Encoder
5. Standardization of Data
6. Balancing the data

# Data exploration
Please have a look on the folder named "Data exploration"

# Feature extraction
Please have a look on the folder named "Feature Selection".
This step was done to help our choices of variables in our Stacking ensenble model.

# Models 
Please have a look on the folder named "Models".
We build two different classification model, to predict the survival rate of a given individual if exposed to the virus.
Our best model was the AutoML_h2o.

# Causal Inference
Please have a look on the folder named "Causal Inference".
Since our causal Estimate is -0.16964848600630436; we can sate that:
As the age increases, the probability of survival decreases.


# Conclusion
Our model help us validate our initial assumption about the age. Indeed, we learned that the likelihood to get severely infected with the virus is high for young people and old people.

Our hope is that people can look at our model and utilize it to predict the probability of fatality of the recent outbreak of Coronavirus we witnessed in early 2020.

# Limits
Our data was imbalanced, we have more people surviving the virus than people dying because of it.
So, further techniques of data augmentation could be explored with our best model.

# Team members
Karun Prashant Bhasin <br>
Blessy Prackuzhy <br>
Bhavvyya Malhotra <br>
Katia Sory <br>
