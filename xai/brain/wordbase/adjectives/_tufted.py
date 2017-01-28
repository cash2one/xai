

#calss header
class _TUFTED():
	def __init__(self,): 
		self.name = "TUFTED"
		self.definitions = [u'with, or made of, a tuft or tufts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
