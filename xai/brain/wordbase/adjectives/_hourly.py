

#calss header
class _HOURLY():
	def __init__(self,): 
		self.name = "HOURLY"
		self.definitions = [u'done or happening every hour: ', u'the amount that is charged or earned every hour']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
