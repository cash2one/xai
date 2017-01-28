

#calss header
class _HEATEDLY():
	def __init__(self,): 
		self.name = "HEATEDLY"
		self.definitions = [u'in an excited or angry way']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
