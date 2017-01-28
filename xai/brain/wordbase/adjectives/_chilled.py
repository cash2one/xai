

#calss header
class _CHILLED():
	def __init__(self,): 
		self.name = "CHILLED"
		self.definitions = [u'relaxed, not worrying about anything: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
