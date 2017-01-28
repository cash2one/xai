

#calss header
class _DUTIFUL():
	def __init__(self,): 
		self.name = "DUTIFUL"
		self.definitions = [u'doing everything that you should do: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
