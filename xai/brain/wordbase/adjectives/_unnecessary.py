

#calss header
class _UNNECESSARY():
	def __init__(self,): 
		self.name = "UNNECESSARY"
		self.definitions = [u'not needed or wanted, or more than is needed or wanted: ', u'An offensive remark or action that is unnecessary could have been avoided: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
