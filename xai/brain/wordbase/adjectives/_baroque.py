

#calss header
class _BAROQUE():
	def __init__(self,): 
		self.name = "BAROQUE"
		self.definitions = [u'relating to the heavily decorated style in buildings, art, and music that was popular in Europe in the 17th century and the early part of the 18th century: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
