

#calss header
class _TINNY():
	def __init__(self,): 
		self.name = "TINNY"
		self.definitions = [u'Tinny sound is of low quality or like metal being hit: ', u'If something made of metal is tinny, it is not strong and not of good quality: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
