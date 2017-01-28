

#calss header
class _TREMULOUS():
	def __init__(self,): 
		self.name = "TREMULOUS"
		self.definitions = [u"If a person's voice or a part of their body is tremulous, it is shaking slightly: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
