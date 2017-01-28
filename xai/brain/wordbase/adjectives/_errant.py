

#calss header
class _ERRANT():
	def __init__(self,): 
		self.name = "ERRANT"
		self.definitions = [u'behaving wrongly in some way, especially by leaving home: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
