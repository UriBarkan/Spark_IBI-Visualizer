# Description:
#     This file contains functions to create the dashboard.
#     The functions are divided into two groups:
#         - Functions to load the data from the excel file.
#         - Functions to create the dashboard.
#
# Functions:
#     - load_data(file):
#         This function reads the data from an excel file and returns it as a pandas DataFrame.
#     - load_class_data(file):
#         This function reads the classification data from an excel file and returns it as a pandas DataFrame.
#     - remove_unnecessary_columns(df):
#         This function removes unnecessary columns from the DataFrame.
#     - replace_column_name(df):
#         This function replaces the column's name from '.curr' to 'Currency'.
#     - replace_currency(df):
#         This function replaces currency names.
#
# Required packages:
#     - pandas
#     - streamlit
#     - streamlit.components.v1
#     - plotly.express
#     - openpyxl
#
# Required files:
#     - Data.xlsx
#     - Classification.xlsx
#
# Created by:
#     - Uri Barkan
#
# Licence:
#     - MIT Licence
# Copyright 2023 Uri Barkan

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Date:
#     - 17.4.2023
#




import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")
import plotly.express as px

# Creating function to read data
# Read data from an excel file and return as a pandas DataFrame.

#     Args:
#         file (str): The path to the excel file.

#     Returns:
#         pandas.DataFrame: A DataFrame containing the data from the excel file.



def load_data(file):
# Creating function to read classification data

# Read classification data from an excel file and return as a pandas DataFrame.

#     Args:
#         file (str): The path to the excel file.
#
#     Returns:
#         pandas.DataFrame: A DataFrame containing the data from the excel file.
    dfData = pd.read_excel(file, engine="openpyxl")
    return dfData

def load_class_data(file):
# Read classification data from an excel file and return as a pandas DataFrame.

#     Args:
#         file (str): The path to the excel file.
#
#     Returns:
#         pandas.DataFrame: A DataFrame containing the data from the excel file.
    dfClass = pd.read_excel(file, engine="openpyxl")
    return dfClass


def remove_unnecessary_columns(df):
    # Function to remove unnecessary columns
    #
    # Args:
    #   df (pandas.DataFrame): A pandas DataFrame containing the data.
    #
    # Returns:
    #   pandas.DataFrame: A new pandas DataFrame with the unnecessary columns removed.
    return df.drop(['Symbol', 'Alerts', 'Similar', 'Analysts', 'Price Target', 'Potential Return', 'Rate', 'Profit / Loss', 'FIFO Cost', 'FIFO change %', 'change of FIFO in nis', 'Average FIFO Cost'], axis=1)


def replace_column_name(df):
    # Renames the 'curr.' column in the given dataframe to 'Currency'.
    # 
    # Args:
    #   df: pandas dataframe containing column named 'curr.'
    # 
    # Returns:
    #   Pandas dataframe with renamed column.
    df.rename(columns={'curr.':'Currency'}, inplace=True)
    return df


def replace_currency(df):
    # Replaces the values in the 'Currency' column of the given dataframe, such that:
    #
    # - Any value containing the string 'שקל' will be replaced with 'NIS'
    # - Any value containing the string 'דולר' will be replaced with 'USD'
    #
    # Args:
    #     df (pandas.DataFrame): The dataframe containing the 'Currency' column to be modified.
    #   
    # Returns:
    #     pandas.DataFrame: The modified dataframe with replaced values in the 'Currency' column.

    df.loc[df['Currency'].str.contains('שקל'), 'Currency'] = 'NIS'
    df.loc[df['Currency'].str.contains('דולר'), 'Currency'] = 'USD'
    return df


def filter_stock_names(df):
    # Filters out rows from the input DataFrame `df` where the 'Stock Number'
    #     column matches any of the specified stock names. The list of stock names
    #     to exclude is hard-coded within the function.

    #     Args:
    #         df (pd.DataFrame): The input DataFrame to filter.

    #     Returns:
    #         pd.DataFrame: A new DataFrame containing only the rows from `df` where
    #         the 'Stock Number' column does not match any of the excluded stock names.

    stock_names = ["דולר ארה\"ב", "התחיבות דולרית", "דולרים לקבל", "מגן מס", "מס עתידי"]
    return df[~df['Stock Number'].isin(stock_names)]

def calculate_total_investments_by_currency(df):
    # Calculates the total investments in USD and NIS based on the dataframe provided.
    
    # Args:
    #   df : pandas.DataFrame
    #     The input dataframe containing the investment information.
        
    # Returns:
    #   tuple of floats
    #     A tuple of two floats representing the total investments in USD and NIS respectively.

    # Filter the rows based on the currency
    df_usd = df[df['Currency'] == 'USD']
    df_nis = df[df['Currency'] == 'NIS']
    
    # Calculate the total investments in USD and NIS
    total_usd = df_usd['Current Value ILS'].sum()
    total_nis = df_nis['Current Value ILS'].sum()
    
    # Return the total investments
    return total_usd, total_nis

def calculate_total_investments_by_Securyity_Type(df):
    # Calculate the total investments in stocks and bonds from the given dataframe.

    # Args:
    #     df (pandas.DataFrame): Dataframe containing the investments information.

    # Returns:
    #     tuple: A tuple containing the total investments in stocks and bonds respectively.

    # Filter the rows based on the Security Type
    df_Stock = df[df['Security Type'] == 'Stock']
    df_Bond = df[df['Security Type'] == 'Bond']
    
    # Calculate the total investments in Stock and Bond
    total_Stock = df_Stock['Current Value ILS'].sum()
    total_Bond = df_Bond['Current Value ILS'].sum()
    
    # Return the total investments
    return total_Stock, total_Bond

def calculate_total_investments_by_Market(df):
    # Calculates the total investments in the Global and IL markets.
    #
    # Args:
    #   df: pandas.DataFrame
    #     The data frame containing the investments information.
    #
    # Returns:
    #   tuple
    #     A tuple containing the total investments in the Global and IL markets, respectively.

    # Filter the rows based on the Security Type
    df_Global = df[df['Market'] == 'Global']
    df_IL = df[df['Market'] == 'IL']
    
    # Calculate the total investments in Global and IL
    total_Global = df_Global['Current Value ILS'].sum()
    total_IL = df_IL['Current Value ILS'].sum()
    
    # Return the total investments
    return total_Global, total_IL

# Setting up the layout of the app
st.title("Spark-IBI Visulaizatio Tool")
st.write("Upload your data files below")
uploaded_file_1 = st.file_uploader("Upload investment data", type=["xlsx"])
uploaded_file_2 = st.file_uploader("Upload classification data", type=["xlsx"])

# If files are uploaded, show the data table and column graph
if uploaded_file_1 and uploaded_file_2:
    # Load the data
    dfData = load_data(uploaded_file_1)
    dfClass = load_class_data(uploaded_file_2)

    # Merge the data
    df = pd.merge(dfData, dfClass[['Stock Number', 'Security Type', 'Market']], on='Stock Number')


    # Replace the column's name from '.curr' to 'Currency'
    df = replace_column_name(df)

    # Remove unnecessary columns
    df = remove_unnecessary_columns(df)

    # Replace currency names
    df = replace_currency(df)

    # Filter out specific stock names
    df = filter_stock_names(df)

    col1, col2 = st.columns([1, 1], gap = "large")
    with col1:
        # Create three dropdwon menus, each has the following three options:
        # - Currency
        # - Security Type
        # - Market
        # So the user can choose the order of the sunburst, from the inner curcle to the outside. 

        st.write("**Sunburst Graph**")
        # Create all possibel permutations of Currency, Security type and Market
        option = st.selectbox("Select order: ", ("Currency, Security Type, Market", \
                                "Security Type, Currency, Market", \
                                "Market, Security Type, Currency", \
                                "Security Type, Market, Currency", \
                                "Market, Currency, Security Type", \
                                "Currency, Market, Security Type"))

        #Assign the selction to the path variable
        if option == "Currency, Security Type, Market":
            path = ["Currency", "Security Type", "Market"]
        elif option == "Security Type, Currency, Market":
            path = ["Security Type", "Currency", "Market"]
        elif option == "Market, Security Type, Currency":
            path = ["Market", "Security Type", "Currency"]
        elif option == "Security Type, Market, Currency":
            path = ["Security Type", "Market", "Currency"]
        elif option == "Market, Currency, Security Type":
            path = ["Market", "Currency", "Security Type"]
        elif option == "Currency, Market, Security Type":
            path = ["Currency", "Market", "Security Type"]

        # Based on the user's selection, the app should show a sunburst graph of the dataframe
        # with the selected order
        print(path)
        fig = px.sunburst(df, path = path, values='Current Value ILS')
        st.plotly_chart(fig, use_container_width=True)
    
    # Display the merged data in a table
    st.write("Investmments Table")

    st.write(df)
    
    with col2:
        # Calculate the total investments by currency
        total_usd, total_nis = calculate_total_investments_by_currency(df)

        # Display the results in a table
        # st.write(pd.DataFrame({
        #     "Currency": ["USD", "NIS"],
        #     "Total holdings [NIS]": [total_usd, total_nis]
        # })) 

        # Plot the investments by currency
        fig = px.bar(df, x='Currency', y='Current Value ILS', color='Currency', hover_data=['Stock Name', 'Current Value ILS'])
        fig.update_layout(
            title='Investments by Currency',
            xaxis_title='Currency',
            yaxis_title='Total holdings [NIS]',
            xaxis=dict(
                tickmode='linear',
                tick0=0,
                dtick=1
            )
        )
        st.plotly_chart(fig, use_container_width=True)

        # Calculate the total investments by security type
        total_Stock, total_Bond = calculate_total_investments_by_Securyity_Type(df)

        # Display the results in a table
        # st.write(pd.DataFrame({
        #     "Security Type": ["Stock", "Bond"],
        #     "Total holdings [NIS]": [total_Stock, total_Bond]
        # })) 

        # Plot the investments by Security Type
        fig = px.bar(df, x='Security Type', y='Current Value ILS', color='Security Type', hover_data=['Stock Name', 'Current Value ILS'])
        fig.update_layout(
            title='Investments by Security Type',
            xaxis_title='Security Type',
            yaxis_title='Total holdings [NIS]',
            xaxis=dict(
                tickmode='linear',
                tick0=0,
                dtick=1
            )
        )
        st.plotly_chart(fig, use_container_width=True)

    # Calculate the total investments by Market
        total_Global, total_IL = calculate_total_investments_by_Market(df)

        # Display the results in a table
        # st.write(pd.DataFrame({
        #     "Market": ["Global", "IL"],
        #     "Total holdings [NIS]": [total_Global, total_IL]
        # })) 

        # Plot the investments by Market
        fig = px.bar(df, x='Market', y='Current Value ILS', color='Market', hover_data=['Stock Name', 'Current Value ILS'])
        fig.update_layout(
            title='Investments by Market',
            xaxis_title='Market',
            yaxis_title='Total holdings [NIS]',
            xaxis=dict(
                tickmode='linear',
                tick0=0,
                dtick=1
            )
        )
        st.plotly_chart(fig, use_container_width=True)

        








        
