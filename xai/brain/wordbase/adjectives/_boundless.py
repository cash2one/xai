

#calss header
class _BOUNDLESS():
	def __init__(self,): 
		self.name = "BOUNDLESS"
		self.definitions = [u'having no limit: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
