

#calss header
class _JEWELLED():
	def __init__(self,): 
		self.name = "JEWELLED"
		self.definitions = [u'decorated with jewels']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
