

#calss header
class _IMPIOUS():
	def __init__(self,): 
		self.name = "IMPIOUS"
		self.definitions = [u'showing no respect, especially for God or religion']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
