

#calss header
class _QUILTED():
	def __init__(self,): 
		self.name = "QUILTED"
		self.definitions = [u'(especially of clothes) filled with thick soft material that is sewn in place: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
