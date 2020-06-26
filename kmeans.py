from sklearn.cluster import KMeans
import plotly.express as px
import chart_studio.plotly as py
import matplotlib.pyplot as plt
import pandas as pd
import os


class kMeans(object):

    @staticmethod
    def k_means_modeling(df, nClusters, nInit):
        output = KMeans(n_clusters=int(nClusters),n_init=int(nInit)).fit(df)
        df['k_means'] = output.labels_

    @staticmethod
    def scatter(df,path):
        plt.scatter(x=df['Generosity'], y=df['Social support'], c=df['k_means'].tolist(), label=df['k_means'])
        plt.title('K Means Clustering')
        plt.xlabel('Generosity')
        plt.ylabel('Social support')
        plt.savefig(os.path.dirname(path)+'/scatter.png')

    @staticmethod
    def horoplethMap(df,path):
        countriesDataSet = pd.read_csv('countries_codes_and_coordinates.csv')
        countriesCodes=[]
        for index1, row1 in df.iterrows():
            Found=False
            for index2, row2 in countriesDataSet.iterrows():
                if(row1.name.lower()==row2['Country'].lower()):
                    countriesCodes.append(row2['Alpha-3 code'].strip())
                    Found=True
                    break
            if(Found==False):
                print(row1.name)
        df['countriesCodes']=countriesCodes
        fig = px.choropleth(df,locations='countriesCodes',color='k_means',color_continuous_scale=px.colors.sequential.Plasma, title='K Means Clustering Visualization')
        py.sign_in('dorelkab', 'XcEuEweWhBEW7z5ltW5Q')
        py.image.save_as(fig, filename=os.path.dirname(path)+'/choropleth.png');
