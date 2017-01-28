

#calss header
class _INEXORABLE():
	def __init__(self,): 
		self.name = "INEXORABLE"
		self.definitions = [u'continuing without any possibility of being stopped: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
