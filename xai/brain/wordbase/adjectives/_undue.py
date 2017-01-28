

#calss header
class _UNDUE():
	def __init__(self,): 
		self.name = "UNDUE"
		self.definitions = [u'to a level that is more than is necessary, acceptable, or reasonable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
