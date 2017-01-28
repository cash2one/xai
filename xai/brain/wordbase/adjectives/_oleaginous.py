

#calss header
class _OLEAGINOUS():
	def __init__(self,): 
		self.name = "OLEAGINOUS"
		self.definitions = [u'extremely polite, kind, or helpful in a false way that is intended to bring some advantage to yourself']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
