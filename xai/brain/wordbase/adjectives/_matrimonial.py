

#calss header
class _MATRIMONIAL():
	def __init__(self,): 
		self.name = "MATRIMONIAL"
		self.definitions = [u'related to marriage or people who are married']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
