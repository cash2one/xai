

#calss header
class _IMMEDIATELY():
	def __init__(self,): 
		self.name = "IMMEDIATELY"
		self.definitions = [u'now or without waiting or thinking: ', u'close to something or someone in distance or time: ', u'closely or directly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
