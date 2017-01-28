

#calss header
class _DIVISIONAL():
	def __init__(self,): 
		self.name = "DIVISIONAL"
		self.definitions = [u'relating to a division (= part) of an army or large organization: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
