

#calss header
class _EPOCHAL():
	def __init__(self,): 
		self.name = "EPOCHAL"
		self.definitions = [u'used to refer to times or events that are very important because they involve new developments and great change: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
