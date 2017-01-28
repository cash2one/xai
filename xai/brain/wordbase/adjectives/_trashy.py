

#calss header
class _TRASHY():
	def __init__(self,): 
		self.name = "TRASHY"
		self.definitions = [u'of low quality; with little or no value: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
