

#calss header
class _HALFWAY():
	def __init__(self,): 
		self.name = "HALFWAY"
		self.definitions = [u'in the middle of something, or at a place that is equally far from two other places: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
