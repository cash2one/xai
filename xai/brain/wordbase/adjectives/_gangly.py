

#calss header
class _GANGLY():
	def __init__(self,): 
		self.name = "GANGLY"
		self.definitions = [u'A person, usually a boy or young man, who is very tall and thin and moves awkwardly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
