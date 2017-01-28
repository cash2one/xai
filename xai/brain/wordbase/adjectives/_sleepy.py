

#calss header
class _SLEEPY():
	def __init__(self,): 
		self.name = "SLEEPY"
		self.definitions = [u'tired and wanting to sleep', u'A sleepy place is quiet and without much activity or excitement: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
