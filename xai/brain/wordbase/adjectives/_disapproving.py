

#calss header
class _DISAPPROVING():
	def __init__(self,): 
		self.name = "DISAPPROVING"
		self.definitions = [u'showing that you feel something or someone is bad or wrong: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
