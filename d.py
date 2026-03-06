import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Data Analysis Dashboard", layout="wide")

st.title("AI Agent Data Analysis Dashboard")
st.write("Upload a CSV dataset to begin analysis")

# CSV Upload
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file)

        st.success("CSV file uploaded successfully")

        # Dataset Preview
        st.subheader("Dataset Preview")
        st.dataframe(df.head())

        # Show Columns
        st.subheader("Detected Columns")
        st.write(list(df.columns))

        # Column Selection
        st.subheader("Column Selection")

        date_column = st.selectbox(
            "Select Date Column",
            df.columns
        )

        value_column = st.selectbox(
            "Select Value Column",
            df.columns
        )

        # Validate Column Types
        error_message = ""

        if date_column:
            try:
                df[date_column] = pd.to_datetime(df[date_column])
            except:
                error_message = "Selected Date Column is not a valid datetime format"

        if value_column:
            if not pd.api.types.is_numeric_dtype(df[value_column]):
                error_message = "Selected Value Column must contain numeric values"

        # Error Handling
        if error_message:
            st.error(error_message)

        else:
            st.success("Columns validated successfully")

            # Show Selected Columns
            st.subheader("Selected Columns")
            st.write("Date Column:", date_column)
            st.write("Value Column:", value_column)

            # Start Workflow
            if st.button("Start AI Agent Analysis"):
                st.success("AI Agent Workflow Initiated")

                # Example workflow message
                st.info("Data is ready for AI analysis module")

    except Exception as e:
        st.error("Error reading CSV file")

else:
    st.info("Please upload a CSV file to continue")