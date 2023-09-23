import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as sc
import matplotlib.pyplot as plt



st.set_page_config(page_title="Z Test")
st.title("Z Test Hypothesis Testing ")
st.header("Population Data set of School")
dataset  = pd.read_csv("new_dataset.csv")
exp1 = st.expander("Population Dataset")
exp1.dataframe(dataset)

exp2 = st.expander("Graph")
sns.kdeplot(x = "Test Score",data=dataset)
plt.title("Population data set distribution")
exp2.pyplot(plt.gcf())


with st.sidebar :
        mean = dataset["Test Score"].mean()
        st.subheader(f"Original Population Mean :  {round(mean,2)}")
        Population_mean = st.text_input("Almost Population Mean")
        Population_std = dataset["Test Score"].std()
        st.subheader(f"Original Population Std. :  {round(Population_std,2)}")
        n_sample = st.text_input("Number of Sample")
        area = st.text_input("Alternative (H1) Hypothesis Area")

        button1 = st.button("Done")
        if button1 :
            sample = []
            index = []
            for i in range(int(n_sample)):
                inx = np.random.randint(0, 999)
                index.append(inx)
                sample.append(dataset["Test Score"][inx])
            sample_dataset = pd.DataFrame({"Index": index, "Sample Test": sample})
            sample_dataset = sample_dataset.drop_duplicates(subset=["Index"])
            no_sample = sample_dataset.shape[0]

            st.subheader(f"Sample Data Without Duplicates :  {no_sample}")
            sample_mean = sample_dataset["Sample Test"].mean()
            st.subheader(f"Sample Data Mean :  {round(sample_mean, 2)}")

            z_test = (sample_mean - float(Population_mean)) / (Population_std / np.sqrt(no_sample))
            st.subheader(f"Z test Calculated :  {round(z_test,2)}")
            ctr = sc.norm.ppf(1 - float(area))
            st.subheader(f"Z Table :  {round(ctr, 2)}")
            if z_test > ctr:
                st.subheader("Reject Ho and Accpect Ha")
            else:
                st.subheader("Accpect Ho")

            exp2 = st.expander("Sample Dataset")
            exp2.dataframe(sample_dataset)