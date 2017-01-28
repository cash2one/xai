

#calss header
class _WHIMSICAL():
	def __init__(self,): 
		self.name = "WHIMSICAL"
		self.definitions = [u'unusual and strange in a way that might be funny or annoying: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
