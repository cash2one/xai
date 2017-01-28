

#calss header
class _PRIMITIVE():
	def __init__(self,): 
		self.name = "PRIMITIVE"
		self.definitions = [u'relating to human society at a very early stage of development, with people living in a simple way without machines or a writing system: ', u'Primitive living conditions are basic, unpleasant, and uncomfortable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
