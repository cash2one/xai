

#calss header
class _EUCLIDEAN():
	def __init__(self,): 
		self.name = "EUCLIDEAN"
		self.definitions = [u'relating to the geometry (= the study of angles and shapes formed by the relationships between lines) described by Euclid']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
