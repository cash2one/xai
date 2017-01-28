

#calss header
class _EXUBERANT():
	def __init__(self,): 
		self.name = "EXUBERANT"
		self.definitions = [u'(especially of people and their behaviour) very energetic: ', u'(of plants) strong and growing quickly']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
