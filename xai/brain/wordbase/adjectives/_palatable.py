

#calss header
class _PALATABLE():
	def __init__(self,): 
		self.name = "PALATABLE"
		self.definitions = [u'Palatable food or drink has a pleasant taste: ', u'acceptable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
