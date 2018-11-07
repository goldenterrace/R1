
import sample_student as sample
import util
import helper

# Cluster class
class Cluster(object):

    def __init__(self, samples):
        """Assumes samples is a list of Sample Class instances"""
        self.samples = samples # [a, b], a = sample.Sample('a', [1, 9]), etc
        """ centroid is also an instance of Sample class """
        self.centroid = self.computeCentroid()

    def size(self):
        return len(self.samples)

    def getCentroid(self):
        return self.centroid

    def getMembers(self):
        return self.samples

    #### Implement the centroid computing function here!

    def computeCentroid(self):
        '''
        use average x and y coordinates as centroids
        similar to using Minkowski Distance with p = 1
        return an instance of Sample, its features should be
        the center of all the samples in the cluster
        '''

        #------- your code below -----------#
        return helper.computeCentroid(self)

        #-------- end of your code ----------#

    #### Implement the centroid updating function here!
    def update(self, new_samples):
        """Replace the samples in the cluster by new samples
           Return: how much the centroid has changed"""

        #------- your code below -----------#
        return helper.update(self, new_samples)

        #-------- end of your code ----------#

    def __str__(self):
        names = []
        for e in self.samples:
            names.append(e.getName())
        names.sort()
        result = 'Cluster with centroid '\
                 + str(self.centroid.getFeatures()) + ' contains:\n  '
        for e in names:
            result = result + e + ', '
        return result[:-2]

if __name__ == "__main__":
    test_samples = util.genDistribution()
    c = Cluster(test_samples)
    #print(c.centroid)
    print("cluster center: ", c.centroid.features)
    util.plot_cluster([c])

    # now assign the cluster new samples, and move it
    test_samples2 = util.genDistribution(1, 1, 1, 1, 30)
    diff = c.update(test_samples2 + test_samples)
    print("center moved: ", diff)
    # plot_cluster expects an array of cluster...
    util.plot_cluster([c])
