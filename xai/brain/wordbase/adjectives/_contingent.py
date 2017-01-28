

#calss header
class _CONTINGENT():
	def __init__(self,): 
		self.name = "CONTINGENT"
		self.definitions = [u'depending on something else in the future in order to happen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
