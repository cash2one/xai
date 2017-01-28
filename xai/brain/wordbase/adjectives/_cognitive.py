

#calss header
class _COGNITIVE():
	def __init__(self,): 
		self.name = "COGNITIVE"
		self.definitions = [u'connected with thinking or conscious mental processes: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
