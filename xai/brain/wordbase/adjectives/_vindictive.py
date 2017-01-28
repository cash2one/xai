

#calss header
class _VINDICTIVE():
	def __init__(self,): 
		self.name = "VINDICTIVE"
		self.definitions = [u'having or showing a wish to harm someone because you think that they harmed you; unwilling to forgive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
