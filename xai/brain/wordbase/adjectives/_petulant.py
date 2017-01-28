

#calss header
class _PETULANT():
	def __init__(self,): 
		self.name = "PETULANT"
		self.definitions = [u'easily annoyed and complaining in a rude way like a child']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
