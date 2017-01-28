

#calss header
class _SUBURBAN():
	def __init__(self,): 
		self.name = "SUBURBAN"
		self.definitions = [u'relating to a suburb: ', u'used to suggest that something is boring and has no excitement: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
