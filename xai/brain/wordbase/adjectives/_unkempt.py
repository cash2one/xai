

#calss header
class _UNKEMPT():
	def __init__(self,): 
		self.name = "UNKEMPT"
		self.definitions = [u'untidy; not cared for: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
