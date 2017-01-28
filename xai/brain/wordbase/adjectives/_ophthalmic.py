

#calss header
class _OPHTHALMIC():
	def __init__(self,): 
		self.name = "OPHTHALMIC"
		self.definitions = [u'relating to ophthalmology (= the scientific study of eyes and their diseases)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
