

#calss header
class _MAGICAL():
	def __init__(self,): 
		self.name = "MAGICAL"
		self.definitions = [u'produced by or using magic: ', u'used for describing something with a special and exciting quality: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
