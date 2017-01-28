

#calss header
class _FURRY():
	def __init__(self,): 
		self.name = "FURRY"
		self.definitions = [u'covered with fur: ', u'Furry things are made from a soft material that looks like fur: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
