

#calss header
class _AUTOIMMUNE():
	def __init__(self,): 
		self.name = "AUTOIMMUNE"
		self.definitions = [u"relating to a condition in which someone's antibodies attack substances that are naturally found in the body: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
