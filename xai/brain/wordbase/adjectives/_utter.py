

#calss header
class _UTTER():
	def __init__(self,): 
		self.name = "UTTER"
		self.definitions = [u'complete or extreme: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
