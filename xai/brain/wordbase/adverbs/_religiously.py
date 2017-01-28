

#calss header
class _RELIGIOUSLY():
	def __init__(self,): 
		self.name = "RELIGIOUSLY"
		self.definitions = [u'in ways or subjects relating to religion: ', u'If you do something religiously, you do it regularly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
