

#calss header
class _EURASIAN():
	def __init__(self,): 
		self.name = "EURASIAN"
		self.definitions = [u'A Eurasian person has one European parent and one Asian parent.', u'of or connected with Europe and Asia considered as a unit: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
