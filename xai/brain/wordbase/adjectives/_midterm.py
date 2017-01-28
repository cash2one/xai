

#calss header
class _MIDTERM():
	def __init__(self,): 
		self.name = "MIDTERM"
		self.definitions = [u'in the middle of the period when a government is in office: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
