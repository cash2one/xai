

#calss header
class _OLFACTORY():
	def __init__(self,): 
		self.name = "OLFACTORY"
		self.definitions = [u'connected with the ability to smell: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
