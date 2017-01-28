

#calss header
class _VIRILE():
	def __init__(self,): 
		self.name = "VIRILE"
		self.definitions = [u'A virile man, especially a young man, is full of sexual strength and energy in a way that is considered attractive: ', u'powerful, strong, and energetic: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
