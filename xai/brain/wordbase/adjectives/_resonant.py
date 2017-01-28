

#calss header
class _RESONANT():
	def __init__(self,): 
		self.name = "RESONANT"
		self.definitions = [u'clear and loud, or causing sounds to be clear and loud: ', u'making you think of a similar experience or memory: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
