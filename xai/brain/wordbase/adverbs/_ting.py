

#calss header
class _TING():
	def __init__(self,): 
		self.name = "TING"
		self.definitions = [u'(with) a clear, high ringing sound: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
