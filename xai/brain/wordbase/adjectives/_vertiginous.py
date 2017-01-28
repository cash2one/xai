

#calss header
class _VERTIGINOUS():
	def __init__(self,): 
		self.name = "VERTIGINOUS"
		self.definitions = [u'causing or experiencing the feeling that everything is spinning around: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
