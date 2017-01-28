

#calss header
class _SIGHTLESS():
	def __init__(self,): 
		self.name = "SIGHTLESS"
		self.definitions = [u'unable to see']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
