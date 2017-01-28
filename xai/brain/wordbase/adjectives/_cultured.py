

#calss header
class _CULTURED():
	def __init__(self,): 
		self.name = "CULTURED"
		self.definitions = [u'A cultured person has had a good education and knows a lot about art, music, literature, etc.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
