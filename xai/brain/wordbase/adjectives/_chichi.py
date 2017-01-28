

#calss header
class _CHICHI():
	def __init__(self,): 
		self.name = "CHICHI"
		self.definitions = [u'trying too hard to be decorated in a stylish or attractive way and therefore having no real style or beauty: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
