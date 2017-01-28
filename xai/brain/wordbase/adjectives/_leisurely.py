

#calss header
class _LEISURELY():
	def __init__(self,): 
		self.name = "LEISURELY"
		self.definitions = [u'used to describe an action that is done in a relaxed way, without hurrying: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
