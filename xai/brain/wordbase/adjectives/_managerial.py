

#calss header
class _MANAGERIAL():
	def __init__(self,): 
		self.name = "MANAGERIAL"
		self.definitions = [u'relating to a manager or management: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
