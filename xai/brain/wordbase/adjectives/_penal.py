

#calss header
class _PENAL():
	def __init__(self,): 
		self.name = "PENAL"
		self.definitions = [u'of or relating to punishment given by law: ', u'having a harmful effect; causing disadvantage: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
