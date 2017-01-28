

#calss header
class _HEALTHY():
	def __init__(self,): 
		self.name = "HEALTHY"
		self.definitions = [u'strong and well: ', u'showing that you are strong and well: ', u'good for your health: ', u'successful and strong: ', u'normal and showing good judgment: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
