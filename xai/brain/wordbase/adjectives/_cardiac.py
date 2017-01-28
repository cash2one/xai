

#calss header
class _CARDIAC():
	def __init__(self,): 
		self.name = "CARDIAC"
		self.definitions = [u'of the heart or heart disease']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
