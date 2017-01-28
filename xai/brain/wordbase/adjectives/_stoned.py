

#calss header
class _STONED():
	def __init__(self,): 
		self.name = "STONED"
		self.definitions = [u'experiencing the effects of a drug, such as cannabis: ', u'with the stone (= seed) removed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
