

#calss header
class _RIPPED():
	def __init__(self,): 
		self.name = "RIPPED"
		self.definitions = [u'having strong, well-developed muscles that can be seen through the skin: ', u'very drunk or under the influence of drugs: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
