

#calss header
class _HUDDLED():
	def __init__(self,): 
		self.name = "HUDDLED"
		self.definitions = [u'standing or sitting close together: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
