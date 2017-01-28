

#calss header
class _SLICK():
	def __init__(self,): 
		self.name = "SLICK"
		self.definitions = [u'operating or performing skilfully and effectively, without problems and without seeming to need effort: ', u'skilful and effective but not sincere or honest: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
