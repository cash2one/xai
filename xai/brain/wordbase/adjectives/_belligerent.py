

#calss header
class _BELLIGERENT():
	def __init__(self,): 
		self.name = "BELLIGERENT"
		self.definitions = [u'wishing to fight or argue: ', u'fighting a war: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
