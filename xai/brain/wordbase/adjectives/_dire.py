

#calss header
class _DIRE():
	def __init__(self,): 
		self.name = "DIRE"
		self.definitions = [u'very serious or extreme: ', u'very bad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
