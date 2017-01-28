

#calss header
class _NORTHEAST():
	def __init__(self,): 
		self.name = "NORTHEAST"
		self.definitions = [u'in or towards the northeast: ', u'a wind that comes from the northeast']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
