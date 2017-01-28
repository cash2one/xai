

#calss header
class _PROSPECTIVE():
	def __init__(self,): 
		self.name = "PROSPECTIVE"
		self.definitions = [u'people who are expected to buy something, employ someone, become parents, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
