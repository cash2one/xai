

#calss header
class _QUERULOUS():
	def __init__(self,): 
		self.name = "QUERULOUS"
		self.definitions = [u'often complaining, especially in a weak high voice: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
