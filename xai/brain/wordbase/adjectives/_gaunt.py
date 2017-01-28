

#calss header
class _GAUNT():
	def __init__(self,): 
		self.name = "GAUNT"
		self.definitions = [u'very thin, especially because of sickness or hunger: ', u'empty and not attractive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
