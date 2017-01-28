

#calss header
class _CAMPY():
	def __init__(self,): 
		self.name = "CAMPY"
		self.definitions = [u"used to describe an activity, or someone's behaviour or appearance, that is funny because it is obviously intended to be strange or shocking: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
