

#calss header
class _PECULIARLY():
	def __init__(self,): 
		self.name = "PECULIARLY"
		self.definitions = [u'in a strange, and sometimes unpleasant, way: ', u'very or especially: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
