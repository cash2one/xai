

#calss header
class _RECURRING():
	def __init__(self,): 
		self.name = "RECURRING"
		self.definitions = [u'happening many times, or happening again: ', u'(of a number) repeating itself for ever following a decimal point: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
