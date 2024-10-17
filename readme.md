training set adult.data
evaluation set adult.test

| Variable Name  | Role    | Type        | Demographic     | Description                                                  | Units | Missing Values |
| -------------- | ------- | ----------- | --------------- | ------------------------------------------------------------ | ----- | -------------- |
| age            | Feature | Integer     | Age             | N/A                                                          |       | no             |
| workclass      | Feature | Categorical | Income          | Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked. |       | yes            |
| fnlwgt         | Feature | Integer     |                 |                                                              |       | no             |
| education      | Feature | Categorical | Education Level | Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool. |       | no             |
| education-num  | Feature | Integer     | Education Level |                                                              |       | no             |
| marital-status | Feature | Categorical | Other           | Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse. |       | no             |
| occupation     | Feature | Categorical | Other           | Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces. |       | yes            |
| relationship   | Feature | Categorical | Other           | Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried. |       | no             |
| race           | Feature | Categorical | Race            | White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black. |       | no             |
| sex            | Feature | Binary      | Sex             | Female, Male.                                                |       | no             |
| capital-gain   | Feature | Integer     |                 |                                                              |       | no             |
| capital-loss   | Feature | Integer     |                 |                                                              |       | no             |
| hours-per-week | Feature | Integer     |                 |                                                              |       | no             |
| native-country | Feature | Categorical | Other           | United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands. |       | yes            |
| income         | Target  | Binary      | Income          | >50K, <=50K.                                                 |       | no             |





| Variable Name  | Role    | Type        | Demographic     | Description                                                  | Units | Missing Values |
| -------------- | ------- | ----------- | --------------- | ------------------------------------------------------------ | ----- | -------------- |
| age            | Feature | Integer     | Age             | N/A                                                          |       | no             |
| workclass      | Feature | Categorical | Income          | Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked. |       | yes            |
| fnlwgt         | Feature | Integer     |                 |                                                              |       | no             |
| education      | Feature | Categorical | Education Level | Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool. |       | no             |
| education-num  | Feature | Integer     | Education Level |                                                              |       | no             |
| marital-status | Feature | Categorical | Other           | Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse. |       | no             |
| occupation     | Feature | Categorical | Other           | Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces. |       | yes            |
| relationship   | Feature | Categorical | Other           | Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried. |       | no             |
| race           | Feature | Categorical | Race            | White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black. |       | no             |
| sex            | Feature | Binary      | Sex             | Female, Male.                                                |       | no             |
| capital-gain   | Feature | Integer     |                 |                                                              |       | no             |
| capital-loss   | Feature | Integer     |                 |                                                              |       | no             |
| hours-per-week | Feature | Integer     |                 |                                                              |       | no             |
| income         | Target  | Binary      | Income          | >50K, <=50K.                                                 |       | no             |