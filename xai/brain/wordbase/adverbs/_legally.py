

#calss header
class _LEGALLY():
	def __init__(self,): 
		self.name = "LEGALLY"
		self.definitions = [u'as stated by the law: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
