

#calss header
class _JUGULAR():
	def __init__(self,): 
		self.name = "JUGULAR"
		self.definitions = [u'relating to the throat or neck']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
