

#calss header
class _SOUTHERLY():
	def __init__(self,): 
		self.name = "SOUTHERLY"
		self.definitions = [u'towards or in the south: ', u'a wind that comes from the south']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
