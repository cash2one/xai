

#calss header
class _COGENT():
	def __init__(self,): 
		self.name = "COGENT"
		self.definitions = [u'A cogent argument, reason, etc. is clearly expressed and persuades people to believe it.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
