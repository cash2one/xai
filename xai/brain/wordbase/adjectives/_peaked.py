

#calss header
class _PEAKED():
	def __init__(self,): 
		self.name = "PEAKED"
		self.definitions = [u'A peaked hat has a peak at the front: ', u'rising to a point', u'slightly ill, often looking pale']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
