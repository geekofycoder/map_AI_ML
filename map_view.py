# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import geopandas as gpd

# # %matplotlib inline

# # crime_data=pd.read_csv('District_wise_crimes_committed_IPC_2001_2012.csv')

# # odisha_crime_data=crime_data.loc[crime_data.STATE_UT=="ODISHA"]\
    
# # odisha_copy=odisha_crime_data.copy()

# # odisha_crime_data=odisha_crime_data.set_index('DISTRICT')

# # odisha_crime_data=odisha_crime_data.drop(['STATE_UT','YEAR'],axis=1)
# # odisha_crime_data=odisha_crime_data.drop('TOTAL')

# # list_of_district=list(odisha_crime_data.index.unique())

# # data=[]
# # for district in list_of_district:
# #     data.append(odisha_crime_data[odisha_crime_data.index==district].sum())
    
# # dfs = []
# # for i in range(0, len(data), 2):
# #     df = pd.concat([data[i], data[i+1]], axis=1).T
# #     df.index = [list_of_district[i],list_of_district[i+1]]
# #     dfs.append(df)

# # final_df = pd.concat(dfs)

# # start = final_df['TOTAL_IPC_CRIMES'].min()+1000
# # end = final_df['TOTAL_IPC_CRIMES'].max()

# # start = min(start, end)

# # # quantiles = np.percentile(final_df['TOTAL_IPC_CRIMES'], np.linspace(0, 100, 11))
# # # thresholds = quantiles[1:] 
# # divisions = np.linspace(start, end, 11)
# # thresholds=divisions

# # def assign_safety_rating(crime_count):
# #     for i, threshold in enumerate(divisions[:-1]):
# #         if crime_count <= threshold:
# #             # Rescale the safety rating to range from 1 to 10
# #             return int((i / 10) * 9 + 1)
# #     return 10 
# # final_df['SAFETY_RATING'] = final_df['TOTAL_IPC_CRIMES'].apply(assign_safety_rating)

# # final_df['SAFETY_RATING']=10-final_df['SAFETY_RATING']



# # Load Odisha map data (replace 'odisha_map.geojson' with your file)
# odisha_map = gpd.read_file('odisha_map.geojson')

# # Load safety ratings data (replace 'safety_ratings.csv' with your file)
# safety_ratings = pd.read_csv('safety_ratings.csv')

# # Merge data
# merged_df = pd.merge(odisha_map, safety_ratings, left_index=True, right_index=True)

# # Plot the map
# fig, ax = plt.subplots(figsize=(10, 10))
# merged_df.plot(ax=ax, column='SAFETY_RATING', cmap='viridis', legend=True, legend_kwds={'label': "Safety Rating"})
# plt.title("District Safety Ratings in Odisha")
# plt.xlabel("Longitude")
# plt.ylabel("Latitude")

# plt.show()
# import streamlit as st
# import pandas as pd
# import geopandas as gpd
# import plotly.express as px

# # Load Odisha map data (replace 'odisha_map.geojson' with your file)
# odisha_map = gpd.read_file('odisha_map.geojson')

# # Load safety ratings data (replace 'safety_ratings.csv' with your file)
# safety_ratings = pd.read_csv('safety_ratings.csv') 

# # Merge data
# merged_df = pd.merge(odisha_map, safety_ratings, left_index=True, right_index=True)

# # Create Streamlit web application
# def main():
#     # Set page title and description
#     st.title('District Safety Ratings in Odisha')
#     st.write('This web application displays the safety ratings of districts in Odisha.')

#     # Create interactive map with Plotly Express
#     fig = px.choropleth(merged_df, 
#                         geojson=merged_df.geometry, 
#                         locations=merged_df.index, 
#                         color='SAFETY_RATING',
#                         color_continuous_scale="Viridis",
#                         projection="mercator",
#                         hover_name=merged_df.index,
#                         hover_data={'SAFETY_RATING': True},
#                         labels={'SAFETY_RATING': 'Safety Rating'}
#                         )
#     fig.update_geos(fitbounds="locations", visible=False)
#     fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#     # Display the map using Streamlit
#     st.plotly_chart(fig)

# if __name__ == '__main__':
#     main()

import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px

# Load Odisha map data (replace 'odisha_map.geojson' with your file)
odisha_map = gpd.read_file('odisha_map.geojson')

# Load safety ratings data (replace 'safety_ratings.csv' with your file)
safety_ratings = pd.read_csv('safety_ratings.csv') 


# Merge data
merged_df = pd.merge(odisha_map, safety_ratings, left_index=True, right_index=True)

# Create Streamlit web application
def main():
    # Set page title and description
    st.title('District Safety Ratings in Odisha')
    st.write('This web application displays the safety ratings of districts in Odisha.')

    # Create interactive map with Plotly Express
    fig = px.choropleth(merged_df, 
                        geojson=merged_df.geometry, 
                        locations=merged_df.index, 
                        color='SAFETY_RATING',
                        color_continuous_scale="YlOrRd",  # Change the color scale
                        projection="mercator",
                        hover_name=merged_df.index,  # Specify the index for hover text
                        hover_data={'SAFETY_RATING': True},
                        labels={'SAFETY_RATING': 'Safety Rating'}
                        )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    # Display the map using Streamlit
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()
