

#calss header
class _MITIGATING():
	def __init__(self,): 
		self.name = "MITIGATING"
		self.definitions = [u'making something less harmful, unpleasant, or bad: ', u'causing you to judge a crime to be less serious or to make the punishment less severe: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
