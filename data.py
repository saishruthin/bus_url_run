import streamlit as st
import pandas as pd
import plotly.express as px
def data():
    dataset_url = "https://raw.githubusercontent.com/saishruthin/bus_fleet_details/main/Road%20Transport.csv"
    df = pd.read_csv(dataset_url)
    st.title("📊 Bus Transport details")
    dis_filter = st.selectbox("What is the district that you want to filter? ", pd.unique(df['Districts']))
    df_1 = df[df['Districts'] == dis_filter]
    st.markdown(f"#Filter data {dis_filter}")
    st.markdown(f"**Number of Bus Depots from {dis_filter} are** {int(df_1['RTC Bus Depots'].iloc[0])}")
    st.markdown(f"**Number of Bus Fleets from {dis_filter} are** {int(df_1['RTC Fleet of Buses'].iloc[0])}")
    st.markdown(f"**Number of kms travelled from {dis_filter} are** {int(df_1['Daily Operated Length (Kms.)'])} kms")

    mean_length = round(df['Daily Operated Length (Kms.)'].mean())
    mean_fleet = round(df['RTC Fleet of Buses'].mean())
    mean_depots = round(df['RTC Bus Depots'].mean())

    kpi1, kpi2, kpi3 = st.columns(3)
    with kpi1:
        st.subheader("The average distance travelled from the districts by a bus")
        st.subheader(f"{mean_length} kms")
    with kpi2: 
        st.subheader("The average number of bus fleets are: ")
        st.subheader(f"{mean_fleet}")
    with kpi3:
        st.subheader("The average number of bus depots are")
        st.subheader(f"{mean_depots}")

    g1, g2, g3 = st.columns(3)
    fig1 = px.bar(df, x = 'Districts', y = 'Daily Operated Length (Kms.)', title = 'Districts vs Daily Operated Length')
    fig2 = px.bar(df, x = 'Districts', y = 'RTC Fleet of Buses', title = 'Districts vs RTC Fleet of buses')
    fig3 = px.bar(df, x = 'Districts', y = 'RTC Bus Depots', title = 'Districts vs Bus Depots')

    with g1:
        fig1.add_hline(y = mean_length, line_dash = 'dash', line_color = 'red', annotation_text = 'Mean Length', annotation_position = 'top left')
        fig1.update_traces(marker_color = ['lightskyblue' if d == dis_filter else 'lightgrey' for d in df['Districts']])
        st.plotly_chart(fig1, use_container_width=True)
    with g2:
        fig2.add_hline(y = mean_fleet, line_dash = 'dash', line_color = 'red', annotation_text = "Mean Fleet", annotation_position = 'top left')
        fig2.update_traces(marker_color = ['lightskyblue' if d == dis_filter else 'lightgrey' for d in df['Districts']])
        st.plotly_chart(fig2, use_container_width=True)
    with g3:
        fig3.add_hline(y = mean_depots, line_dash = 'dash', line_color = 'red', annotation_text = "Mean Depot", annotation_position = 'top left')
        fig3.update_traces(marker_color = ['lightskyblue' if d == dis_filter else 'lightgrey' for d in df['Districts']])
        st.plotly_chart(fig3, use_container_width=True)
data()