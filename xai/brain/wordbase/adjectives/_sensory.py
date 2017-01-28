

#calss header
class _SENSORY():
	def __init__(self,): 
		self.name = "SENSORY"
		self.definitions = [u'connected with the physical senses of touch, smell, taste, hearing, and sight']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
