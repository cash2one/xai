

#calss header
class _SYCOPHANTIC():
	def __init__(self,): 
		self.name = "SYCOPHANTIC"
		self.definitions = [u'(of a person or of behaviour) praising people in authority in a way that is not sincere, usually in order to get some advantage from them: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
