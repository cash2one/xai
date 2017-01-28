

#calss header
class _LEAFY():
	def __init__(self,): 
		self.name = "LEAFY"
		self.definitions = [u'A leafy place is pleasant and has a lot of trees: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
