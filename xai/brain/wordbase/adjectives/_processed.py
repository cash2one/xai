

#calss header
class _PROCESSED():
	def __init__(self,): 
		self.name = "PROCESSED"
		self.definitions = [u'Processed food has had some sort of chemical or industrial treatment in order to cook it, preserve it, or improve its taste or appearance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
