

#calss header
class _PEDESTRIAN():
	def __init__(self,): 
		self.name = "PEDESTRIAN"
		self.definitions = [u'not interesting; showing very little imagination: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
