

#calss header
class _UNREFINED():
	def __init__(self,): 
		self.name = "UNREFINED"
		self.definitions = [u'in a natural state, without having been through a chemical or industrial process to remove unwanted parts; not refined: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
