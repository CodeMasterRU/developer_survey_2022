import streamlit as st
import pickle
import numpy as np
# import sklearn
# import plotly.graph_objects as go

def load_model(): 
    with open('saved_model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()

regressor = data["model"]
lab_country = data["lab_country"]
lab_education = data["lab_education"]

def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some information to predict the salary""")

    countries = [
        "United States of America",
        "India",
        "United Kingdom of Great Britain and Northern Ireland",   
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    ]
    # countries_numpy = np.array(countries)   
    # countries = (
    #     "USA",
    #     "IND",
    #     "GBR",
    #     "DEU",
    #     "CAN",
    #     "BRA",
    #     "FRA",
    #     "ESP",
    #     "AUS",
    #     "NLD",
    #     "POL",
    #     "ITA",
    #     "RUS",
    #     "SWE",
    # )

    educations = (
        "Less than a Bachelors", 
        "Bachelor’s degree",
        "Master’s degree",
        "Doctorat",
    )

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education level", educations)

    experience = st.slider("Years of Experience", 0, 30, 3)


    ok = st.button("Calculate Salary")
    if ok:
        X = np.array([[country, education, experience]])
        X[:, 0] = lab_country.transform(X[:,0])
        X[:, 1] = lab_education.transform(X[:,1])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")

    # data = go.Choropleth(
    #     locations=country,
    #     # z=salary,
    #     locationmode="country names",
    #     colorscale="YlOrRd",
    # )

    # layout = go.Layout(geo=dict(showframe=False, projection_type="natural earth"))

    # fig = go.Figure(data=[data], layout=layout)

    # fig.show()