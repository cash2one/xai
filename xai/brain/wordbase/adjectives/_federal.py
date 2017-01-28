

#calss header
class _FEDERAL():
	def __init__(self,): 
		self.name = "FEDERAL"
		self.definitions = [u'relating to the central government, and not to the government of a region, of some countries such as the US: ', u'A federal system of government consists of a group of regions that are controlled by a central government.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
