

#calss header
class _SUBSIDIARY():
	def __init__(self,): 
		self.name = "SUBSIDIARY"
		self.definitions = [u'used to refer to something less important than something else with which it is connected: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
