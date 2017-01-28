

#calss header
class _DESPONDENT():
	def __init__(self,): 
		self.name = "DESPONDENT"
		self.definitions = [u'unhappy and with no hope or enthusiasm: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
