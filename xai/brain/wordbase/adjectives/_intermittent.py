

#calss header
class _INTERMITTENT():
	def __init__(self,): 
		self.name = "INTERMITTENT"
		self.definitions = [u'not happening regularly or continuously; stopping and starting repeatedly or with periods in between: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
