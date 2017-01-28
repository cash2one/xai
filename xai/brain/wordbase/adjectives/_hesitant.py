

#calss header
class _HESITANT():
	def __init__(self,): 
		self.name = "HESITANT"
		self.definitions = [u'If you are hesitant, you do not do something immediately or quickly because you are nervous or not certain: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
