

#calss header
class _INEXTRICABLE():
	def __init__(self,): 
		self.name = "INEXTRICABLE"
		self.definitions = [u'unable to be separated, released, or escaped from: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
