

#calss header
class _INELEGANT():
	def __init__(self,): 
		self.name = "INELEGANT"
		self.definitions = [u'not attractive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
