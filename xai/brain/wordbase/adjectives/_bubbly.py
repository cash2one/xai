

#calss header
class _BUBBLY():
	def __init__(self,): 
		self.name = "BUBBLY"
		self.definitions = [u'(especially of a woman or girl) attractively full of energy and enthusiasm: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
