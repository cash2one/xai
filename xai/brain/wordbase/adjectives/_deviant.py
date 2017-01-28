

#calss header
class _DEVIANT():
	def __init__(self,): 
		self.name = "DEVIANT"
		self.definitions = [u'used to describe a person or behaviour that is not usual and is generally considered to be unacceptable']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
