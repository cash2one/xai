

#calss header
class _PATCHY():
	def __init__(self,): 
		self.name = "PATCHY"
		self.definitions = [u'only existing or happening in some parts: ', u'sometimes good and sometimes bad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
