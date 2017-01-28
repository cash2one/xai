

#calss header
class _MANY():
	def __init__(self,): 
		self.name = "MANY"
		self.definitions = [u'used mainly in negative sentences and questions and with "too", "so", and "as" to mean "a large number of": ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
