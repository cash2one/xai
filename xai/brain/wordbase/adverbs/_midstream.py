

#calss header
class _MIDSTREAM():
	def __init__(self,): 
		self.name = "MIDSTREAM"
		self.definitions = [u'in the middle of an activity, often one that is interrupted']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
