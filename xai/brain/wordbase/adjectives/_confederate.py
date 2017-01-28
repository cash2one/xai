

#calss header
class _CONFEDERATE():
	def __init__(self,): 
		self.name = "CONFEDERATE"
		self.definitions = [u'united in or part of a confederacy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
