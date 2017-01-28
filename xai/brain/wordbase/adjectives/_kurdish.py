

#calss header
class _KURDISH():
	def __init__(self,): 
		self.name = "KURDISH"
		self.definitions = [u'related to the Kurdish people or their languages']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
