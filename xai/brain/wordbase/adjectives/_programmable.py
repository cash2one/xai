

#calss header
class _PROGRAMMABLE():
	def __init__(self,): 
		self.name = "PROGRAMMABLE"
		self.definitions = [u'able to be programmed']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
