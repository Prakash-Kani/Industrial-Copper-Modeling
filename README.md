# Industrial Copper Modeling

___

## Problem Statement
___

The copper industry encounters challenges in handling sales and pricing data, which can be less straightforward due to issues like skewness and noise. Manual efforts to address these issues are time-consuming and may not lead to optimal pricing decisions. Implementing a machine learning regression model with techniques like data normalization and outlier detection can improve accuracy. Additionally, capturing leads poses a challenge, and a lead classification model is needed to evaluate and classify leads based on their likelihood to become customers. Utilizing the STATUS variable, where WON is success and LOST is failure, and removing other STATUS values can streamline this process.

## Data Preprocessing:
___

### 1. Understanding the Data:

- Before starting the modeling process, it's important to thoroughly understand the dataset.
- Identify the types of variables, like whether they are numbers or categories, and see how they are spread out.
- Check for 'Material_Ref' values starting with '00000.' Convert these to null for better data quality.

### 2. Handling Missing Values:

- Deal with any missing values in the dataset.
- Decide whether to fill in missing values using the average, middle, or most common value, depending on the data and feature.

### 3. Encoding and Type Conversion:

- Get categorical features ready for modeling by using ordinal encoding.
- Change data types as needed to match the requirements for modeling.

### 4. Addressing Skewness and Feature Scaling:

- Skewness, or lopsidedness in the data, is common. Identify and handle it.
- Use methods like log transformation to balance and normalize continuous variables.
- This step is important for many machine learning methods.

### 5. Dealing with Outliers:

- Outliers, or unusual values, can affect the accuracy of the model.
- Use the Interquartile Range (IQR) method to find and adjust extreme values.
- This helps create a stronger and more accurate model.

### 6. Correcting Wrong Dates:

- If there are delivery dates that come before item dates, fix this by calculating the difference.
- Train a Random Forest Regressor model to predict the corrected delivery date.
- This ensures our dataset stays accurate and reliable.

## Exploratory Data Analysis (EDA) and Feature Engineering:

### 1. Making Data More Even:

- We use Seaborn's Histplot and Violinplot to look at our data's shape and make it more even.
- Applying the Log Transformation method helps balance and spread out our data better, keeping it reliable.

### 2. Spotting and Fixing Outliers:

- Seaborn's Boxplot helps us find and fix outliers, which are unusual values in our data.
- We use the Interquartile Range (IQR) method to bring outlier values in line with the rest of the data, making it stronger.

### 3. Making Features Better:

- Our goal is to improve our dataset for better modeling.
- We create new features to get more useful information from the data and make it work more efficiently.
- Checking correlations with Seaborn's Heatmap shows that no columns are strongly linked, ensuring good data quality, and we don't need to remove any columns.

## Classification:
___

**1. Sorting Success and Failure:**
   - We use the 'status' variable, marking 'Won' as Success and 'Lost' as Failure.
   - Data points with status values other than 'Won' and 'Lost' are left out to focus on the main classification task.

**2. Picking the Right Algorithm:**
   - After careful checking, two good choices emerge: Extra Trees Classifier and Random Forest Classifier.
   - Both show good accuracy without getting too specific to the training data.
   - I go with the Extra Trees Classifier because it balances being easy to understand and accurate.

**3. Tweaking for Best Results:**
   - To make sure our model is just right, we use GridSearchCV with cross-validation to tweak its settings.
   - The best settings turn out to be ```{'bootstrap': False, 'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 200}```.

**4. Checking How Good Our Model Is:**
   - With these settings, our Extra Trees Classifier is really accurate, hitting 97.12%.
   - We look at other measures like confusion matrix, precision, recall, F1-score, AUC, and ROC curve to get a complete picture of how well it's doing.

**5. Saving Our Model:**
   - To make things easy for the future, we save our well-trained model to a pickle file.
   - This way, we can load the model whenever we want and make predictions on the status without any fuss.


### Regression:

**1. Finding the Right Algorithm:**
   - In regression, our main goal is predicting the selling price, a continuous variable.
   - We split our data into training and testing parts and try out different algorithms.
   - We use the R2 (R-squared) metric to see how well each algorithm fits our data.

**2. Picking the Best Algorithm:**
   - After testing, we see two good options: Extra Trees Regressor and Random Forest Regressor.
   - Both work well without getting too specific to our training data.
   - I go with the  Extra Trees Regressor because it balances being easy to understand and accurate.

**3. Making Sure It's Just Right:**
   - To fine-tune our model and make sure it's not too focused on the training data, we use RandomizedSearchCV with cross-validation.
   - The best settings turn out to be ```{'bootstrap': False, 'max_depth': 30, 'max_features': 'sqrt', 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 197}```.

**4. Checking How Good Our Model Is:**
   - With these settings, our  Extra Trees Regressor is really accurate, hitting 95.8%.
   - We look at other measures like mean absolute error, mean squared error, root mean squared error, and R-squared to get a complete picture of how well it's doing.

**5. Saving Our Model:**
   - To make things easy for the future, we save our well-trained model to a pickle file.
   - This way, we can load the model whenever we want and predict selling prices without any fuss.


# Getting Started
___

To begin working with the Business Card Data Extraction project, follow these simple steps:

1. **Clone the Repository:**
   - Start by copying this project from GitHub to your computer. Just type the following command:
     ```
     git clone https://github.com/Prakash-Kani/Industrial-Copper-Modeling.git
     ```

2. **Install the Required Packages:**
   - Make sure you have all the necessary tools installed. Do this by typing the following command:
     ```
     pip install -r requirements.txt
     ```

3. **Run the Streamlit App:**
   - Fire up the Streamlit application using this command:
     ```
     streamlit run app.py
     ```

4. **Access the App in Your Browser:**
   - Open your internet browser and go to http://localhost:8501. You should see the app there.

Now you're all set! You've got the project on your machine, installed what you need, and can access the app in your browser. Happy exploring!


