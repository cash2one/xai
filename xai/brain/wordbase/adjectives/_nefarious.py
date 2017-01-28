

#calss header
class _NEFARIOUS():
	def __init__(self,): 
		self.name = "NEFARIOUS"
		self.definitions = [u'(especially of activities) morally bad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
