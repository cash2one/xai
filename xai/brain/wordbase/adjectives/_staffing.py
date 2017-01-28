

#calss header
class _STAFFING():
	def __init__(self,): 
		self.name = "STAFFING"
		self.definitions = [u'relating to the staff (= employees) of an organization: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
