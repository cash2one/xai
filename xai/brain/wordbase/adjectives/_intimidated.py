

#calss header
class _INTIMIDATED():
	def __init__(self,): 
		self.name = "INTIMIDATED"
		self.definitions = [u'frightened or nervous because you are not confident in a situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
