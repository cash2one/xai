

#calss header
class _MODERN():
	def __init__(self,): 
		self.name = "MODERN"
		self.definitions = [u'designed and made using the most recent ideas and methods: ', u'of the present or recent times, especially the period of history since around 1500: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
