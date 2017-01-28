

#calss header
class _HAUNTING():
	def __init__(self,): 
		self.name = "HAUNTING"
		self.definitions = [u'beautiful, but in a sad way and often in a way that cannot be forgotten: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
