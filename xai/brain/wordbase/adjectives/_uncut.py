

#calss header
class _UNCUT():
	def __init__(self,): 
		self.name = "UNCUT"
		self.definitions = [u'complete and in its original form: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
