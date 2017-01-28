

#calss header
class _UNKIND():
	def __init__(self,): 
		self.name = "UNKIND"
		self.definitions = [u"not treating someone very well; not considering someone's feelings: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
