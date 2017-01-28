

#calss header
class _ALLURING():
	def __init__(self,): 
		self.name = "ALLURING"
		self.definitions = [u'attractive or exciting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
