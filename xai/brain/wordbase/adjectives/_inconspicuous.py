

#calss header
class _INCONSPICUOUS():
	def __init__(self,): 
		self.name = "INCONSPICUOUS"
		self.definitions = [u'not easily or quickly noticed or seen, or not attracting attention: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
