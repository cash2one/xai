

#calss header
class _FILTHY():
	def __init__(self,): 
		self.name = "FILTHY"
		self.definitions = [u'extremely or unpleasantly dirty: ', u'containing sexually offensive words or pictures: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
