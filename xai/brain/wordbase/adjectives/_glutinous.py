

#calss header
class _GLUTINOUS():
	def __init__(self,): 
		self.name = "GLUTINOUS"
		self.definitions = [u'sticky: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
