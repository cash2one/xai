

#calss header
class _BANGING():
	def __init__(self,): 
		self.name = "BANGING"
		self.definitions = [u'very good or enjoyable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
