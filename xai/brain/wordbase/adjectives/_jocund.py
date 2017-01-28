

#calss header
class _JOCUND():
	def __init__(self,): 
		self.name = "JOCUND"
		self.definitions = [u'in a happy mood']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
