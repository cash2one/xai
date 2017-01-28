

#calss header
class _TRIUMPHAL():
	def __init__(self,): 
		self.name = "TRIUMPHAL"
		self.definitions = [u'used to refer to something that celebrates a great victory (= winning a war or competition)or success: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
