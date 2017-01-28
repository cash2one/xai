

#calss header
class _LABYRINTHINE():
	def __init__(self,): 
		self.name = "LABYRINTHINE"
		self.definitions = [u'used to describe something that has a lot of parts and is therefore confusing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
