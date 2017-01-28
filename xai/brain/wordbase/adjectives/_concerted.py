

#calss header
class _CONCERTED():
	def __init__(self,): 
		self.name = "CONCERTED"
		self.definitions = [u'planned or done together for a shared purpose: ', u'A concerted effort or attempt is determined and serious: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
