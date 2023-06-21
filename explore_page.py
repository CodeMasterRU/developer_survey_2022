import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def filter_categories(categories, cut):
    categories_map = {}
    for i in range (len(categories)):
        if categories.values[i] >= cut:
            categories_map[categories.index[i]] = categories.index[i]
        else:
            categories_map[categories.index[i]] = "Other"
    return categories_map

def filter_experience(x):
    if x == 'Less than 1 year':
        return 0.5
    if x == 'More than 50 years':
        return 51
    return float(x)

def filter_education(x):
    if "Master’s degree" in x:
        return "Master’s degree"
    if "Bachelor’s degree" in x:
        return "Bachelor’s degree"
    if "Professional degree" in x or "Other doctoral" in x:
        return "Doctorat"
    return "Less than a Bachelors"

@st.cache_data
def load_data():
    df = pd.read_csv("./survey_results_public.csv")
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearly"]]  
    df = df.rename({"ConvertedCompYearly" : "Salary"}, axis=1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed, full-time"]
    df = df.drop("Employment", axis=1)
    country_map = filter_categories(df["Country"].value_counts(), 400)
    df["Country"] = df["Country"].map(country_map)
    df = df[df['Salary'] <= 300000]
    df = df[df['Salary'] >= 10000]
    df = df[df['Country'] != 'Other']
    df["YearsCodePro"] = df["YearsCodePro"].apply(filter_experience)
    df["EdLevel"] = df["EdLevel"].apply(filter_education)
    return df

df = load_data()

def show_explore_page():
    st.title("Explore Software Engineer Salaries")

    st.write("### Stack Overflow Developer Survey 2020")

    data = df["Country"].value_counts()

    fig1, ax1 = plt.subplots(figsize=(9, 9))
    ax1.pie(data, labels = data.index, autopct="%1.1f%%", shadow = True, startangle = 90)
    ax1.axis("equal")

    st.write("""### Number of Data from different countries""")

    st.pyplot(fig1)

    st.write("\n")

    st.write("### Mean salary based on Country")

    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    

    