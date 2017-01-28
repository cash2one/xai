

#calss header
class _SLAVISH():
	def __init__(self,): 
		self.name = "SLAVISH"
		self.definitions = [u'obeying completely and having no original thoughts or ideas: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
