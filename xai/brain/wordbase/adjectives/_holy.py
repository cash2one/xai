

#calss header
class _HOLY():
	def __init__(self,): 
		self.name = "HOLY"
		self.definitions = [u'related to a religion or a god: ', u'very religious or pure: ', u'used to show that you think something is surprising, shocking, or impressive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
