

#calss header
class _SEEDY():
	def __init__(self,): 
		self.name = "SEEDY"
		self.definitions = [u'looking dirty or in bad condition and likely to be involved in dishonest or illegal activities: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
