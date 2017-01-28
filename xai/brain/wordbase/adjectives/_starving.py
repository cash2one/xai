

#calss header
class _STARVING():
	def __init__(self,): 
		self.name = "STARVING"
		self.definitions = [u'dying because of not having enough food: ', u'very hungry: ', u'extremely cold: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
