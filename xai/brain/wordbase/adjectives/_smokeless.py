

#calss header
class _SMOKELESS():
	def __init__(self,): 
		self.name = "SMOKELESS"
		self.definitions = [u'not causing or allowing smoke: ', u'tobacco that is chewed or put in the mouth']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
