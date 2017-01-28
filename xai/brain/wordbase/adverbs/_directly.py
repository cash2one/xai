

#calss header
class _DIRECTLY():
	def __init__(self,): 
		self.name = "DIRECTLY"
		self.definitions = [u'without anything else being involved or in between: ', u'honestly, even when it might make people feel uncomfortable: ', u'very soon: ', u'immediately: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
