import streamlit as st
import datetime as dt
import numpy as np
from scipy.stats import boxcox
import pickle

def regression(test_data):
    with open('regression_model.pkl', 'rb' ) as file:
        model = pickle.load(file)
        data = np.exp(model.predict(test_data))

        return data

def classification(test_data):
    with open('classification_model.pkl', 'rb' ) as file:
        model = pickle.load(file)
        data = model.predict(test_data)
        if data == 1.0:
          return 'Won'
        else:
          return 'Lost'

item_type_value = {'W': 5.0, 'S': 3.0, 'Others': 1.0, 'PL': 2.0, 'WI': 6.0, 'IPL': 0.0, 'SLAWR': 4.0}

status_values = {'Won': 7.0, 'Draft': 0.0, 'To be approved': 6.0, 
                'Lost': 1.0, 'Not lost for AM': 2.0, 'Wonderful': 8.0,
                'Revised': 5.0, 'Offered': 4.0, 'Offerable': 3.0}

classification_status = {'Won': 1.0, 'Lost': 0.0}

application_code = [10., 41., 28., 59., 15.,  4., 38., 56., 42., 26., 27., 19., 20.,
                66., 29., 22., 40., 25., 67., 79.,  3., 99.,  2.,  5., 39., 69.,
                70., 65., 58., 68.]

country_code = [ 28.,  25.,  30.,  32.,  38.,  78.,  27.,  77., 113.,  79.,  26.,
                 39.,  40.,  84.,  80., 107.,  89.]



st.set_page_config(page_title = "Industrial Copper Modeling Prediction",
                   page_icon = "",
                   layout = "wide",
                   initial_sidebar_state = "expanded",
                   menu_items = None)

st.title(":red[Industrial] :blue[Copper] :orange[Modeling]")
tab1, tab2 = st.tabs(['***Regression***','***Classification***'])

with tab1:
  col1, col2 = st.columns(2, gap= 'large')

  with col1:
    item_date = st.date_input("Select the **Item Date**", dt.date(2020, 7,2), min_value= dt.date(2020, 7,2), max_value= dt.date(2021, 4,1))

    quantity_tons = st.number_input('Enter the **Quantity Tons**', min_value = 1e-05, max_value= 1000000000.0, value = 5874.904 )

    customer = st.number_input('Enter the **Customer**', min_value = 12458.0, max_value= 2147483647.0, value = 30512207.0 )

    status = st.selectbox('Select The **Status**', status_values)

    item_type =  st.selectbox('Select The **Item Type**', item_type_value)

    application = st.selectbox('Select The **Application**', application_code)

  with col2:

    country = st.selectbox('Select the **Country**', country_code)

    thickness = st.number_input('Enter the **Thickness**', min_value = 0.18, max_value= 2500.0, value = 2.56482 )

    width = st.number_input('Enter the **Width**', min_value = 700.0, max_value= 1980.0, value = 1297.0455 )

    product_ref = st.number_input('Enter the **Product Reference**', min_value = 611728.0, max_value= 1722207590.0, value = 473967910.72 )

    delivery_date= st.date_input("Select the **Delivery Date**", dt.date(2019, 4,1), min_value= dt.date(2019, 4,1), max_value= dt.date(2022, 1,1))

    st.markdown('Click below button to predict the **Selling Price**')
    prediction = st.button('**Predict**')

day_difference = item_date - delivery_date
transform = np.array([quantity_tons, thickness])
transformed_data, lambda_value = boxcox(transform)
test_data =[[quantity_tons, customer,  status_values[status], item_type_value[item_type], application, country, thickness, width, product_ref, 
            transformed_data[0], transformed_data[1], day_difference.days, item_date.day, item_date.month, item_date.year,
            delivery_date.day, delivery_date.month, delivery_date.year]]

if prediction and test_data:
  st.markdown(f"### :bule[Selling Price :] :green[$ {round(regression(test_data)[0],3)}]")

with tab2:
  col3, col4 = st.columns(2, gap= 'large')

  with col3:
    item_date1 = st.date_input(" Select the **Item Date**", dt.date(2020, 7,2), min_value= dt.date(2020, 7,2), max_value= dt.date(2021, 4,1))

    quantity_tons1 = st.number_input(' Enter the **Quantity Tons**', min_value = 1e-05, max_value= 1000000000.0, value = 5874.904 )

    customer1 = st.number_input(' Enter the **Customer**', min_value = 12458.0, max_value= 2147483647.0, value = 30512207.0 )

    item_type1 =  st.selectbox(' Select The **Item Type**', item_type_value)

    application1 = st.selectbox(' Select The **Application**', application_code)

    country1 = st.selectbox(' Select the **Country**', country_code)

  with col4:

    thickness1 = st.number_input(' Enter the **Thickness**', min_value = 0.18, max_value= 2500.0, value = 2.56482 )

    width1 = st.number_input(' Enter the **Width**', min_value = 700.0, max_value= 1980.0, value = 1297.0455 )

    product_ref1 = st.number_input(' Enter the **Product Reference**', min_value = 611728.0, max_value= 1722207590.0, value = 473967910.72 )

    selling_price = st.number_input(' Enter the **Selling Price**',  max_value= 100001015.0, value = 1918.06 )

    delivery_date1 = st.date_input(" Select the **Delivery Date**", dt.date(2019, 4,1), min_value= dt.date(2019, 4,1), max_value= dt.date(2022, 1,1))

    st.markdown('Click below button to predict the **Status**')
    prediction1 = st.button('**Predict The Status**')

day_difference1 = item_date1 - delivery_date1
transform = np.array([quantity_tons1, thickness1])
transformed_data, lambda_value = boxcox(transform)
test_data1 =[[quantity_tons1, customer1, item_type_value[item_type1], application1, country1, thickness1, width1, product_ref1, selling_price,
            np.log1p(selling_price), transformed_data[0], transformed_data[1], day_difference1.days, item_date1.day, item_date1.month, 
            item_date1.year, delivery_date1.day, delivery_date1.month, delivery_date1.year]]

if prediction1 and test_data1:
  st.markdown(f"### :bule[Status :] :green[ {classification(test_data1)}]")