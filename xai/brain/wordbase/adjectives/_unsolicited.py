

#calss header
class _UNSOLICITED():
	def __init__(self,): 
		self.name = "UNSOLICITED"
		self.definitions = [u'not asked for: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
