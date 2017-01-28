

#calss header
class _AMBASSADORIAL():
	def __init__(self,): 
		self.name = "AMBASSADORIAL"
		self.definitions = [u'belonging or relating to an ambassador: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
