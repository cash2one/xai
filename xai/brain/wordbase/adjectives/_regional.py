

#calss header
class _REGIONAL():
	def __init__(self,): 
		self.name = "REGIONAL"
		self.definitions = [u'relating to or coming from a particular part of a country: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
