

#calss header
class _ACIDULOUS():
	def __init__(self,): 
		self.name = "ACIDULOUS"
		self.definitions = [u'sour or sharp in taste: ', u'sharply critical or cruel: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
