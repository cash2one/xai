

#calss header
class _STANDOFFISH():
	def __init__(self,): 
		self.name = "STANDOFFISH"
		self.definitions = [u'behaving in a slightly unfriendly and too formal way']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
