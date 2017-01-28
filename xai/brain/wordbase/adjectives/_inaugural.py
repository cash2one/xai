

#calss header
class _INAUGURAL():
	def __init__(self,): 
		self.name = "INAUGURAL"
		self.definitions = [u'An inaugural speech is the first speech someone gives when starting an important new job: ', u'An inaugural event is the first in a series of planned events: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
