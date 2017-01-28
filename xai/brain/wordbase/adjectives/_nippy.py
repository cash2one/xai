

#calss header
class _NIPPY():
	def __init__(self,): 
		self.name = "NIPPY"
		self.definitions = [u'able to change speed and direction easily: ', u'Nippy weather or air is quite cold: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
