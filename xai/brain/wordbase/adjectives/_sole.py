

#calss header
class _SOLE():
	def __init__(self,): 
		self.name = "SOLE"
		self.definitions = [u'being one only; single: ', u'not shared with anyone else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
