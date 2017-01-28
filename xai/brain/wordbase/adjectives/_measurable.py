

#calss header
class _MEASURABLE():
	def __init__(self,): 
		self.name = "MEASURABLE"
		self.definitions = [u'able to be measured, or large enough to be noticed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
