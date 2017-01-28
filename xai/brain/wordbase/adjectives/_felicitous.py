

#calss header
class _FELICITOUS():
	def __init__(self,): 
		self.name = "FELICITOUS"
		self.definitions = [u'suitable or right and expressing well the intended thought or feeling: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
