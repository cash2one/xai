

#calss header
class _UNEXPLAINED():
	def __init__(self,): 
		self.name = "UNEXPLAINED"
		self.definitions = [u'Unexplained events, behaviour, etc. are ones for which people do not know or understand the reason: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
