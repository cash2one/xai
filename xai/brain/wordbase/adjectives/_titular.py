

#calss header
class _TITULAR():
	def __init__(self,): 
		self.name = "TITULAR"
		self.definitions = [u'having the title of a position but not the responsibilities, duties, or power; in name only: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
