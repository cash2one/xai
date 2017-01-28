

#calss header
class _KIND():
	def __init__(self,): 
		self.name = "KIND"
		self.definitions = [u"generous, helpful, and thinking about other people's feelings: ", u'not causing harm or damage: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
