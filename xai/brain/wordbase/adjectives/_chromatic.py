

#calss header
class _CHROMATIC():
	def __init__(self,): 
		self.name = "CHROMATIC"
		self.definitions = [u'relating to colours: ', u'belonging or relating to a musical scale in which the notes follow each other in semitones: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
