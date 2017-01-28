

#calss header
class _INCONGRUOUS():
	def __init__(self,): 
		self.name = "INCONGRUOUS"
		self.definitions = [u'unusual or different from what is around or from what is generally happening: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
