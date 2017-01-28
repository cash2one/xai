

#calss header
class _FUNKY():
	def __init__(self,): 
		self.name = "FUNKY"
		self.definitions = [u'used to describe a style of music, usually for dancing to, with a strong rhythm based on jazz and a tune that repeats: ', u'fashionable in an unusual and noticeable way: ', u'having a bad smell or appearance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
