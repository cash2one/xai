

#calss header
class _TAXING():
	def __init__(self,): 
		self.name = "TAXING"
		self.definitions = [u'difficult or needing a lot of thought or effort: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
