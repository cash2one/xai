

#calss header
class _SVELTE():
	def __init__(self,): 
		self.name = "SVELTE"
		self.definitions = [u'attractively thin, graceful, and stylish']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
