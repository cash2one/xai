

#calss header
class _RUNAWAY():
	def __init__(self,): 
		self.name = "RUNAWAY"
		self.definitions = [u'having escaped or run away from somewhere: ', u'out of control: ', u'Runaway success is surprisingly sudden or great: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
