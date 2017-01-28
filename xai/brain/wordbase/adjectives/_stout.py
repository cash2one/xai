

#calss header
class _STOUT():
	def __init__(self,): 
		self.name = "STOUT"
		self.definitions = [u'(especially of older people) fat and solid-looking, especially around the waist: ', u'Stout objects are strongly made from thick, strong materials: ', u'strong and determined: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
