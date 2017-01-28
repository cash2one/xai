

#calss header
class _CRESTED():
	def __init__(self,): 
		self.name = "CRESTED"
		self.definitions = [u'A crested bird has a growth of feathers on its head: ', u'Crested paper has a crest (= design) at the top: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
