

#calss header
class _HELPFUL():
	def __init__(self,): 
		self.name = "HELPFUL"
		self.definitions = [u'willing to help, or useful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
