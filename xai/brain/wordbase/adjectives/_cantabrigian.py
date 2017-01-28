

#calss header
class _CANTABRIGIAN():
	def __init__(self,): 
		self.name = "CANTABRIGIAN"
		self.definitions = [u'relating to the town or university of Cambridge in England, or to the university of Harvard in Cambridge, Massachusetts']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
