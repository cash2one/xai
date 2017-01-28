

#calss header
class _BOBBED():
	def __init__(self,): 
		self.name = "BOBBED"
		self.definitions = [u"(of a style of women's hair) cut to neck length all around the head: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
