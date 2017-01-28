

#calss header
class _IMMANENT():
	def __init__(self,): 
		self.name = "IMMANENT"
		self.definitions = [u'present as a natural and permanent part of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
