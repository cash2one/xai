

#calss header
class _LETHARGIC():
	def __init__(self,): 
		self.name = "LETHARGIC"
		self.definitions = [u'having little energy; feeling unwilling and unable to do anything: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
