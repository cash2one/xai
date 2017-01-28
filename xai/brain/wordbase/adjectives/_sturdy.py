

#calss header
class _STURDY():
	def __init__(self,): 
		self.name = "STURDY"
		self.definitions = [u'physically strong and solid or thick, and therefore unlikely to break or be hurt: ', u'strong and determined: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
