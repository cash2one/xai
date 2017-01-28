

#calss header
class _WHEREVER():
	def __init__(self,): 
		self.name = "WHEREVER"
		self.definitions = [u'to or in any or every place: ', u'in every case: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
