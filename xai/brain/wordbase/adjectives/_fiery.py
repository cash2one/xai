

#calss header
class _FIERY():
	def __init__(self,): 
		self.name = "FIERY"
		self.definitions = [u'bright red, like fire: ', u'Fiery food causes a strong burning feeling in the mouth: ', u'showing very strong feeling: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
