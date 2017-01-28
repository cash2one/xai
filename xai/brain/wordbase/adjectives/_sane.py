

#calss header
class _SANE():
	def __init__(self,): 
		self.name = "SANE"
		self.definitions = [u'having a healthy mind and not mentally ill: ', u'showing good judgment and understanding: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
