

#calss header
class _NATAL():
	def __init__(self,): 
		self.name = "NATAL"
		self.definitions = [u'relating to where a person or animal was born: ', u'relating to the birth of babies: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
