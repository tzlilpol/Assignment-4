from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
class kMeans(object):

    @staticmethod
    def kMeans(df, nClusters, nInit):
        output=KMeans(n_clusters=nClusters,n_init=nInit).fit(df)
        df['k_means']=output

    @staticmethod
    def scatter(df):


