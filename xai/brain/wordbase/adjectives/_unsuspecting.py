

#calss header
class _UNSUSPECTING():
	def __init__(self,): 
		self.name = "UNSUSPECTING"
		self.definitions = [u'trusting; not realizing there is any danger or harm: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
