# Import libraries
import pandas as pd
import plotly as px
import streamlit as st

# Page configuration
st.set_page_config(
    page_title='Consoleflare Analytics Portal', 
    page_icon='📊'
)

# Title
st.title(':red[Data Analytics Portal]')
st.subheader(':gray[Explore your data with ease]')

# File Upload
file = st.file_uploader('Drop CSV or Excel file here', type=['csv', 'xlsx'])

if file is not None:
    if file.name.endswith('.csv'):
        data = pd.read_csv(file, encoding='utf-8', encoding_errors='ignore')
    else:
        data = pd.read_excel(file)
        
    st.dataframe(data)
    st.info('File is successfully loaded!', icon='🎊')

    # Dataset Summary
    st.subheader(':red[Basic Information of the Dataset]')
    tab1, tab2, tab3, tab4 = st.tabs(['Summary', 'Top and Bottom Rows', 'Data Types', 'Columns'])

    with tab1:
        st.write(f'There are {data.shape[0]} rows and {data.shape[1]} columns in the dataset.')
        st.subheader(':gray[Statistical Summary]')
        st.dataframe(data.describe())

    with tab2:
        st.subheader(':gray[Top Rows]')
        top_rows = st.slider('Number of rows you want', 1, min(50, data.shape[0]), key='top_rows')
        st.dataframe(data.head(top_rows))

        st.subheader(':gray[Bottom Rows]')
        bottom_rows = st.slider('Number of rows you want', 1, min(50, data.shape[0]), key='bottom_rows')
        st.dataframe(data.tail(bottom_rows))

    with tab3:
        st.subheader(':gray[Data Types]')
        st.write(data.dtypes)

    with tab4:
        st.subheader(':gray[Columns]')
        st.write(list(data.columns))

    # Value Counts
    st.subheader(':red[Column Value Counts]')
    with st.expander('Value Count'):
        col1, col2 = st.columns(2)
        with col1:
            column = st.selectbox('Choose a column', options=list(data.columns))
        with col2:
            top_n = st.number_input('Top rows', min_value=1, value=10, step=5)
        
        if st.button('Show Counts'):
            result = data[column].value_counts().reset_index().head(top_n)
            result.columns = [column, 'count']
            st.dataframe(result)

            st.subheader('Visualization')
            st.plotly_chart(px.bar(result, x=column, y='count', text='count', template='plotly_dark'))
            st.plotly_chart(px.line(result, x=column, y='count', text='count', template='plotly_dark'))
            st.plotly_chart(px.pie(result, names=column, values='count', template='plotly_dark'))

    # GroupBy Analysis
    st.subheader(':red[Groupby: Simplify Your Data Analysis]')
    st.write('Summarize your data using groupby functionality.')
    
    with st.expander('Group By Your Columns'):
        col1, col2, col3 = st.columns(3)
        with col1:
            groupby_cols = st.multiselect('Choose columns to group by', options=list(data.columns))
        with col2:
            operation_col = st.selectbox('Choose column for aggregation', options=list(data.columns))
        with col3:
            operation = st.selectbox('Choose operation', options=['mean', 'sum', 'count', 'min', 'max'])

        if groupby_cols:
            result = data.groupby(groupby_cols)[operation_col].agg(operation).reset_index()
            st.dataframe(result)

            st.subheader(':red[Data Visualization]')
            graph_type = st.selectbox('Choose Graph Type', ['Bar', 'Line', 'Pie', 'Scatter', 'Sunburst'])
            
            if graph_type == 'Bar':
                x_axis = st.selectbox('Choose X-axis', options=result.columns)
                y_axis = st.selectbox('Choose Y-axis', options=result.columns)
                color = st.selectbox('Choose Information', options=[None] + list(result.columns))
                st.plotly_chart(px.bar(result, x=x_axis, y=y_axis, color=color, template='plotly_dark'))
            
            elif graph_type == 'Line':
                x_axis = st.selectbox('Choose X-axis', options=result.columns)
                y_axis = st.selectbox('Choose Y-axis', options=result.columns)
                color = st.selectbox('Choose Information', options=[None] + list(result.columns))
                st.plotly_chart(px.line(result, x=x_axis, y=y_axis, color=color, template='plotly_dark'))
            
            elif graph_type == 'Scatter':
                x_axis = st.selectbox('Choose X-axis', options=result.columns)
                y_axis = st.selectbox('Choose Y-axis', options=result.columns)
                color = st.selectbox('Choose Information', options=[None] + list(result.columns))
                size = st.selectbox('Choose Size Column', options=[None] + list(result.columns))
                st.plotly_chart(px.scatter(result, x=x_axis, y=y_axis, color=color, size=size, template='plotly_dark'))
            
            elif graph_type == 'Pie':
                values = st.selectbox('Choose Numerical Values', options=result.columns)
                names = st.selectbox('Choose Labels', options=result.columns)
                st.plotly_chart(px.pie(result, values=values, names=names, template='plotly_dark'))
            
            elif graph_type == 'Sunburst': 
                path = st.multiselect('Choose Your Path', options=list(result.columns))
                if path:  # Ensuring path is not empty
                    fig = px.sunburst(data_frame=result, path=path, values=result.columns[-1])  # Using the last column as values
                    st.plotly_chart(fig)
