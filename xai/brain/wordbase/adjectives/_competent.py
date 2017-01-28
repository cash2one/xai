

#calss header
class _COMPETENT():
	def __init__(self,): 
		self.name = "COMPETENT"
		self.definitions = [u'able to do something well: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
