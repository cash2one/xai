

#calss header
class _CONSCIOUS():
	def __init__(self,): 
		self.name = "CONSCIOUS"
		self.definitions = [u'to notice that a particular thing or person exists or is present: ', u'awake, thinking, and knowing what is happening around you: ', u'determined and intentional: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
