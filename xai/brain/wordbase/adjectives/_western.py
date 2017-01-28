

#calss header
class _WESTERN():
	def __init__(self,): 
		self.name = "WESTERN"
		self.definitions = [u'in or from the west of a place: ', u'relating to countries in the west part of the world, especially North America and countries in the west of Europe: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
